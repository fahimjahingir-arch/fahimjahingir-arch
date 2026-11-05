"""Generate banner.svg: an original pixel ninja breathes a fireball that ignites the name.

Pure SMIL animation on one 8-second clock, so it plays inside a GitHub README <img>.
Run:  python make_banner.py
"""

from __future__ import annotations

import random
from pathlib import Path

W, H, T = 1200, 300, 8.0
OUT = Path(__file__).with_name("banner.svg")
NAME = "FAHIM JAHINGIR"
TAGLINE = "AI/ML - DATA ENGINEERING - BIOTECH"

# ---------------------------------------------------------------- ninja (original design)
NINJA_PAL = {
    "k": "#0a0a12",  # outline
    "h": "#1f2336",  # hair
    "H": "#3d4466",  # hair highlight
    "b": "#2b2f45",  # headband cloth
    "p": "#cfd8e3",  # headband plate
    "P": "#8793a6",  # plate shade
    "s": "#f2c38b",  # skin
    "t": "#cf9459",  # skin shade
    "e": "#111111",  # eye
    "w": "#ffffff",
    "r": "#e63946",  # scarf / sash
    "R": "#9d1b26",
    "g": "#25345e",  # gi
    "G": "#16203d",
    "l": "#3a5296",
    "n": "#3a2d2a",  # sandals
    "x": "#d9d4c7",  # leg wraps
}
NINJA = [
    "........k...k...........",
    ".......khk.khk...k......",
    "......khhhkhhhk.khk.....",
    "..k..khhHhhhHhhkhhk.....",
    ".khkkhhhhHhhhhhhhhk.....",
    "..khhhhhhhhhhHhhhhhk....",
    "...khhhhhhhhhhhhhhhk....",
    "..khhhhhhhhhhhhhhhhhk...",
    "..khhbbbbbbbbbbpppPPk...",
    "..khhhhhhhhhsssssssssk..",
    "..khhhhhhhssssssweessk..",
    "..khhhhhhssssssssssstk..",
    "...khhhhhsssssssssssssk.",
    "...khhhhhtssssssssssskk.",
    "....khhhttsssssssssk....",
    ".....khkkttttsssssk.....",
    "......k..ktttttkk.......",
    "RrRr....krrrrrrrrk......",
    ".rRrr..krrrrrrrrrrk.....",
    "..rRrrrrrrrrrrrrrrk.....",
    "......kgggggglgggk......",
    ".....kggggggglllggk.....",
    ".....kGgggggggllgggk....",
    ".....kGggggggglggggk....",
    ".....kGGgggggggggggk....",
    ".....krrrrrrrrrrrrrk....",
    ".....kRrrrrrrrrrrrRk....",
    "....kGGggggggggggggk....",
    "....kGGgggggk.kgggggk...",
    "...kGGggggk...kggggggk..",
    "...kGgggggk....kgggggk..",
    "..kGggggk.......kggggk..",
    "..kxxxxxk.......kxxxxk..",
    ".knnnnnnk......knnnnnnk.",
    ".kkkkkkkk......kkkkkkkk.",
]
# arms raised, hands sealed in front of the mouth (drawn over the base sprite)
NINJA_ARMS = {
    11: "...................kkkk.",
    12: "..................kssssk",
    13: "..................kstsk.",
    14: ".................kkssssk",
    15: "................klkttkk.",
    16: "...............klggkk...",
    17: "..............klgggk....",
    18: ".............klgggk.....",
    19: "............kgggGk......",
}
NX, NY, NS = 56, 36, 7  # ninja origin + pixel size
MOUTH = (NX + 23 * NS, NY + 14 * NS)

# ---------------------------------------------------------------- fireball (two flicker frames)
FIRE_PAL = {"R": "#c1121f", "o": "#f77f00", "O": "#fb5607", "y": "#fcbf49", "w": "#fff3c4"}
FIRE_A = [
    "..........R.....RRRRR.....",
    "....R...RRORRRRRooooORR...",
    ".R....RROooooooOoyyyooOR..",
    "...RROOoooyyyyyyyywwyyoOR.",
    "RROOooooyyyywwwwwwwwwyyoOR",
    ".RROOoooyyywwwwwwwwwwyyoOR",
    "...RROooooyyyywwwwwwyyooR.",
    ".R....RROOoooyyyyyyyyoOR..",
    "....R...RRROOooooooORR....",
    "..........RRR.RRRRRR......",
]
FIRE_B = [
    ".........R......RRRRR.....",
    "..R...RRRORRRRRRooooORR...",
    "....RRROOoooooooOyyyooOR..",
    ".RRROOooooyyyyyyyywwyyoOR.",
    "..ROOoooyyyywwwwwwwwwyyoOR",
    "RRROOoooyyywwwwwwwwwwyyoOR",
    "..RROOoooyyyyywwwwwwyyooR.",
    "....RRROOOooyyyyyyyyyoOR..",
    "..R....RRROOooooooOORR....",
    ".........RRRR.RRRRRR......",
]
FS = 7
FIRE_W, FIRE_H = len(FIRE_A[0]) * FS, len(FIRE_A) * FS
T_LAUNCH, T_EXIT = 0.85, 2.65
FIRE_START, FIRE_END = MOUTH[0] + 12, W + FIRE_W  # x of fireball front

