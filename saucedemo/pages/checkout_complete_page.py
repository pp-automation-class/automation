"""Checkout step 3, the thank-you screen: /checkout-complete.html"""

from playwright.sync_api import Page

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.title = page.locator("[data-test='title']")
        self.header = page.locator("[data-test='complete-header']")
        self.back_home_button = page.get_by_role("button", name="Back Home")

    def open(self) -> None:
        super().open("/checkout-complete.html")
