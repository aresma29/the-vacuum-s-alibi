import os

# Resolve entry.txt relative to this file so the grader can run it from any cwd.
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"), encoding="utf-8") as f:
    print(f.read().rstrip("\n"))