# ---------------------------------------------------------------- 5x7 pixel font
FONT = {
    "A": "01110 10001 10001 11111 10001 10001 10001", "B": "11110 10001 10001 11110 10001 10001 11110",
    "C": "01110 10001 10000 10000 10000 10001 01110", "D": "11110 10001 10001 10001 10001 10001 11110",
    "E": "11111 10000 10000 11110 10000 10000 11111", "F": "11111 10000 10000 11110 10000 10000 10000",
    "G": "01110 10001 10000 10111 10001 10001 01111", "H": "10001 10001 10001 11111 10001 10001 10001",
    "I": "01110 00100 00100 00100 00100 00100 01110", "J": "00111 00010 00010 00010 00010 10010 01100",
    "K": "10001 10010 10100 11000 10100 10010 10001", "L": "10000 10000 10000 10000 10000 10000 11111",
    "M": "10001 11011 10101 10101 10001 10001 10001", "N": "10001 10001 11001 10101 10011 10001 10001",
    "O": "01110 10001 10001 10001 10001 10001 01110", "P": "11110 10001 10001 11110 10000 10000 10000",
    "R": "11110 10001 10001 11110 10100 10010 10001", "S": "01111 10000 10000 01110 00001 00001 11110",
    "T": "11111 00100 00100 00100 00100 00100 00100", "U": "10001 10001 10001 10001 10001 10001 01110",
    "V": "10001 10001 10001 10001 10001 01010 00100", "W": "10001 10001 10001 10101 10101 10101 01010",
    "Y": "10001 10001 01010 00100 00100 00100 00100", "/": "00001 00010 00010 00100 01000 01000 10000",
    "-": "00000 00000 00000 01110 00000 00000 00000", " ": "00000 00000 00000 00000 00000 00000 00000",
}
TS = 9  # name pixel size
TX = 322
TY = MOUTH[1] - 7 * TS // 2 - 2
SUB_S, SUB_Y = 3, TY + 7 * TS + 34

rng = random.Random(11)


def cells_to_path(cells, x0: float, y0: float, s: float) -> str:
    return "".join(f"M{x0 + c * s:g} {y0 + r * s:g}h{s:g}v{s:g}h{-s:g}z" for r, c in cells)


def grid_paths(rows: list[str], pal: dict, x0: float, y0: float, s: float, overlay: dict | None = None) -> str:
    grid = [list(r) for r in rows]
    for r, line in (overlay or {}).items():
        for c, ch in enumerate(line):
            if ch != ".":
                grid[r][c] = ch
    by_colour: dict[str, list] = {}
    for r, line in enumerate(grid):
        for c, ch in enumerate(line):
            if ch in pal:
                by_colour.setdefault(pal[ch], []).append((r, c))
    return "".join(
        f'<path fill="{col}" d="{cells_to_path(cells, x0, y0, s)}"/>' for col, cells in by_colour.items()
    )


def text_cells(text: str) -> tuple[list[tuple[int, int]], list[int]]:
    cells, starts = [], []
    for i, ch in enumerate(text):
        starts.append(i * 6)
        for r, row in enumerate(FONT[ch].split()):
            cells += [(r, i * 6 + c) for c, bit in enumerate(row) if bit == "1"]
    return cells, starts


def anim(attr: str, frames: list[tuple[float, str]], mode: str = "linear", tag: str = "animate", extra: str = "") -> str:
    """One SMIL animation on the shared T-second loop; frames are (seconds, value)."""
    if frames[0][0] != 0:
        frames = [(0, frames[0][1]), *frames]
    if frames[-1][0] != T:
        frames = [*frames, (T, frames[-1][1])]
    kt = ";".join(f"{t / T:.4f}" for t, _ in frames)
    vals = ";".join(v for _, v in frames)
    return (f'<{tag} attributeName="{attr}" dur="{T}s" repeatCount="indefinite" '
            f'calcMode="{mode}" keyTimes="{kt}" values="{vals}" {extra}/>')


