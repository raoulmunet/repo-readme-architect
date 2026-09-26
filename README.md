# repo-readme-architect

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

## License

MIT.
