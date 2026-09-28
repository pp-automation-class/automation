"""Checkout step 2, the order summary: /checkout-step-two.html"""

import logging

from playwright.sync_api import Page

from pages.base_page import BasePage

log = logging.getLogger(__name__)


class CheckoutOverviewPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.title = page.locator("[data-test='title']")
        self.items = page.locator("[data-test='inventory-item']")
        self.item_total = page.locator("[data-test='subtotal-label']")
        self.finish_button = page.get_by_role("button", name="Finish")

    def open(self) -> None:
        super().open("/checkout-step-two.html")

    def item(self, name: str):
        return self.items.filter(has_text=name)

    def finish(self) -> None:
        log.info("Finish the order")
        self.finish_button.click()
