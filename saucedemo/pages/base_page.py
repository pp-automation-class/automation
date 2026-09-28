"""
Things every Sauce Demo screen can do: open an address, and (after login)
use the cart icon and the side menu.

Students: do not copy these locators into each page. Inherit BasePage instead.
LoginPage inherits it too, but the menu is not on screen until you log in.
"""

import logging

from playwright.sync_api import Page

from config import BASE_URL

log = logging.getLogger(__name__)


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

        # Sauce Demo marks elements with data-test="...".
        # Those attributes stay the same when the layout changes,
        # so we prefer them to CSS classes.
        self.cart_link = page.locator("[data-test='shopping-cart-link']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        # data-test="open-menu" is on the icon inside the button.
        # The button itself has the name "Open Menu", so we click that.
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.logout_link = page.locator("[data-test='logout-sidebar-link']")

    def open(self, path: str = "/") -> None:
        """Open a path on saucedemo.com, for example '/inventory.html'."""
        log.info("Open %s", path)
        self.page.goto(f"{BASE_URL}{path}")
        log.debug("Now on %s", self.page.url)

    def open_cart(self) -> None:
        log.info("Open the cart")
        self.cart_link.click()

    def logout(self) -> None:
        """Open the side menu, then click Logout."""
        log.info("Log out")
        self.menu_button.click()
        self.logout_link.click()
