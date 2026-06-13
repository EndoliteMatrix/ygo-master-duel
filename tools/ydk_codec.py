#!/usr/bin/env python3
"""ydk_codec — Yu-Gi-Oh deck-file codec for Master Duel.

Resolves card name <-> passcode, converts .ydk <-> ydke://, and checks Master
Duel availability. Cache-first (instant, offline, repeatable); falls back to the
ygoprodeck API for unknown cards, then caches them. The cache is the ground truth
once seeded, and is seeded FROM the API (never hand-typed) so every id is
primary-sourced.

Usage:
  ydk_codec.py build  <list.txt> [--out deck.ydk] [--no-net]
  ydk_codec.py decode <deck.ydk | 'ydke://...'> [--no-net]
  ydk_codec.py id     "Card Name" [--no-net]
  ydk_codec.py name   <passcode>  [--no-net]
  ydk_codec.py verify <deck.ydk | 'ydke://...'> [--no-net]
  ydk_codec.py seed-from-ydk <a.ydk> [b.ydk ...]      # fetch names from API -> cache
  ydk_codec.py seed   <id,id,id>                       # fetch these ids -> cache

Decklist (.txt) input for `build` — sections + quantities, e.g.:
  #main
  3 Dark Magician
  3x Magician's Rod
  Maxx "C"
  46986414            # a bare passcode also works
  #extra
  2 Dark Paladin
  #side

API note: ygoprodeck is fetched via `curl` on purpose — python-urllib is
Cloudflare-blocked on this box. `--no-net` forbids any fetch (cache-only).
"""
import base64, json, os, re, struct, subprocess, sys, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = os.path.join(HERE, "card-id-cache.json")
API = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

# ---------- cache ----------
def load_cache():
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH) as f:
            c = json.load(f)
    else:
        c = {}
    c.setdefault("by_id", {})     # "passcode"(str) -> canonical card name
    c.setdefault("by_name", {})   # normalized name -> passcode (int)
    c.setdefault("md", {})        # "passcode"(str) -> bool (in Master Duel)
    return c

def save_cache(c):
    with open(CACHE_PATH, "w") as f:
        json.dump(c, f, ensure_ascii=False, indent=1, sort_keys=True)

def norm(s):                      # exact-ish key
    return re.sub(r"\s+", " ", s.strip().casefold())

def loose(s):                     # punctuation-insensitive key
    return re.sub(r"[^a-z0-9]", "", s.casefold())

def cache_put(c, cid, name, md=None):
    cid = int(cid)
    c["by_id"][str(cid)] = name
    c["by_name"][norm(name)] = cid
    c["by_name"][loose(name)] = cid
    if md is not None:
        c["md"][str(cid)] = bool(md)

# ---------- api (via curl) ----------
def curl(url):
    try:
        out = subprocess.run(["curl", "-s", "-H", "User-Agent: Mozilla/5.0", url],
                             capture_output=True, text=True, timeout=30)
        return json.loads(out.stdout) if out.stdout.strip() else None
    except Exception:
        return None

def card_in_md(card):
    for mi in card.get("misc_info", []) or []:
        if "Master Duel" in (mi.get("formats") or []):
            return True
    return False

def api_by_ids(ids):
    if not ids: return []
    url = API + "?misc=yes&id=" + ",".join(str(i) for i in ids)
    d = curl(url)
    return (d or {}).get("data", []) or []

def api_by_name(name):
    url = API + "?misc=yes&name=" + urllib.parse.quote(name)
    d = curl(url)
    data = (d or {}).get("data")
    if data: return data
    url = API + "?misc=yes&fname=" + urllib.parse.quote(name)   # fuzzy fallback
    d = curl(url)
    return (d or {}).get("data") or []

# ---------- resolution ----------
def resolve_id_to_name(c, cid, net):
    s = str(int(cid))
    if s in c["by_id"]:
        return c["by_id"][s]
    if not net:
        return None
    for card in api_by_ids([cid]):
        cache_put(c, card["id"], card["name"], card_in_md(card))
        # also cache alt-art ids that share the name
        for img in card.get("card_images", []) or []:
            aid = img.get("id")
            if aid and str(aid) not in c["by_id"]:
                c["by_id"][str(aid)] = card["name"]
    return c["by_id"].get(s)