def front_time(x: float) -> float:
    """When the fireball front passes x."""
    return T_LAUNCH + (x - FIRE_START) / (FIRE_END - FIRE_START) * (T_EXIT - T_LAUNCH)


def build() -> str:
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
           'shape-rendering="crispEdges" role="img" aria-label="Fahim Jahingir - animated pixel banner">']

    name_cells, starts = text_cells(NAME)
    name_w = (len(NAME) * 6 - 1) * TS
    t0, t1 = front_time(TX), front_time(TX + name_w)

    out.append(f"""<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#07080f"/><stop offset=".65" stop-color="#140d24"/><stop offset="1" stop-color="#2a0f1d"/>
  </linearGradient>
  <linearGradient id="fire" gradientUnits="userSpaceOnUse" x1="0" y1="{TY}" x2="0" y2="{TY + 7 * TS}">
    <stop offset="0" stop-color="#fff1a8"/><stop offset=".3" stop-color="#ffbe0b"/>
    <stop offset=".62" stop-color="#fb5607"/><stop offset="1" stop-color="#c1121f"/>
  </linearGradient>
  <clipPath id="reveal"><rect x="{TX - 4}" y="0" height="{H}" width="0">
    {anim("width", [(t0, "0"), (t1, str(name_w + 8)), (T, str(name_w + 8))])}
  </rect></clipPath>
  <filter id="heat" x="-10%" y="-60%" width="120%" height="220%">
    <feTurbulence type="fractalNoise" baseFrequency="0.02 0.09" numOctaves="2" seed="3" result="n">
      <animate attributeName="seed" dur="0.6s" values="3;7;12;3" calcMode="discrete" repeatCount="indefinite"/>
    </feTurbulence>
    <feGaussianBlur in="SourceGraphic" stdDeviation="7" result="b"/>
    <feDisplacementMap in="b" in2="n" scale="18" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <filter id="soft"><feGaussianBlur stdDeviation="10"/></filter>
</defs>""")

    # backdrop: sky, stars, moon, rooftop
    out.append(f'<rect width="{W}" height="{H}" rx="18" fill="url(#sky)"/>')
    for _ in range(46):
        x, y = rng.randrange(20, W - 20), rng.randrange(14, 80)
        if TX - 20 < x < TX + name_w + 20 and y > TY - 20:
            continue
        s = rng.choice([3, 3, 4, 6])
        d = rng.uniform(2.2, 4.5)
        out.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="#cfd6ff" opacity=".7">'
                   f'<animate attributeName="opacity" values=".15;.9;.15" dur="{d:.2f}s" begin="{rng.uniform(0, 3):.2f}s" '
                   'repeatCount="indefinite"/></rect>')
    moon = ["..mmmm..", ".mmmmmm.", "mmmmmMmm", "mmMmmmmm", "mmmmmmMm", "mmmmmmmm", ".mmmMmm.", "..mmmm.."]
    out.append(grid_paths(moon, {"m": "#f4e7c5", "M": "#d8c99f"}, W - 92, 24, 6))
    ground_y = NY + len(NINJA) * NS
    out.append(f'<path fill="#120a14" d="M0 {ground_y}H{W}V{H - 18}a18 18 0 0 1 -18 18H18a18 18 0 0 1 -18 -18z"/>')
    out.append(f'<rect x="0" y="{ground_y}" width="{W}" height="4" fill="#2c1a2b"/>')
    for x in range(0, W, 48):
        out.append(f'<rect x="{x + 10}" y="{ground_y + 14}" width="18" height="4" fill="#1d1220"/>')

    # ninja with recoil on launch
    out.append('<g>' + anim("transform", [(T_LAUNCH, "0 0"), (T_LAUNCH + 0.08, "-7 0"),
                                          (T_LAUNCH + 0.45, "0 0")], tag="animateTransform", extra='type="translate"'))
    out.append(grid_paths(NINJA, NINJA_PAL, NX, NY, NS, NINJA_ARMS))
    # chakra charge at the hands
    mx, my = MOUTH
    out.append(f'<g opacity="0"><circle cx="{mx + 6}" cy="{my}" r="26" fill="#fb5607" filter="url(#soft)"/>'
               f'<rect x="{mx}" y="{my - 6}" width="12" height="12" fill="#ffd166"/>'
               f'<rect x="{mx + 14}" y="{my - 16}" width="6" height="6" fill="#f77f00"/>'
               f'<rect x="{mx + 10}" y="{my + 12}" width="6" height="6" fill="#fb5607"/>'
               + anim("opacity", [(0.1, "0"), (0.45, ".55"), (0.6, ".3"), (T_LAUNCH, "1"), (T_LAUNCH + 0.15, "0")])
               + "</g></g>")

    # name: shadow, glow, fire fill - all revealed behind the fireball
    name_d = cells_to_path(name_cells, TX, TY, TS)
    out.append('<g clip-path="url(#reveal)"><g>')
    out.append(anim("opacity", [(7.15, "1"), (7.75, "0"), (T, "0")]))
    out.append(f'<path d="{name_d}" fill="#ff5400" opacity=".55" filter="url(#heat)">'
               '<animate attributeName="opacity" values=".35;.65;.45;.6;.35" dur="1.3s" repeatCount="indefinite"/></path>')
    out.append(f'<path d="{cells_to_path(name_cells, TX + 4, TY + 4, TS)}" fill="#3d0613"/>')
    out.append(f'<path d="{name_d}" fill="url(#fire)"/>')
    for i, ch in enumerate(NAME):  # white-hot flash as each letter ignites
        if ch == " ":
            continue
        cells = [(r, c - starts[i]) for r, c in name_cells if starts[i] <= c < starts[i] + 5]
        ti = front_time(TX + starts[i] * TS + 2.5 * TS)
        out.append(f'<path d="{cells_to_path(cells, TX + starts[i] * TS, TY, TS)}" fill="#fffbe6" opacity="0">'
                   + anim("opacity", [(ti - 0.02, "0"), (ti + 0.04, "1"), (ti + 0.6, "0")]) + "</path>")
    # tagline fades in after the name
    sub_cells, _ = text_cells(TAGLINE)
    out.append(f'<path d="{cells_to_path(sub_cells, TX + 2, SUB_Y, SUB_S)}" fill="#f4a261" opacity="0">'
               + anim("opacity", [(t1 + 0.2, "0"), (t1 + 0.9, ".9")]) + "</path>")
    out.append("</g></g>")

    # embers drifting up off the letters
    for _ in range(30):
        x = TX + rng.uniform(0, name_w)
        b = max(front_time(x) + 0.1, rng.uniform(front_time(x) + 0.1, 6.2))
        life = rng.uniform(0.9, 1.6)
        s = rng.choice([4, 4, 6])
        col = rng.choice(["#ffbe0b", "#fb5607", "#ff006e", "#ffd166"])
        y = TY + rng.uniform(0, 7 * TS)
        out.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{s}" height="{s}" fill="{col}" opacity="0">'
                   + anim("opacity", [(b, "0"), (b + 0.1, "1"), (b + life, "0")])
                   + anim("transform", [(b, "0 0"), (b + life, f"{rng.uniform(-14, 14):.0f} {-rng.uniform(40, 80):.0f}"),
                                        (T, "0 0")], tag="animateTransform", extra='type="translate"')
                   + "</rect>")

    # fireball: travels left -> right, two-frame flicker, grows as it flies
    y_mid = MOUTH[1] - FIRE_H / 2
    out.append(f'<g opacity="0">'
               + anim("opacity", [(T_LAUNCH - 0.01, "0"), (T_LAUNCH, "1"), (T_EXIT, "1"), (T_EXIT + 0.01, "0")])
               + anim("transform", [(T_LAUNCH, f"{FIRE_START - FIRE_W} {y_mid}"), (T_EXIT, f"{FIRE_END - FIRE_W} {y_mid}")],
                      tag="animateTransform", extra='type="translate"'))
    out.append(f'<g>{anim("transform", [(T_LAUNCH, ".45"), (T_LAUNCH + 0.35, "1.15"), (T_EXIT, "1.3")], tag="animateTransform", extra=f"type=\"scale\"")}')
    out.append(f'<ellipse cx="{FIRE_W * .62}" cy="{FIRE_H / 2}" rx="{FIRE_W * .6}" ry="{FIRE_H * .9}" fill="#fb5607" opacity=".45" filter="url(#soft)"/>')
    for frame, vals in ((FIRE_A, "1;0"), (FIRE_B, "0;1")):
        out.append(f'<g>{grid_paths(frame, FIRE_PAL, 0, 0, FS)}'
                   f'<animate attributeName="opacity" values="{vals}" dur="0.18s" calcMode="discrete" repeatCount="indefinite"/></g>')
    out.append("</g></g>")

    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    OUT.write_text(build(), encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size / 1024:.0f} KB)")
