from pathlib import Path
from repo_readme_architect import inspect_repo, render_readme

def test_python_repo(tmp_path: Path):
    (tmp_path / 'pyproject.toml').write_text("[project]\nname='x'\n", encoding='utf-8')
    (tmp_path / 'tests').mkdir()
    f = inspect_repo(tmp_path)
    assert 'Python' in f.technologies
    assert f.has_tests
    assert '## Installation' in render_readme(f)
