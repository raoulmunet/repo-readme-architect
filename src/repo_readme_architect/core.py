from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import json

@dataclass(frozen=True)
class RepoFacts:
    name: str
    technologies: list[str]
    has_tests: bool
    has_docs: bool
    has_examples: bool
    has_actions: bool
    install_commands: list[str]
    test_commands: list[str]

def inspect_repo(path: str | Path) -> RepoFacts:
    p = Path(path)
    tech, install, tests = [], [], []
    if (p / 'pyproject.toml').exists():
        tech.append('Python'); install.append('python -m pip install -e "."'); tests.append('pytest')
    elif (p / 'requirements.txt').exists():
        tech.append('Python'); install.append('python -m pip install -r requirements.txt'); tests.append('pytest')
    if (p / 'package.json').exists():
        tech.append('Node.js'); install.append('npm install')
        try:
            pkg = json.loads((p / 'package.json').read_text(encoding='utf-8'))
            if 'test' in pkg.get('scripts', {}): tests.append('npm test')
        except Exception:
            pass
    if (p / 'Dockerfile').exists(): tech.append('Docker')
    if (p / '.github/workflows').exists(): tech.append('GitHub Actions')
    return RepoFacts(p.resolve().name, tech, (p/'tests').exists() or (p/'test').exists(), (p/'docs').exists(), (p/'examples').exists(), (p/'.github/workflows').exists(), install, tests)

def render_readme(f: RepoFacts) -> str:
    tech = '\n'.join('- ' + x for x in f.technologies) or '- TODO: identify technologies'
    install = '\n\n'.join('```bash\n' + x + '\n```' for x in f.install_commands) or 'TODO: add installation steps.'
    testing = '\n\n'.join('```bash\n' + x + '\n```' for x in f.test_commands) or 'TODO: add test instructions.'
    structure = []
    if f.has_tests: structure.append('- `tests/` — automated tests')
    if f.has_docs: structure.append('- `docs/` — project documentation')
    if f.has_examples: structure.append('- `examples/` — runnable examples')
    if f.has_actions: structure.append('- `.github/workflows/` — CI workflows')
    return '# ' + f.name + '\n\n## Overview\n\nTODO: explain the problem this project solves and who it is for.\n\n## Tech stack\n\n' + tech + '\n\n## Installation\n\n' + install + '\n\n## Usage\n\nTODO: add the smallest working example.\n\n## Project structure\n\n' + ('\n'.join(structure) if structure else 'TODO: describe the important directories.') + '\n\n## Testing\n\n' + testing + '\n\n## Limitations\n\nTODO: document important limitations and unsupported cases.\n\n## License\n\nTODO: state the project license.\n'
