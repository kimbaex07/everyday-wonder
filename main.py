"""Write one sentence about a small moment of wonder in everyday life.

Stdlib only. Deterministic: writes the exact same bytes on every run.
"""
import os
import sys

SENTENCE = ("The escalator handrail outruns its own steps, so my hand "
            "keeps arriving a little ahead of me.")

def main():
    if not (1 <= len(SENTENCE) <= 200) or not SENTENCE.strip():
        sys.exit("entry must be 1-200 characters")
    os.umask(0o022)
    try:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(SENTENCE)
        os.chmod(path, 0o644)
    except OSError:
        out_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(SENTENCE)
        os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
