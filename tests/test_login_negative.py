"""Negative tests for the https://www.saucedemo.com/ login page."""

import re

import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"
PASSWORD = "secret_sauce"

USERNAME_REQUIRED = "Epic sadface: Username is required"
PASSWORD_REQUIRED = "Epic sadface: Password is required"
NO_MATCH = "Epic sadface: Username and password do not match any user in this service"
LOCKED_OUT = "Epic sadface: Sorry, this user has been locked out."


@pytest.fixture
def login_page(page: Page) -> Page:
    page.goto(BASE_URL)
    return page


def login(page: Page, username: str, password: str) -> None:
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()


def error_message(page: Page):
    return page.locator("[data-test='error']")


@pytest.mark.regression
@pytest.mark.parametrize(
    ("username", "password", "message"),
    [
        ("", "", USERNAME_REQUIRED),
        ("", PASSWORD, USERNAME_REQUIRED),
        ("standard_user", "", PASSWORD_REQUIRED),
        ("standard_user", "wrong_password", NO_MATCH),
        ("no_such_user", PASSWORD, NO_MATCH),
        ("locked_out_user", PASSWORD, LOCKED_OUT),
    ],
    ids=[
        "both_fields_empty",
        "empty_username",
        "empty_password",
        "wrong_password",
        "unknown_username",
        "locked_out_user",
    ],
)
def test_invalid_credentials_show_error(login_page: Page, username: str, password: str, message: str):
    login(login_page, username, password)

    expect(login_page).to_have_url(BASE_URL)
    expect(error_message(login_page)).to_have_text(message)


@pytest.mark.regression
@pytest.mark.parametrize(
    ("username", "password"),
    [
        ("STANDARD_USER", PASSWORD),
        ("Standard_User", PASSWORD),
        ("standard_user", "SECRET_SAUCE"),
        ("standard_user", "Secret_Sauce"),
    ],
    ids=["username_upper", "username_mixed", "password_upper", "password_mixed"],
)
def test_credentials_are_case_sensitive(login_page: Page, username: str, password: str):
    login(login_page, username, password)

    expect(login_page).to_have_url(BASE_URL)
    expect(error_message(login_page)).to_have_text(NO_MATCH)


@pytest.mark.regression
@pytest.mark.parametrize(
    ("username", "password"),
    [
        ("  standard_user  ", PASSWORD),
        ("standard_user", "  secret_sauce  "),
    ],
    ids=["padded_username", "padded_password"],
)
def test_credentials_are_not_trimmed(login_page: Page, username: str, password: str):
    login(login_page, username, password)

    expect(login_page).to_have_url(BASE_URL)
    expect(error_message(login_page)).to_have_text(NO_MATCH)


@pytest.mark.regression
@pytest.mark.parametrize(
    "username",
    [
        "' OR '1'='1",
        "<script>alert(1)</script>",
        "standard_user' --",
        "a" * 256,
    ],
    ids=["sql_injection", "xss_payload", "sql_comment", "very_long_username"],
)
def test_malicious_or_oversized_username_is_rejected(login_page: Page, username: str):
    login(login_page, username, PASSWORD)

    expect(login_page).to_have_url(BASE_URL)
    expect(error_message(login_page)).to_have_text(NO_MATCH)


@pytest.mark.regression
def test_failed_login_marks_both_fields_with_error(login_page: Page):
    login(login_page, "standard_user", "wrong_password")

    expect(login_page.get_by_placeholder("Username")).to_have_class(re.compile(r"\berror\b"))
    expect(login_page.get_by_placeholder("Password")).to_have_class(re.compile(r"\berror\b"))


@pytest.mark.regression
def test_failed_login_keeps_the_entered_values(login_page: Page):
    login(login_page, "standard_user", "wrong_password")

    # both fields keep what was typed, so the user can correct just one of them
    expect(login_page.get_by_placeholder("Username")).to_have_value("standard_user")
    expect(login_page.get_by_placeholder("Password")).to_have_value("wrong_password")


@pytest.mark.regression
def test_error_can_be_dismissed_and_fields_are_reset(login_page: Page):
    login(login_page, "", "")
    expect(error_message(login_page)).to_be_visible()

    login_page.get_by_role("button", name="Dismiss error").click()

    expect(error_message(login_page)).to_be_hidden()
    expect(login_page.get_by_placeholder("Username")).not_to_have_class(re.compile(r"\berror\b"))
    expect(login_page.get_by_placeholder("Password")).not_to_have_class(re.compile(r"\berror\b"))


@pytest.mark.regression
def test_error_is_replaced_on_the_next_failed_attempt(login_page: Page):
    login(login_page, "standard_user", "")
    expect(error_message(login_page)).to_have_text(PASSWORD_REQUIRED)

    login(login_page, "", PASSWORD)

    expect(error_message(login_page)).to_have_text(USERNAME_REQUIRED)


@pytest.mark.regression
def test_enter_key_with_empty_fields_shows_error(login_page: Page):
    login_page.get_by_placeholder("Password").press("Enter")

    expect(login_page).to_have_url(BASE_URL)
    expect(error_message(login_page)).to_have_text(USERNAME_REQUIRED)


@pytest.mark.regression
@pytest.mark.parametrize(
    "path",
    ["inventory.html", "cart.html", "checkout-step-one.html", "checkout-step-two.html"],
    ids=["inventory", "cart", "checkout_step_one", "checkout_step_two"],
)
def test_protected_pages_are_not_reachable_without_login(page: Page, path: str):
    page.goto(f"{BASE_URL}{path}")

    expect(page).to_have_url(BASE_URL)
    expect(error_message(page)).to_have_text(
        f"Epic sadface: You can only access '/{path}' when you are logged in."
    )


@pytest.mark.regression
def test_session_is_not_restored_by_going_back_after_logout(login_page: Page):
    login(login_page, "standard_user", PASSWORD)
    expect(login_page).to_have_url(f"{BASE_URL}inventory.html")

    login_page.locator("#react-burger-menu-btn").click()
    # the sidebar is aria-hidden until it finishes opening, so address the link by id
    login_page.locator("#logout_sidebar_link").click()
    expect(login_page).to_have_url(BASE_URL)

    login_page.go_back()

    expect(error_message(login_page)).to_have_text(
        "Epic sadface: You can only access '/inventory.html' when you are logged in."
    )
