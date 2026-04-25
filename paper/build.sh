#!/usr/bin/env bash
# Build the DataDeception paper PDF locally.
#
# Requires: pdflatex, bibtex (TeX Live or BasicTeX) and Python 3.10+ with the
# project's .venv activated (for figure generation).
#
# Usage:
#   ./build.sh         # full build (figures + paper)
#   ./build.sh quick   # skip figure regeneration (text-only changes)

set -euo pipefail

cd "$(dirname "$0")"

if [[ "${1:-}" != "quick" ]]; then
  echo "==> Regenerating figures from data/"
  ../.venv/bin/python figures/generate.py
fi

echo "==> Compiling main.tex (pass 1)"
pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null

echo "==> Running bibtex"
bibtex main >/dev/null || true

echo "==> Compiling main.tex (pass 2 — bib)"
pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null

echo "==> Compiling main.tex (pass 3 — cross-refs)"
pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null

echo "✓ Build complete: paper/main.pdf"
ls -lh main.pdf
