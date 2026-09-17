# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A shared class practice repo (`pp-automation-class/automation`) for learning Python and browser test automation with Playwright + pytest. Several students commit to it, each on their own branch, and they merge into `main`. This branch (`Denis_Python-2.0`) belongs to Denis.

## Commands

The project uses [uv](https://docs.astral.sh/uv/) with Python 3.12 (`.python-version`).

```bash
uv sync                                   # install dependencies
uv run playwright install                 # install browser binaries (one-time)

uv run pytest                             # run all tests (headless Chromium)
uv run pytest tests/test_Denis_by_Claude.py                                   # one file
uv run pytest tests/test_Denis_by_Claude.py::test_login_with_enter_key        # one test
uv run pytest "tests/test_Denis_by_Claude.py::test_valid_users_can_login[problem_user]"  # one parametrized case
uv run pytest -m smoke                    # by marker (smoke | regression, declared in pyproject.toml)
uv run pytest --headed --slowmo 500       # watch the browser (pytest-playwright options)
uv run pytest --browser firefox

uv run python DENIS_class.py              # run a lesson script
```

There's no linter or formatter set up.

On some platforms Playwright's `greenlet` dependency needs a C++ compiler (Xcode CLT on macOS, Build Tools on Windows, `build-essential` on Debian/Ubuntu). See README.md.

## Layout and conventions

- **Root `*.py` files are standalone lesson scripts**, not a package. They cover variables, loops, functions, classes, exceptions and imports. Many use `input()`, so they're interactive. File-name prefixes mark who wrote them (`DENIS_`, `EZ_`, `EK_`, `LM_`, and so on). Unprefixed files usually come from the instructor or `main`. Only edit your own prefixed files unless you're asked to touch others. Some scripts are unfinished on purpose (for example, `DENIS_exceptions.py` has notes that aren't commented out, so it doesn't parse).
- **Root `*_index.html` / `DN_locators.html`** are static practice pages each student made for writing locators against. README.md mentions a login page at `index.html` with `student@example.com` / `Playwright1!`, but that file isn't on this branch.
- **`src/automation/`** is only the `uv init` package stub (`automation` console script). The tests don't use it.
- **`tests/`** has Playwright tests that run against the live site **https://www.saucedemo.com/** (password `secret_sauce`; users include `standard_user`, `locked_out_user`, `problem_user`, `performance_glitch_user`, `error_user`, `visual_user`), so they need network access.
  - Tests use the `page: Page` fixture from `pytest-playwright` and assert with `expect(...)` (auto-waiting). There's no `conftest.py`.
  - `test_Denis_by_Claude.py` has the more structured style: `BASE_URL`/`PASSWORD` constants, a `login_page` fixture, a `login()` helper, `@pytest.mark.parametrize` with `ids`, role/placeholder locators, and `smoke`/`regression` markers. `test_Denis.py` and `test_playwright_basics.py` are earlier, step-by-step exercises that use CSS/XPath locators and `press_sequentially`.
  - `performance_glitch_user` loads slowly, so assertions after its login need a longer timeout (`timeout=15_000`).
- pytest's `testpaths = ["."]` means pytest collects `test_*.py` from the whole repo, not only `tests/`. Don't give lesson scripts a `test_` prefix, because collecting them would run their `input()` calls.
- If you add a new marker, declare it under `[tool.pytest.ini_options].markers` in `pyproject.toml`.
