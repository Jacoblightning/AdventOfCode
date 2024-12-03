#!/usr/bin/env bash

# Year is passed as first arg

# Make year dir
mkdir "$1"

# Make day dirs and copy base script
for i in {1..31}; do mkdir "$1/day$i"; cp base.py "$1/day$i/solver.py"; done

