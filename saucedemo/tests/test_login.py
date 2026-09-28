"""
Login checks.

Students: assertions stay in the test. Locators stay in LoginPage.
To try another account, pass a different short name to get_user()
and get_password(). Each line in .env is login/password.
"""

import allure
import pytest
from playwright.sync_api import expect

from Data.users import get_password, get_user
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

# Groups these tests under "Login" in the Allure report.
pytestmark = allure.feature("Login")


@pytest.mark.smoke
def test_login_form_is_visible(login: LoginPage) -> None:
    expect(login.page).to_have_title("Swag Labs")
    expect(login.username_input).to_be_visible()
    expect(login.password_input).to_be_visible()
    expect(login.login_button).to_be_enabled()


@pytest.mark.smoke
def test_standard_user_opens_the_products(login: LoginPage) -> None:
    login.login(get_user("standard"), get_password("standard"))

    products = InventoryPage(login.page)
    expect(products.title).to_have_text("Products")


def test_locked_out_user_sees_an_error(login: LoginPage) -> None:
    login.login(get_user("locked_out"), get_password("locked_out"))

    expect(login.error).to_have_text(
        "Epic sadface: Sorry, this user has been locked out."
    )


def test_empty_login_asks_for_a_username(login: LoginPage) -> None:
    login.login(username="", password="")

    expect(login.error).to_have_text("Epic sadface: Username is required")


@pytest.mark.smoke
def test_logout_returns_to_the_login_form(inventory: InventoryPage) -> None:
    inventory.logout()

    login_screen = LoginPage(inventory.page)
    expect(login_screen.login_button).to_be_visible()
