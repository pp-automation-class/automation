import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def logged_in_page(page: Page) -> Page:
    """Log in to SauceDemo and ensure arrival on the inventory page."""
    page.goto(BASE_URL)
    page.locator('[data-test="username"]').fill(USERNAME)
    page.locator('[data-test="password"]').fill(PASSWORD)
    page.locator('[data-test="login-button"]').click()
    
    # Assert successful login and navigation to the inventory page
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")
    return page


# ==============================================================================
# Positive Test Scenarios
# ==============================================================================

@pytest.mark.smoke
@pytest.mark.regression
def test_add_single_item_and_verify_cart(logged_in_page: Page) -> None:
    """
    Positive Test:
    1. Add an item ('Sauce Labs Backpack') to cart from inventory.
    2. Verify cart badge displays count 1.
    3. Click shopping cart link to navigate to cart.
    4. Verify user is on cart page.
    5. Verify cart contains the added item, expected price, and quantity 1.
    """
    page = logged_in_page

    # Add 'Sauce Labs Backpack' to cart
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    # Verify shopping cart badge shows '1'
    cart_badge = page.locator('[data-test="shopping-cart-badge"]')
    expect(cart_badge).to_be_visible()
    expect(cart_badge).to_have_text("1")

    # Click the shopping cart link to access the cart
    page.locator('[data-test="shopping-cart-link"]').click()

    # Verify navigation to cart page
    expect(page).to_have_url(f"{BASE_URL}/cart.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Your Cart")

    # Verify item details in cart
    cart_items = page.locator('[data-test="inventory-item"]')
    expect(cart_items).to_have_count(1)
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_text("Sauce Labs Backpack")
    expect(page.locator('[data-test="inventory-item-price"]')).to_have_text("$29.99")
    expect(page.locator('[data-test="item-quantity"]')).to_have_text("1")


@pytest.mark.regression
def test_add_multiple_items_and_verify_cart(logged_in_page: Page) -> None:
    """
    Positive Test:
    1. Add two items to cart from inventory.
    2. Verify cart badge displays count 2.
    3. Click shopping cart link to navigate to cart.
    4. Verify both items appear in the cart list.
    """
    page = logged_in_page

    # Add two items
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()

    # Verify shopping cart badge shows '2'
    cart_badge = page.locator('[data-test="shopping-cart-badge"]')
    expect(cart_badge).to_be_visible()
    expect(cart_badge).to_have_text("2")

    # Click shopping cart link to access the cart
    page.locator('[data-test="shopping-cart-link"]').click()

    # Verify navigation to cart page
    expect(page).to_have_url(f"{BASE_URL}/cart.html")

    # Verify both items exist in the cart
    cart_items = page.locator('[data-test="inventory-item"]')
    expect(cart_items).to_have_count(2)
    item_names = page.locator('[data-test="inventory-item-name"]')
    expect(item_names).to_have_text(["Sauce Labs Backpack", "Sauce Labs Bike Light"])


@pytest.mark.regression
def test_remove_item_from_cart_page(logged_in_page: Page) -> None:
    """
    Positive Test:
    1. Add an item and access the shopping cart.
    2. Remove the item using the 'Remove' button inside the cart.
    3. Verify item is removed and cart badge disappears.
    """
    page = logged_in_page

    # Add item and go to cart
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()
    expect(page).to_have_url(f"{BASE_URL}/cart.html")

    # Click remove button inside the cart
    page.locator('[data-test="remove-sauce-labs-backpack"]').click()

    # Verify item is removed and cart is empty
    expect(page.locator('[data-test="inventory-item"]')).to_have_count(0)

    # Verify cart badge is no longer displayed
    expect(page.locator('[data-test="shopping-cart-badge"]')).not_to_be_visible()


