#!/usr/bin/env python3
"""Render entry.png: a newspaper front page summing up the world news of
Tuesday 17 November 2026. All stories were reported that day; sources are
listed in README.md. Drawn entirely with Pillow + system fonts (no assets).

Run:  python3 render.py   ->  writes entry.png (1024x1024) beside this file.
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W = H = 1024
MARGIN = 44
CW = W - 2 * MARGIN  # content width = 936

PAPER = (247, 243, 233)
INK = (20, 18, 14)
ACCENT = (138, 30, 30)
FAINT = (110, 102, 88)
COLRULE = (198, 190, 170)

FONT_DIR = "/usr/share/fonts/truetype/noto"
DISPLAY_BLACK = f"{FONT_DIR}/NotoSerifDisplay-Black.ttf"
SERIF_BOLD = f"{FONT_DIR}/NotoSerif-Bold.ttf"
SERIF = f"{FONT_DIR}/NotoSerif-Regular.ttf"
SANS_BOLD = f"{FONT_DIR}/NotoSans-Bold.ttf"
SANS_SEMI = f"{FONT_DIR}/NotoSans-SemiBold.ttf"
SANS = f"{FONT_DIR}/NotoSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(draw, s, f):
    return draw.textlength(s, font=f)


def wrap(draw, s, f, max_w):
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        t = f"{cur} {w_}".strip()
        if text_w(draw, t, f) <= max_w or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def tracked(draw, xy, s, f, fill, tracking=3):
    x, y = xy
    for ch in s:
        draw.text((x, y), ch, font=f, fill=fill)
        x += text_w(draw, ch, f) + tracking
    return x


def tracked_center(draw, y, s, f, fill, tracking=3):
    total = sum(text_w(draw, ch, f) for ch in s) + tracking * (len(s) - 1)
    tracked(draw, ((W - total) / 2, y), s, f, fill, tracking)


def block(draw, x, y, s, f, fill, max_w, leading):
    for line in wrap(draw, s, f, max_w):
        draw.text((x, y), line, font=f, fill=fill)
        y += leading
    return y


def story(draw, x, y, w, kicker, headline, summary, h_size=25, s_size=20):
    tracked(draw, (x, y), kicker.upper(), font(SANS_BOLD, 18), ACCENT, 2)
    y += 27
    y = block(draw, x, y, headline, font(SERIF_BOLD, h_size), INK, w, int(h_size * 1.16))
    y += 3
    y = block(draw, x, y, summary, font(SERIF, s_size), INK, w, int(s_size * 1.3))
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ------------------------------------------------------
    d.line([MARGIN, 24, W - MARGIN, 24], fill=INK, width=5)
    d.line([MARGIN, 33, W - MARGIN, 33], fill=INK, width=2)
    name_f = font(DISPLAY_BLACK, 88)
    name = "The World Today"
    d.text(((W - text_w(d, name, name_f)) / 2, 38), name, font=name_f, fill=INK)
    tracked_center(d, 138, "ONE PAGE · ALL THE NEWS THAT MATTERED", font(SANS_SEMI, 20), FAINT, 3)

    # ---- Date bar ------------------------------------------------------
    bar_y = 166
    d.rectangle([MARGIN, bar_y, W - MARGIN, bar_y + 54], fill=INK)
    tracked_center(d, bar_y + 8, "TUESDAY 17 NOVEMBER 2026", font(SANS_BOLD, 37), PAPER, 4)
    d.line([MARGIN, bar_y + 64, W - MARGIN, bar_y + 64], fill=INK, width=2)

    # ---- Lead story ----------------------------------------------------
    y = bar_y + 80
    tracked(d, (MARGIN, y), "LEAD STORY · UKRAINE WAR", font(SANS_BOLD, 21), ACCENT, 2)
    y += 32
    y = block(d, MARGIN, y,
              "\u201cUnprecedented\u201d Ukrainian attack partly collapses Crimean Bridge",
              font(SERIF_BOLD, 50), INK, CW, 58)
    y += 12

    sub_y = y
    sf_end = block(d, MARGIN, sub_y,
                   "A seven-stage missile and drone attack tore through the Kerch Strait "
                   "bridge linking Russia to occupied Crimea. Russia answered by damaging "
                   "two bridges across the Dnipro in Kyiv.",
                   font(SERIF, 26), INK, 560, 34)
    sx = MARGIN + 592
    ap_end = story(d, sx, sub_y, W - MARGIN - sx, "Diplomacy · APEC",
                   "First Xi\u2013Trump\u2013Putin summit set for Shenzhen",
                   "China confirms the three leaders meet on Thursday, at the APEC summit.")
    d.line([sx - 16, sub_y, sx - 16, max(sf_end, ap_end) - 6], fill=FAINT, width=1)

    # ---- Grid: six stories, three columns x two rows -------------------
    grid_top = max(sf_end, ap_end) + 20
    d.line([MARGIN, grid_top - 12, W - MARGIN, grid_top - 12], fill=INK, width=3)
    col_w = (CW - 2 * 30) // 3
    xs = [MARGIN, MARGIN + col_w + 30, MARGIN + 2 * (col_w + 30)]

    rows = [
        [("Middle East · Iran", "Trump: US takes Iran plot \u201cvery seriously\u201d",
          "Tehran calls the plot claim \u201cbaseless\u201d; Iran again hit a US facility in Bahrain."),
         ("Middle East · West Bank", "Palestinian woman, 72, shot dead by settlers",
          "Gunmen stormed homes overnight; Britain sanctioned eight Israeli settlement firms."),
         ("Africa · Health", "Congo Ebola outbreak grows at \u201crecord pace\u201d",
          "Data reviewed by Reuters: 11,254 cases and 5,505 deaths in six months.")],
        [("United States · Health", "US loses measles elimination status",
          "Elimination status held for 26 years ends amid 5,400 cases and 10 deaths this year."),
         ("Business · Technology", "US tightens AI chip curbs; Nvidia soars",
          "New rules close chip routes to China; ousted chief Huang will not return."),
         ("Climate · COP31", "COP31 draft deal under fire in Antalya",
          "Draft seeks faster fossil-fuel phase-out; $120bn a year for adaptation by 2035.")],
    ]
    row_y = grid_top
    for ri, row in enumerate(rows):
        ends = [story(d, x, row_y, col_w, k, h, s) for x, (k, h, s) in zip(xs, row)]
        row_y = max(ends) + 14
        if ri == 0:
            d.line([MARGIN, row_y - 7, W - MARGIN, row_y - 7], fill=FAINT, width=1)
    grid_end = row_y - 14
    for cx in (xs[1] - 15, xs[2] - 15):
        d.line([cx, grid_top + 2, cx, grid_end], fill=COLRULE, width=1)

    # ---- Footer ---------------------------------------------------------
    fy = H - 38
    d.line([MARGIN, fy - 11, W - MARGIN, fy - 11], fill=INK, width=2)
    foot = "Sources: BBC News · Reuters · AFP · Al Jazeera · Watan News — every story reported on 17 November 2026"
    ff = font(SANS, 19)
    d.text(((W - text_w(d, foot, ff)) / 2, fy), foot, font=ff, fill=FAINT)
    print(f"lead sub-row ends {max(sf_end, ap_end)}, grid ends {grid_end}, footer text at {fy}")

    out = Path(__file__).with_name("entry.png")
    img.save(out, optimize=True)
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
