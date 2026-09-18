import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"
ERROR = "[data-test='error']"


def login(page: Page, username: str, password: str):
    """Open the login page and try to log in with the given credentials."""
    page.goto(BASE_URL)

    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()


@pytest.mark.negative
@pytest.mark.regression
def test_login_with_empty_credentials(page: Page):
    login(page, "", "")

    expect(page.locator(ERROR)).to_have_text("Epic sadface: Username is required")
    expect(page).to_have_url(BASE_URL)  # Still on the login page


@pytest.mark.negative
@pytest.mark.regression
def test_login_with_empty_password(page: Page):
    login(page, "standard_user", "")

    expect(page.locator(ERROR)).to_have_text("Epic sadface: Password is required")
    expect(page).to_have_url(BASE_URL)


@pytest.mark.negative
@pytest.mark.regression
def test_login_with_empty_username(page: Page):
    login(page, "", "secret_sauce")

    expect(page.locator(ERROR)).to_have_text("Epic sadface: Username is required")
    expect(page).to_have_url(BASE_URL)


@pytest.mark.negative
@pytest.mark.regression
def test_login_with_wrong_password(page: Page):
    login(page, "standard_user", "wrong_password")

    expect(page.locator(ERROR)).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )
    expect(page).to_have_url(BASE_URL)


@pytest.mark.negative
@pytest.mark.regression
def test_login_with_unknown_username(page: Page):
    login(page, "no_such_user", "secret_sauce")

    expect(page.locator(ERROR)).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )
    expect(page).to_have_url(BASE_URL)


@pytest.mark.negative
@pytest.mark.regression
def test_login_is_case_sensitive(page: Page):
    login(page, "Standard_User", "secret_sauce")

    expect(page.locator(ERROR)).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )
    expect(page).to_have_url(BASE_URL)


@pytest.mark.negative
@pytest.mark.regression
def test_login_with_locked_out_user(page: Page):
    login(page, "locked_out_user", "secret_sauce")

    expect(page.locator(ERROR)).to_have_text(
        "Epic sadface: Sorry, this user has been locked out."
    )
    expect(page).to_have_url(BASE_URL)


@pytest.mark.negative
@pytest.mark.regression
def test_login_with_sql_injection(page: Page):
    login(page, "' OR 1=1 --", "' OR 1=1 --")

    expect(page.locator(ERROR)).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )
    expect(page).to_have_url(BASE_URL)


@pytest.mark.negative
@pytest.mark.regression
def test_login_with_whitespace_credentials(page: Page):
    login(page, "   ", "   ")

    expect(page.locator(ERROR)).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )
    expect(page).to_have_url(BASE_URL)


@pytest.mark.negative
@pytest.mark.regression
def test_password_field_is_masked(page: Page):
    page.goto(BASE_URL)

    password = page.locator("#password")
    password.fill("secret_sauce")

    expect(password).to_have_attribute("type", "password")


@pytest.mark.negative
@pytest.mark.regression
def test_error_message_can_be_dismissed(page: Page):
    login(page, "standard_user", "wrong_password")

    expect(page.locator(ERROR)).to_be_visible()

    page.locator("button.error-button").click()  # The "X" button on the error banner

    expect(page.locator(ERROR)).not_to_be_visible()


@pytest.mark.negative
@pytest.mark.regression
def test_inventory_page_is_not_reachable_without_login(page: Page):
    page.goto("https://www.saucedemo.com/inventory.html")

    expect(page.locator(ERROR)).to_have_text(
        "Epic sadface: You can only access '/inventory.html' when you are logged in."
    )
    expect(page).to_have_url(BASE_URL)
