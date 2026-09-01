```bash
git clone https://github.com/pp-automation-class/automation.git
cd automation

brew install uv   # or: curl -LsSf https://astral.sh/uv/install.sh | sh

uv python install 3.12
uv python pin 3.12

uv init --name automation   # skip if pyproject.toml exists
uv add playwright pytest pytest-playwright
uv run playwright install
```

```bash
uv run pytest
uv run python path/to/script.py
```
