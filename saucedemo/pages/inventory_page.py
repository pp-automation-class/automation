"""Product list, shown after a successful login: /inventory.html"""

import logging

from playwright.sync_api import Page

from pages.base_page import BasePage

log = logging.getLogger(__name__)


class InventoryPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # "Products" is a span, not a heading, so we use data-test.
        self.title = page.locator("[data-test='title']")
        self.items = page.locator("[data-test='inventory-item']")

    def open(self) -> None:
        """
        Open the product list directly.

        The site sends you back to login if you are not logged in.
        Tests that need this page usually use the inventory fixture.
        """
        super().open("/inventory.html")

    def add_item(self, name: str) -> None:
        """
        Click Add to cart on one product.

        name is the full title, for example "Sauce Labs Backpack".
        A short name can match more than one card.
        """
        log.info("Add to cart: %s", name)
        button = self.items.filter(has_text=name).get_by_role(
            "button", name="Add to cart"
        )
        self._debug("add to cart", button)
        button.click()
