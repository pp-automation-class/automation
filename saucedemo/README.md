# saucedemo

A small test framework for the live site [saucedemo.com](https://www.saucedemo.com/).
It is meant for learning. The design follows KISS: few files, no extra layers.

A page class knows how to open a screen and find its elements.
A test calls those methods and checks what the user should see.

## Layout

```
.env                           login/password pairs (copy from .env.example)
.env.example                   placeholders only — no real accounts
config.py                      site URL and the example product name
conftest.py                    shared setup for every test
Data/                          accounts the tests read
  users.py                     get_user() and get_password()
helper/                        shared helpers, no browser
  letters.py                   Faker _letters() for name fields
pages/                         Page Object Model — locators and clicks
  base_page.py                 open a URL, cart icon, side menu
  login_page.py
  inventory_page.py            product list
  cart_page.py
  checkout_info_page.py        step 1: your details
  checkout_overview_page.py    step 2: order summary
  checkout_complete_page.py    step 3: thank you
tests/                         checks only — no locators in here
reports/index.html             Allure report, written after each run
logs/tests.log                 log of the last run (git-ignored)
```

`conftest.py` is not a test. Pytest loads it by itself. Do not run it:

```bash
uv run pytest conftest.py          # collects 0 tests
```

A test asks for a fixture by name. `login` opens the login screen. `inventory` signs in as the standard user and stops on the products page.

## Setup

```bash
uv sync
uv run playwright install chromium
cp .env.example .env               # only if .env is missing
```

`.env.example` has `login/password` placeholders. Put the real accounts in `.env`. Each line is one pair:

```
STANDARD_USER=login/password
```

A test reads them with `get_user("standard")` and `get_password("standard")`.

Check that the Allure command is available:

```bash
allure --version
```

## Run

```bash
uv run pytest                              # all tests, headless Chromium
uv run pytest -m smoke                     # login, cart, and one purchase
uv run pytest --headed                     # watch the browser
uv run pytest --headed --slowmo 500        # watch, half a second between actions
uv run pytest tests/test_login.py          # one file
uv run pytest tests/test_login.py::test_login_form_is_visible
```

`--slowmo` and `500` are two arguments. `--slowmo500` is not a flag.

Tests call the real website, so they need network access.
Name fields are typed one letter at a time. The letters come from Faker.

## Logs

Every run writes `logs/tests.log`. pytest makes the folder and replaces the file each run.
The page classes write what they do, for example `Open /cart.html`.

```bash
uv run pytest                              # INFO: the steps (default)
uv run pytest --log-file-level=DEBUG       # DEBUG: steps plus details (URLs, names typed)
```

Passwords are never logged. In your own page, add:

```python
import logging

log = logging.getLogger(__name__)
log.info("Something the user did")
log.debug("Extra detail for finding a bug")
```

## Report

Every `uv run pytest` does two things:

1. Writes raw results to `allure-results/`.
2. Saves one HTML file at `reports/index.html`. This step needs the `allure` command.
   Without it, pytest prints a warning and skips the report.

Open `reports/index.html` in a browser. Both folders are git-ignored.

These folders, and `logs/` and `test-results/`, are always made in the project folder,
even when you start pytest from somewhere else.

Other Allure commands:

```bash
allure serve allure-results                # build a temporary report and open it
allure serve allure-results -p 8080        # same, on port 8080
allure generate allure-results --single-file --clean -o reports
allure --version
allure --help
```

`allure serve` keeps running until you stop it with Ctrl+C.

`allure open` needs the report folder, not the file:

```bash
allure open allure-report                  # folder
allure open allure-report/index.html       # fails: that path is a file
```

The HTML file this project keeps is `reports/index.html`. Open that in a browser. `allure open` is for a full report folder, not for the single file.
