# Automation

Practice repo for browser automation with [Playwright](https://playwright.dev/python/) and pytest. It includes a local login page you can drive from tests.

## Login page

Open `index.html` in a browser (or serve it locally). Valid credentials:

| Field    | Value                 |
| -------- | --------------------- |
| Email    | `student@example.com` |
| Password | `Playwright1!`        |

Successful login shows **Login successful.** Invalid credentials show **Invalid email or password.**

## Install C++

Playwright’s Python packages (notably `greenlet`) need a C++ compiler on some platforms. Install one before `uv add playwright`.

### Windows

Install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) and select the **Desktop development with C++** workload.

Or from PowerShell with winget:

```powershell
winget install Microsoft.VisualStudio.2022.BuildTools --force --override "--wait --passive --add Microsoft.VisualStudio.Workload.VCTools --includeRecommended"
```

Restart the terminal after install.

### macOS

```bash
xcode-select --install
```

### Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install build-essential
```

## Setup

```bash
git clone https://github.com/pp-automation-class/automation.git
cd automation

brew install uv   # or: curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows: irm https://astral.sh/uv/install.ps1 | iex

uv sync
uv run playwright install
```

## Run

```bash
uv run pytest
```
