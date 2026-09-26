# repo-readme-architect

[![tests](https://github.com/raoulmunet/repo-readme-architect/actions/workflows/tests.yml/badge.svg)](https://github.com/raoulmunet/repo-readme-architect/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/Python-3.10--3.13-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Generate a useful README starter by inspecting a local software repository.

> **Oracle compatibility:** Not applicable. This tool is repository- and database-agnostic.

## What it detects

- Python projects (`pyproject.toml`, `requirements.txt`)
- Node projects (`package.json`)
- Docker
- `src/`, `tests/`, `docs/`, `examples/`
- licenses
- GitHub Actions
- likely install/test commands

The generated README is deliberately a **starter**, not invented marketing copy. Unknown sections are emitted as TODOs.

## Usage

```bash
python -m pip install "git+https://github.com/raoulmunet/repo-readme-architect.git"
repo-readme-architect .
repo-readme-architect /path/to/project --output README.generated.md
```

## Why this is useful

A repository often has enough structural information to bootstrap accurate setup documentation, but not enough to infer its purpose. This tool automates what can be known and clearly marks what still needs a human description.

## Related portfolio tools

- [Oracle Dev Tools](https://github.com/raoulmunet?tab=repositories&q=ora-&type=source) — the Oracle-focused tool suite.
- [repo-readme-architect](https://github.com/raoulmunet/repo-readme-architect) — bootstrap repository documentation from project structure.
- [github-portfolio-generator](https://github.com/raoulmunet/github-portfolio-generator) — build a factual Markdown portfolio from GitHub metadata.

## License

MIT.
