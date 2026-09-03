# Automation

Practice repo for browser automation with [Playwright](https://playwright.dev/python/) and pytest. It includes a local login page you can drive from tests.

## Login page

Open `index.html` in a browser (or serve it locally). Valid credentials:

| Field    | Value                 |
| -------- | --------------------- |
| Email    | `student@example.com` |
| Password | `Playwright1!`        |

Successful login shows **Login successful.** Invalid credentials show **Invalid email or password.**

## Setup

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

On Windows (PowerShell), install uv with:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Run

```bash
uv run pytest
uv run python path/to/script.py
```
