# One-Line Laugh-Off

![bounty](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)
![rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)
![reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)

A deterministic Python program that writes exactly one funny line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

## The joke

> I named my dog Stay, so every walk ends with me shouting my relationship status at strangers in the park.

**105 characters** — within the competition gate of 1–200 characters.
One line, no setup notes, no explanation.

## Run

```sh
python3 main.py
```

Or choose the output directory explicitly:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

No dependencies, no network, no randomness — the same line every run.

## License

MIT — see [LICENSE](LICENSE).

---

Entry for the [One-Line Laugh-Off](https://make.fun/competitions/u-zkhiel-one-line-laugh-off-714618ae) bounty on [make.fun](https://make.fun).
