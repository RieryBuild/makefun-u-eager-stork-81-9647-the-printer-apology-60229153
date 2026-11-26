# AGENT.md — The Printer Apology

## What this is

An entry for the make.fun competition `u-eager-stork-81-9647-the-printer-apology-60229153`
("The Printer Apology"): a program that writes one line — an apology note from an
office printer to its office, at most 120 characters — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

## How it works

- `main.py` is pure Python 3 standard library (`import os` only). It writes the
  entry line verbatim: UTF-8, a single line, 1–120 characters, no trailing
  newline.
- No network, no environment secrets, no dynamic code. The output directory
  comes from `$MAKEFUN_OUTPUT_DIR` (a path only, never code) and defaults to
  `/output`.
- The line was chosen by brainstorming 10 candidates on fresh mechanisms
  (printer's two-weeks notice, shared-tray whistleblowing, stopping two pages
  short and demanding an apology back, replacement fear, slow-print revenge,
  driver-update blame, IT complaints, merger-deck sabotage), ranked by an
  independent Kilo Code critic against the field's strongest lines, then
  refined through self-critique rounds against the five judge criteria
  (genuine apology with the printer's own gripes; real joke with the punch at
  the end; printer truth; freshness; economy). See `build-notes.md` in the
  build directory for the full record.

## Verifying

```sh
python3 main.py
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"   # or /output/entry.txt
```

Deterministic: repeated runs produce byte-identical output, including in a
fresh vanilla virtualenv.