def resolve_name_to_id(c, name, net):
    for k in (norm(name), loose(name)):
        if k in c["by_name"]:
            return c["by_name"][k], None
    if name.strip().isdigit():
        cid = int(name.strip())
        nm = resolve_id_to_name(c, cid, net)
        return (cid, None) if nm else (None, "unknown passcode")
    if not net:
        return None, "not in cache (--no-net)"
    data = api_by_name(name)
    if not data:
        return None, "no API match"
    # prefer an exact (normalized) name hit; else if 1 result take it; else ambiguous
    exact = [d for d in data if norm(d["name"]) == norm(name) or loose(d["name"]) == loose(name)]
    pick = exact[0] if exact else (data[0] if len(data) == 1 else None)
    if pick is None:
        names = ", ".join(d["name"] for d in data[:6])
        return None, f"ambiguous ({len(data)} matches: {names}...)"
    cache_put(c, pick["id"], pick["name"], card_in_md(pick))
    return pick["id"], None

# ---------- ydk / ydke ----------
def parse_decklist(text):
    secs = {"main": [], "extra": [], "side": []}
    cur = "main"
    for ln in text.splitlines():
        s = ln.strip()
        if not s:
            continue
        low = s.lower()
        if low.startswith("#main"): cur = "main"; continue
        if low.startswith("#extra"): cur = "extra"; continue
        if low.startswith("!side") or low.startswith("#side"): cur = "side"; continue
        if s.startswith("#"):       # a real comment (not a section header)
            continue
        s = re.split(r"\s+#", s)[0].strip()   # strip trailing inline comment FIRST
        if not s:
            continue
        m = re.match(r"^(\d+)\s*[xX]?\s+(.+)$", s)
        if m and not s.isdigit():
            qty, card = int(m.group(1)), m.group(2).strip()
        else:
            qty, card = 1, s
        secs[cur].append((qty, card))
    return secs

def read_ydk(path):
    secs = {"main": [], "extra": [], "side": []}
    cur = None
    for ln in open(path):
        s = ln.strip()
        low = s.lower()
        if low.startswith("#main"): cur = "main"; continue
        if low.startswith("#extra"): cur = "extra"; continue
        if low.startswith("!side") or low.startswith("#side"): cur = "side"; continue
        if s.startswith("#") or not s: continue
        if cur and s.isdigit(): secs[cur].append(int(s))
    return secs

def ydke_encode(main, extra, side):
    e = lambda x: base64.b64encode(b"".join(struct.pack("<I", i) for i in x)).decode()
    return f"ydke://{e(main)}!{e(extra)}!{e(side)}!"

def ydke_decode(code):
    body = code.strip()[len("ydke://"):] if code.strip().startswith("ydke://") else code.strip()
    parts = body.split("!")
    out = []
    for p in parts[:3]:
        raw = base64.b64decode(p) if p else b""
        out.append([struct.unpack("<I", raw[i:i+4])[0] for i in range(0, len(raw), 4)])
    while len(out) < 3: out.append([])
    return out  # [main, extra, side]

# ---------- commands ----------
def cmd_build(args):
    net = "--no-net" not in args
    args = [a for a in args if a != "--no-net"]
    src = args[0]
    out = None
    if "--out" in args: out = args[args.index("--out") + 1]
    text = open(src).read()
    secs = parse_decklist(text)
    c = load_cache()
    ids = {"main": [], "extra": [], "side": []}
    problems, nonmd = [], []
    for sec in ("main", "extra", "side"):
        for qty, card in secs[sec]:
            cid, err = resolve_name_to_id(c, card, net)
            if cid is None:
                problems.append(f"{sec}: {card}  -> {err}")
                continue
            if c["md"].get(str(cid)) is False:
                nonmd.append(c["by_id"].get(str(cid), card))
            ids[sec] += [cid] * qty
    save_cache(c)
    if problems:
        print("UNRESOLVED (fix these names, nothing written):", file=sys.stderr)
        for p in problems: print("  " + p, file=sys.stderr)
        sys.exit(2)
    ydke = ydke_encode(ids["main"], ids["extra"], ids["side"])
    if out:
        with open(out, "w") as f:
            f.write("#created by ydk_codec\n#main\n")
            f.write("\n".join(map(str, ids["main"])) + "\n#extra\n")
            f.write("\n".join(map(str, ids["extra"])) + "\n!side\n")
            f.write(("\n".join(map(str, ids["side"])) + "\n") if ids["side"] else "")
        print(f"wrote {out}  (main {len(ids['main'])} / extra {len(ids['extra'])} / side {len(ids['side'])})")
    print(ydke)
    if nonmd:
        print("WARNING — not flagged as Master Duel: " + ", ".join(sorted(set(nonmd))), file=sys.stderr)

