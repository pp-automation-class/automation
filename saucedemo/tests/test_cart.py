"""
Add a product and find it in the cart.

Students: the test calls page methods. It does not look up buttons itself.
"""

import allure
import pytest
from playwright.sync_api import expect

from config import BACKPACK
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

# Groups this test under "Cart" in the Allure report.
pytestmark = allure.feature("Cart")


@pytest.mark.smoke
def test_adding_a_product_updates_the_cart(inventory: InventoryPage) -> None:
    inventory.add_item(BACKPACK)

    expect(inventory.cart_badge).to_have_text("1")

    inventory.open_cart()
    cart = CartPage(inventory.page)
    expect(cart.title).to_have_text("Your Cart")
    expect(cart.item(BACKPACK)).to_be_visible()
