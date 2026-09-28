"""Login screen: https://www.saucedemo.com/"""

import logging

from playwright.sync_api import Page

from pages.base_page import BasePage

log = logging.getLogger(__name__)


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # Placeholder locators follow the text the user sees in the box.
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error = page.locator("[data-test='error']")

    def open(self) -> None:
        super().open("/")

    def login(self, username: str, password: str) -> None:
        """
        Type the account and click Login.

        Pass the pair from .env: get_user("standard"), get_password("standard").
        press_sequentially types one character at a time, so --slowmo shows each key.
        """
        # Never write the password to the log.
        log.info("Log in as %r", username)
        self.username_input.press_sequentially(username)
        self.password_input.press_sequentially(password)
        self.login_button.click()
