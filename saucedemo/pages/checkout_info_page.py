"""Checkout step 1, your details: /checkout-step-one.html"""

import logging

from playwright.sync_api import Page

from helper.letters import _letters
from pages.base_page import BasePage

log = logging.getLogger(__name__)


class CheckoutInfoPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.title = page.locator("[data-test='title']")
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.postal_code = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.error = page.locator("[data-test='error']")

    def open(self) -> None:
        super().open("/checkout-step-one.html")

    def fill_your_information(self, postal_code: str = "2000") -> None:
        """
        Type a first and last name, then the postal code.

        The names are letters from Faker, a new pair on every run.
        press_sequentially types one letter at a time, so --slowmo shows each key.
        The postal code is digits, so it is filled in one step.
        """
        first_name, last_name = _letters(), _letters()
        log.info("Fill your information")
        log.debug("Name %s %s, postal code %s", first_name, last_name, postal_code)
        self._debug("first name", self.first_name)
        self.first_name.press_sequentially(first_name)
        self._debug("last name", self.last_name)
        self.last_name.press_sequentially(last_name)
        self._debug("postal code", self.postal_code)
        self.postal_code.fill(postal_code)

    def continue_checkout(self) -> None:
        log.info("Continue")
        self._debug("continue", self.continue_button)
        self.continue_button.click()
