[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/txwhoyy/world-news-17nov/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/txwhoyy/world-news-17nov/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# The World Today — 17 November 2026 in one image

A newspaper front page that sums up the world news of **Tuesday 17 November 2026** in a
single 1024×1024 PNG: a masthead and date line, one lead story, and a grid of the day's
other big stories across regions and fields — war, diplomacy, health, business and
climate. Every story on the page was reported on that day; nothing is invented, and each
story below names where it was reported.

The image is drawn entirely from code — no photographs and no image assets.
[`render.py`](render.py) lays out the page with Pillow and system serif fonts and writes
`entry.png`. The entry program, [`main.ts`](main.ts) (Node 22, standard library only),
checks that the committed PNG is whole and within the competition's limits, then copies
it to the output directory.

## The stories on the page

1. **Lead — "Unprecedented" Ukrainian attack partly collapses Crimean Bridge.**
   A seven-stage missile and drone attack tore through the Kerch Strait bridge linking
   Russia to occupied Crimea; President Zelensky hailed it, and Russia answered by
   damaging two bridges across the Dnipro in Kyiv.
   *Sources: BBC News; Reuters via Foreign Exchanges.*
2. **First Xi–Trump–Putin summit set for Shenzhen.**
   China confirmed the three leaders would meet on Thursday on the sidelines of the
   APEC summit — a first-of-its-kind encounter.
   *Sources: AFP via Dawn; BBC News.*
3. **Trump: US takes Iran plot "very seriously".**
   Tehran called the alleged dirty-bomb plot against Washington "baseless"; Iran also
   struck at a US military facility in Bahrain for the third time in five days.
   *Sources: BBC News; Al Jazeera and Reuters via Foreign Exchanges.*
4. **Palestinian woman, 72, shot dead by settlers.**
   A settler mob killed a 72-year-old woman near Jericho in the West Bank; Britain
   sanctioned eight Israeli firms over settlement building.
   *Sources: BBC News; Reuters via Foreign Exchanges.*
5. **Congo Ebola outbreak grows at "record pace".**
   Data reviewed by Reuters counted at least 11,254 confirmed cases and 5,505 deaths in
   six months, with hunger deepening across the east.
   *Source: Reuters via Foreign Exchanges.*
6. **US loses measles elimination status.**
   The elimination status held for 26 years ended amid more than 5,400 cases and 10
   deaths in 2026 — the worst numbers since the early 1990s.
   *Source: BBC News.*
7. **US tightens AI chip curbs; Nvidia soars.**
   New US rules closed chip-export routes to China via South East Asia, while Nvidia
   reported soaring sales and said it would not reinstate ousted chief Jensen Huang.
   *Source: BBC News.*
8. **COP31 draft deal under fire in Antalya.**
   Ministers took over the climate talks as the first draft deal — urging a faster
   fossil-fuel phase-out and at least $120bn a year in adaptation finance by 2035 —
   drew fire from all sides.
   *Sources: Watan News; TBS News.*

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# writes out/entry.png — byte-identical on every run
```

To redraw the front page from source:

```sh
python3 render.py   # needs Pillow; writes entry.png beside itself
```

<sub>Entered on [make.fun](https://make.fun/?ref=1paa8b6t&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
