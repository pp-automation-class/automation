import re

import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"
PASSWORD = "secret_sauce"


@pytest.fixture
def login_page(page: Page) -> Page:
    page.goto(BASE_URL)
    return page


def login(page: Page, username: str, password: str) -> None:
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()


@pytest.mark.smoke
def test_login_page_elements_visible(login_page: Page):
    expect(login_page).to_have_title("Swag Labs")
    expect(login_page.locator(".login_logo")).to_have_text("Swag Labs")
    expect(login_page.get_by_placeholder("Username")).to_be_visible()
    expect(login_page.get_by_placeholder("Password")).to_be_visible()
    expect(login_page.get_by_role("button", name="Login")).to_be_enabled()


@pytest.mark.regression
def test_password_field_is_masked(login_page: Page):
    expect(login_page.get_by_placeholder("Password")).to_have_attribute("type", "password")


@pytest.mark.regression
def test_credentials_hint_is_shown(login_page: Page):
    credentials = login_page.locator("[data-test='login-credentials']")
    expect(credentials).to_contain_text("Accepted usernames are:")
    for user in ["standard_user", "locked_out_user", "problem_user",
                 "performance_glitch_user", "error_user", "visual_user"]:
        expect(credentials).to_contain_text(user)
    expect(login_page.locator("[data-test='login-password']")).to_contain_text(PASSWORD)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("username", ["standard_user", "problem_user", "performance_glitch_user",
                                      "error_user", "visual_user"])
def test_valid_users_can_login(login_page: Page, username: str):
    login(login_page, username, PASSWORD)

    expect(login_page).to_have_url(f"{BASE_URL}inventory.html")
    # performance_glitch_user renders the inventory ~5s late
    expect(login_page.get_by_text("Products")).to_be_visible(timeout=15_000)


@pytest.mark.regression
@pytest.mark.parametrize(
    ("username", "password", "message"),
    [
        ("", "", "Epic sadface: Username is required"),
        ("", PASSWORD, "Epic sadface: Username is required"),
        ("standard_user", "", "Epic sadface: Password is required"),
        ("locked_out_user", PASSWORD, "Epic sadface: Sorry, this user has been locked out."),
        ("standard_user", "wrong_password", "Epic sadface: Username and password do not match any user in this service"),
        ("unknown_user", PASSWORD, "Epic sadface: Username and password do not match any user in this service"),
    ],
    ids=["empty_fields", "empty_username", "empty_password", "locked_out", "wrong_password", "unknown_user"],
)
def test_invalid_login_shows_error(login_page: Page, username: str, password: str, message: str):
    login(login_page, username, password)

    expect(login_page).to_have_url(BASE_URL)
    expect(login_page.locator("[data-test='error']")).to_have_text(message)
    expect(login_page.get_by_placeholder("Username")).to_have_class(re.compile(r"\berror\b"))
    expect(login_page.get_by_placeholder("Password")).to_have_class(re.compile(r"\berror\b"))


@pytest.mark.regression
def test_error_message_can_be_dismissed(login_page: Page):
    login(login_page, "", "")
    error = login_page.locator("[data-test='error']")
    expect(error).to_be_visible()

    login_page.get_by_role("button", name="Dismiss error").click()

    expect(error).to_be_hidden()
    expect(login_page.get_by_placeholder("Username")).not_to_have_class(re.compile(r"\berror\b"))


@pytest.mark.regression
def test_login_with_enter_key(login_page: Page):
    login_page.get_by_placeholder("Username").fill("standard_user")
    login_page.get_by_placeholder("Password").fill(PASSWORD)
    login_page.get_by_placeholder("Password").press("Enter")

    expect(login_page).to_have_url(f"{BASE_URL}inventory.html")


@pytest.mark.regression
def test_inventory_requires_login(page: Page):
    page.goto(f"{BASE_URL}inventory.html")

    expect(page.locator("[data-test='error']")).to_have_text(
        "Epic sadface: You can only access '/inventory.html' when you are logged in."
    )
    expect(page.get_by_role("button", name="Login")).to_be_visible()
