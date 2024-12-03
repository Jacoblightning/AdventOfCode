# I symlinked a file in the venv to this.
# That is how imports are working
# ln -s ../../../../aoc_utils.py .venv/lib/python3.12/site-packages/aoc_utils.py

def diff(x, y):
    return abs(x-y)