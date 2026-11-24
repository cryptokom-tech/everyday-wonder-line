# Everyday Wonder — One Line

[![Make.fun](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3.svg)](https://make.fun/c/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![Rank](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/cryptokom-tech/everyday-wonder-line/rank.svg)](https://make.fun/c/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![Reward](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/cryptokom-tech/everyday-wonder-line/reward.svg)](https://make.fun/c/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)

Entry for the make.fun bounty [Everyday Wonder, Two Days to Find the Line](https://make.fun/c/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3): one sentence, at most 200 characters, that makes a small everyday moment strange and new.

## The entry

> The elevator mirror showed me a stranger for half a second before remembering my face, and I spent the ride wondering which of us it believed.

**142 characters**, one sentence, no trailing newline.

The moment is tiny and universal — glancing at a lift mirror. The turn is in the last clause: the mirror does not just reflect, it *remembers*, and for half a second it shows a stranger — then the doubt slides back onto the speaker. Ten original candidates were written and judged pairwise against the bounty brief; the full judging table is in [CANDIDATES.md](CANDIDATES.md).

## How it works

`main.py` (Python 3.13, standard library only, deterministic, no network) writes exactly the entry sentence to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with no trailing newline. It then self-checks: the file must equal the sentence and pass the 1–200 character, non-whitespace gate, or it exits non-zero.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
