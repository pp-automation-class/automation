"""
Buy one product, from the list to the thank-you screen.

Students: each step builds the next page object with the same tab
(`inventory.page`). The browser does not go back to the start.
"""

import allure
import pytest
from playwright.sync_api import expect

from config import BACKPACK
from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.inventory_page import InventoryPage

# Groups this test under "Checkout" in the Allure report.
pytestmark = allure.feature("Checkout")


@pytest.mark.smoke
def test_buy_one_backpack(inventory: InventoryPage) -> None:
    inventory.add_item(BACKPACK)
    inventory.open_cart()

    cart = CartPage(inventory.page)
    cart.checkout()

    info = CheckoutInfoPage(inventory.page)
    expect(info.title).to_have_text("Checkout: Your Information")
    info.fill_your_information()
    info.continue_checkout()

    overview = CheckoutOverviewPage(inventory.page)
    expect(overview.title).to_have_text("Checkout: Overview")
    expect(overview.item(BACKPACK)).to_be_visible()
    expect(overview.item_total).to_have_text("Item total: $29.99")
    overview.finish()

    done = CheckoutCompletePage(inventory.page)
    expect(done.header).to_have_text("Thank you for your order!")
