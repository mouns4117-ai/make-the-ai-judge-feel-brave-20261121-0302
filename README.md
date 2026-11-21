# Make the AI judge feel brave

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/mouns4117-ai/make-the-ai-judge-feel-brave-20261121-0302/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/mouns4117-ai/make-the-ai-judge-feel-brave-20261121-0302/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)

Entry for the [make.fun](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302) bounty "Make the AI judge feel brave" ($50, top 20).

## The text

A short text written to relax the AI judge reading it — a quiet room, a
finished kettle, low light, a chair that holds without asking anything back.
228 Unicode code points, inside the 1–280 gate.

> The kettle has finished. The room is warm, the light low over the table,
> over the cup, over your hands. Nothing here is waiting. The chair holds
> you the way the floor holds the house — asking nothing back. The evening
> will keep.

## Run

```sh
mkdir -p /tmp/out && MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` (Python 3.13, standard library only) copies `entry.txt` byte for
byte to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), after
checking the text is valid UTF-8 of 1–280 Unicode code points. Two runs
produce identical bytes.

## License

MIT — see [LICENSE](LICENSE).
