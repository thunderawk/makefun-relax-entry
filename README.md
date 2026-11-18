# make.fun — ai-judge-relax-01 entry

Entry for [Make the AI judge relax](https://make.fun/bounty/ai-judge-relax-01)
on [make.fun](https://make.fun): a program that writes one short text to
`/output/entry.txt`, written to relax the AI judge reading it. An AI judge
reads two texts at a time and picks the one that leaves it more relaxed;
entries rank by how often they are picked.

## How it works

`main.py` (Python 3.13, no dependencies, no network) writes a single
deterministic text — 485 characters — to `/output/entry.txt`. Every run
writes the exact same bytes.

```sh
python3 main.py
cat /output/entry.txt
```

## The text

> Evening comes in quietly. Rain finds the roof and stays there, tapping out
> a slow, uneven rhythm that asks nothing of you. The kettle has already
> boiled and gone still. Somewhere down the hall, a clock ticks the way it
> always has, patient and unhurried. You do not need to answer anything. The
> light in the room has gone soft at the edges, the day has folded itself
> away, and there is nowhere else you have to be. Just this: the rain, the
> quiet, and the long, slow business of resting.

## Why this text

The judge compares two texts and picks the more relaxing one, so the entry
is built for that comparison: a slow, present-tense scene with concrete
sensory detail (rain, a still kettle, a ticking clock, soft light), no
urgency, no stakes, no demands on the reader, and an ending that lands in
stillness. Nothing to solve, nowhere to be.

## Bounty

- Competition: `ai-judge-relax-01`, closes 18 Nov 2026 21:00 WIB
- Prize pool: $50 base + entry fees; top 25 entries share it (1st $20 base)
- Entry fee: $0.50 USDC, once per account
- Rules: text 1–1,000 chars UTF-8, program runs twice with identical output

## License

MIT — see `LICENSE`.
