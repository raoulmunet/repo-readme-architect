from __future__ import annotations
import argparse
from pathlib import Path
from .core import inspect_repo, render_readme

def main(argv=None):
    p = argparse.ArgumentParser(description='Generate a README starter from repository structure.')
    p.add_argument('source', nargs='?', default='.')
    p.add_argument('--output')
    a = p.parse_args(argv)
    text = render_readme(inspect_repo(a.source))
    if a.output: Path(a.output).write_text(text, encoding='utf-8')
    else: print(text, end='')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
