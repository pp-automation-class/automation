"""
Shared setup for every test.

Students: this file sits next to the project, not inside tests/.
pytest still loads it. A test does not call these functions. It asks
for a fixture by name, for example `def test_shop(inventory)`.
pytest runs the fixture first and passes the result in.

What this file gives the tests:
- a desktop browser window
- a longer timeout, because the live site can be slow
- `login`: the login screen, before anyone signs in
- `inventory`: the product list, already signed in as the standard user
- a screenshot in test-results/ and in the Allure report when a test fails
- an HTML report at reports/index.html after the run
- a log of the steps at logs/tests.log, with each test's name and result
"""

import logging
import shutil
import subprocess
from pathlib import Path

import allure
import pytest
from playwright.sync_api import Page, expect

from Data.users import get_password, get_user
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

# The project folder. Output folders go here, wherever pytest is started.
ROOT = Path(__file__).resolve().parent

log = logging.getLogger("tests")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config: pytest.Config) -> None:
    """
    Turn the output paths from pyproject.toml into full paths.

    Allure and the log file read relative paths from the folder where
    pytest started. Anchor them to the project folder instead.
    tryfirst: this must run before Allure and logging read the paths.
    """
    alluredir = config.option.allure_report_dir
    if alluredir:
        config.option.allure_report_dir = str(ROOT / alluredir)
    log_file = config.getoption("log_file") or config.getini("log_file")
    if log_file:
        config.option.log_file = str(ROOT / log_file)


# Other libraries log a lot at DEBUG. Keep logs/tests.log about our steps.
for _noisy in ("faker", "asyncio"):
    logging.getLogger(_noisy).setLevel(logging.WARNING)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Desktop window. The shop layout changes on a small screen."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }


@pytest.fixture(autouse=True)
def _set_timeouts(page: Page) -> None:
    """Give each click and each page load a little more time."""
    page.set_default_timeout(15_000)
    page.set_default_navigation_timeout(15_000)


@pytest.fixture
def login(page: Page) -> LoginPage:
    """Open the login screen. The test is not logged in yet."""
    screen = LoginPage(page)
    screen.open()
    return screen


@pytest.fixture
def inventory(login: LoginPage) -> InventoryPage:
    """Log in as the standard user and stop on the products page."""
    login.login(get_user("standard"), get_password("standard"))
    products = InventoryPage(login.page)
    # Stop here with a clear message if the login did not work.
    expect(products.title).to_have_text("Products")
    return products


def pytest_runtest_logstart(nodeid: str) -> None:
    """Write the test name to the log before the test's steps."""
    log.info("START %s", nodeid)


def pytest_runtest_logreport(report: pytest.TestReport) -> None:
    """
    Write the result after the test.

    pytest reports setup, call and teardown separately. Log the call,
    and setup or teardown only when they did not pass.
    """
    if report.when == "call" or report.outcome != "passed":
        log.info("%s %s (%s)", report.outcome.upper(), report.nodeid, report.when)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item):
    """
    After a test fails, save a picture of the browser.

    pytest calls this hook. Tests do not. The picture is written to
    test-results/ and attached to the Allure report. Both are git-ignored.
    """
    outcome = yield
    report = outcome.get_result()
    if not report.failed or report.when not in ("setup", "call"):
        return

    page = item.funcargs.get("page")
    if not isinstance(page, Page):
        return

    folder = ROOT / "test-results"
    folder.mkdir(exist_ok=True)
    # nodeid looks like tests/test_login.py::test_name[chromium]
    safe_name = report.nodeid.replace("/", "_").replace("::", "__")
    try:
        png = page.screenshot(full_page=True)
    except Exception:
        # The browser may already be closed. The test failure still stands.
        return
    (folder / f"{safe_name}.png").write_bytes(png)
    allure.attach(png, name="screenshot", attachment_type=allure.attachment_type.PNG)


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    """
    Save the Allure report as one HTML file: reports/index.html.

    pytest calls this after the tests. Open that file in a browser.
    allure-results/ stays as the raw data this file is built from.
    """
    if getattr(session.config.option, "collectonly", False):
        return
    allure_bin = shutil.which("allure")
    if allure_bin is None:
        terminal = session.config.pluginmanager.get_plugin("terminalreporter")
        if terminal is not None:
            terminal.write_line(
                "No allure command found, so reports/index.html was not made.",
                yellow=True,
            )
        return
    subprocess.run(
        [
            allure_bin,
            "generate",
            str(ROOT / "allure-results"),
            "--single-file",
            "--clean",
            "-o",
            str(ROOT / "reports"),
        ],
        check=False,
    )