def cmd_decode(args):
    net = "--no-net" not in args
    args = [a for a in args if a != "--no-net"]
    arg = args[0]
    if arg.strip().startswith("ydke://") or ("!" in arg and not os.path.exists(arg)):
        main, extra, side = ydke_decode(arg)
        secs = {"main": main, "extra": extra, "side": side}
    else:
        secs = read_ydk(arg)
    c = load_cache()
    for sec in ("main", "extra", "side"):
        ids = secs[sec]
        if not ids and sec == "side": continue
        print(f"#{sec}  ({len(ids)})")
        counts = {}
        order = []
        for i in ids:
            if i not in counts: order.append(i)
            counts[i] = counts.get(i, 0) + 1
        for i in order:
            nm = resolve_id_to_name(c, i, net) or "??? UNKNOWN"
            print(f"  {counts[i]}x {nm}  [{i}]")
    save_cache(c)

def cmd_verify(args):
    net = "--no-net" not in args
    args = [a for a in args if a != "--no-net"]
    arg = args[0]
    secs = ({"main": ydke_decode(arg)[0], "extra": ydke_decode(arg)[1], "side": ydke_decode(arg)[2]}
            if (arg.startswith("ydke://") or ("!" in arg and not os.path.exists(arg))) else read_ydk(arg))
    c = load_cache()
    issues = []
    sizes = {"main": (40, 60), "extra": (0, 15), "side": (0, 15)}
    for sec in ("main", "extra", "side"):
        ids = secs[sec]
        lo, hi = sizes[sec]
        if not (lo <= len(ids) <= hi):
            issues.append(f"{sec} size {len(ids)} (legal {lo}-{hi})")
        counts = {}
        for i in ids: counts[i] = counts.get(i, 0) + 1
        for i, n in counts.items():
            nm = resolve_id_to_name(c, i, net) or f"??? {i}"
            if n > 3: issues.append(f"{nm}: {n} copies (>3)")
            if c["md"].get(str(i)) is False: issues.append(f"{nm}: not in Master Duel")
            if resolve_id_to_name(c, i, net) is None: issues.append(f"{i}: unresolved passcode")
    save_cache(c)
    if issues:
        print("ISSUES:")
        for x in issues: print("  - " + x)
        print("\nNote: per-card Master Duel banlist LIMITS (e.g. Maxx \"C\" Limited 1) are not in the API — cross-check PATCH-BANLIST.md.")
        sys.exit(1)
    print("OK — legal sizes, <=3 each, all resolved. (Still cross-check the MD banlist for limited cards.)")

def cmd_id(args):
    net = "--no-net" not in args
    args = [a for a in args if a != "--no-net"]
    c = load_cache()
    cid, err = resolve_name_to_id(c, args[0], net)
    save_cache(c)
    print(cid if cid else f"no match: {err}")

def cmd_name(args):
    net = "--no-net" not in args
    args = [a for a in args if a != "--no-net"]
    c = load_cache()
    nm = resolve_id_to_name(c, int(args[0]), net)
    save_cache(c)
    print(nm or "??? unknown passcode")

def cmd_seed(args):
    c = load_cache()
    ids = [int(x) for x in args[0].replace(" ", "").split(",") if x]
    added = 0
    for card in api_by_ids(ids):
        cache_put(c, card["id"], card["name"], card_in_md(card))
        for img in card.get("card_images", []) or []:
            if str(img.get("id")) not in c["by_id"]:
                c["by_id"][str(img["id"])] = card["name"]
        added += 1
    save_cache(c)
    print(f"seeded {added} cards into {CACHE_PATH}")

def cmd_seed_from_ydk(args):
    ids = set()
    for path in args:
        secs = read_ydk(path)
        for sec in secs.values(): ids |= set(sec)
    cmd_seed([",".join(map(str, sorted(ids)))])

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(0)
    cmd, rest = sys.argv[1], sys.argv[2:]
    table = {"build": cmd_build, "decode": cmd_decode, "verify": cmd_verify,
             "id": cmd_id, "name": cmd_name, "seed": cmd_seed,
             "seed-from-ydk": cmd_seed_from_ydk}
    if cmd not in table:
        print(__doc__); sys.exit(1)
    table[cmd](rest)

if __name__ == "__main__":
    main()
