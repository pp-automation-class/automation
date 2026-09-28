"""Shopping cart: /cart.html"""

import logging

from playwright.sync_api import Page

from pages.base_page import BasePage

log = logging.getLogger(__name__)


class CartPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.title = page.locator("[data-test='title']")
        self.items = page.locator("[data-test='inventory-item']")
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def open(self) -> None:
        super().open("/cart.html")

    def item(self, name: str):
        """The cart row whose title is name."""
        return self.items.filter(has_text=name)

    def checkout(self) -> None:
        log.info("Checkout")
        self._debug("checkout", self.checkout_button)
        self.checkout_button.click()
