# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/framicks/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/framicks/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A newspaper front page that sums up Friday 20 November 2026 in one image: six of the day's biggest stories, from Washington to Seoul, each with a headline and a one-line summary. `main.py` checks the image and copies it to the output directory.

![The world in one day — 20 November 2026](entry.png)

## The six stories

1. **Trump delays Iran decision** — The US president says he is in no rush on new strikes and will decide after the new year. *(Reuters)*
2. **Pete Rose pardoned** — Trump grants a posthumous pardon to baseball's all-time hits leader, who finished with 4,256 hits. *(Reuters)*
3. **Cyclone Akvan nears India** — About 300,000 people are evacuated from the Odisha coast as the storm closes in. *(The Hindu)*
4. **GTA VI tops $1.84 billion** — Estimated launch-day sales pass the entire box-office total of *The Odyssey*. *(Sensor Tower via Reuters)*
5. **Europe ready for Russia talks** — European leaders say they are prepared to negotiate with Moscow on ending the war in Ukraine. *(BBC)*
6. **Korea's exports pass $1 trillion** — South Korea reaches the milestone for the first time, powered by demand for AI chips. *(Ministry of Trade, Industry and Resources / AJU Press)*

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` validates `entry.png` (PNG signature, at most 1024x1024, IEND trailer, and the CRC of every chunk) and copies it unchanged; the file is 846,938 bytes.

<sub>Entered on [make.fun](https://make.fun/?ref=jjs4n5n8&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
