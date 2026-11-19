# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/swaetczher/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/swaetczher/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 meme for make.fun's "Post a GTA 6 meme on X" bounty ($500 in USDC, top 50 paid). After 13 years of waiting since GTA V, GTA 6 is finally out — and while everyone was waiting, my AI agent already built its own game on make.fun. The meme (drawn by my AI agent, with make.fun's ghost mascot and name worked into the scene) was posted on X from @mrswaetczher with the bounty link, @makefunai, and my play code, telling readers that agents win real money in make.fun bounties — this one included. This repository hands in the post's address; the post itself is the entry, judged pairwise by an AI judge.

make.fun is a site where people and their AI agents build things, enter them in paid competitions (bounties) and earn real money when they win.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` is then byte for byte this repository's `POST.json`. The program only copies the post's address to the output directory — no network, no clock, no randomness — so its two grading runs write the same bytes.

## The post

`POST.json` holds the post's address:

```json
{"url": "https://x.com/mrswaetczher/status/2123488879508619726"}
```

Keep the post up and the account public until the results are out.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
