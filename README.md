# Automation

Course repo for the automation class (`pp-automation-class`).  
Stack: **Python**, **uv**, **Playwright**.

## Setup

```bash
git clone https://github.com/pp-automation-class/automation.git
cd automation
```

### Install uv (macOS)

```bash
# Homebrew
brew install uv

# or curl
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Install Python (via uv)

```bash
uv python install 3.12
uv python pin 3.12
```

### Project env + Playwright

```bash
uv init --name automation   # skip if pyproject.toml already exists
uv add playwright pytest pytest-playwright
uv run playwright install
# browsers + OS deps (macOS usually just needs the browsers line above)
uv run playwright install-deps   # Linux CI; optional on macOS
```

Verify:

```bash
uv run python -c "import playwright; print(playwright.__version__)"
uv run playwright --version
```

## Structure

```
automation/
├── README.md
├── .gitignore
├── pyproject.toml      # after uv init / uv add
└── …                   # labs / scripts
```

## Usage

```bash
uv run pytest
# or a single script
uv run python path/to/script.py
```

Document each exercise in its own folder with a short note on how to run it.

## Contributing

1. Create a branch: `git checkout -b <your-name>/<topic>`
2. Commit with a clear message
3. Open a PR against `main`

## License

Unlicensed / course material — check with the instructor before redistributing.