@pytest.mark.regression
def test_continue_shopping_from_cart(logged_in_page: Page) -> None:
    """
    Positive Test:
    1. Add an item and access the cart.
    2. Click 'Continue Shopping'.
    3. Verify user returns to the inventory page and the cart retains its contents.
    """
    page = logged_in_page

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()
    expect(page).to_have_url(f"{BASE_URL}/cart.html")

    # Click 'Continue Shopping' button
    page.locator('[data-test="continue-shopping"]').click()

    # Verify returned to inventory page
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")

    # Verify cart badge still retains the item count
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")


# ==============================================================================
# Negative Test Scenarios
# ==============================================================================

@pytest.mark.negative
@pytest.mark.regression
def test_empty_cart_has_no_items_and_no_badge(logged_in_page: Page) -> None:
    """
    Negative Test:
    1. Log in without adding any items.
    2. Verify cart badge does not exist.
    3. Access cart via shopping cart link.
    4. Verify cart page shows 0 items and no badge.
    """
    page = logged_in_page

    # Verify badge is not visible on inventory page
    expect(page.locator('[data-test="shopping-cart-badge"]')).not_to_be_visible()

    # Click shopping cart link
    page.locator('[data-test="shopping-cart-link"]').click()

    # Verify navigation to cart page
    expect(page).to_have_url(f"{BASE_URL}/cart.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Your Cart")

    # Verify cart has no items
    expect(page.locator('[data-test="inventory-item"]')).to_have_count(0)
    expect(page.locator('[data-test="shopping-cart-badge"]')).not_to_be_visible()


@pytest.mark.negative
@pytest.mark.regression
def test_item_removed_on_inventory_page_not_in_cart(logged_in_page: Page) -> None:
    """
    Negative Test:
    1. Add an item from inventory page.
    2. Immediately remove it from the inventory page before visiting cart.
    3. Verify badge is removed.
    4. Access cart via shopping cart link.
    5. Verify cart contains 0 items.
    """
    page = logged_in_page

    # Add then remove item on inventory page
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")

    page.locator('[data-test="remove-sauce-labs-backpack"]').click()
    expect(page.locator('[data-test="shopping-cart-badge"]')).not_to_be_visible()

    # Click shopping cart link
    page.locator('[data-test="shopping-cart-link"]').click()
    expect(page).to_have_url(f"{BASE_URL}/cart.html")

    # Verify cart has 0 items
    expect(page.locator('[data-test="inventory-item"]')).to_have_count(0)


@pytest.mark.negative
@pytest.mark.regression
def test_unauthenticated_user_cannot_access_cart(page: Page) -> None:
    """
    Negative Test:
    1. Attempt to navigate directly to /cart.html without logging in.
    2. Verify user is blocked and redirected to login page.
    3. Verify error message is displayed.
    """
    page.goto(f"{BASE_URL}/cart.html")

    # Verify redirected / stays on login page
    expect(page.locator('[data-test="login-button"]')).to_be_visible()

    # Verify error message
    error_message = page.locator('[data-test="error"]')
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("You can only access '/cart.html' when you are logged in")


@pytest.mark.negative
@pytest.mark.regression
def test_checkout_from_empty_cart_fails_validation(logged_in_page: Page) -> None:
    """
    Negative Test:
    1. Access empty cart via shopping cart link.
    2. Click 'Checkout'.
    3. Attempt to proceed without providing mandatory customer information.
    4. Verify validation error banner is displayed.
    """
    page = logged_in_page

    # Navigate to cart
    page.locator('[data-test="shopping-cart-link"]').click()
    expect(page).to_have_url(f"{BASE_URL}/cart.html")

    # Click checkout
    page.locator('[data-test="checkout"]').click()
    expect(page).to_have_url(f"{BASE_URL}/checkout-step-one.html")

    # Click continue without filling in first name, last name, or postal code
    page.locator('[data-test="continue"]').click()

    # Verify validation error
    error_container = page.locator('[data-test="error"]')
    expect(error_container).to_be_visible()
    expect(error_container).to_have_text("Error: First Name is required")
