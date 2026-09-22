from playwright.sync_api import Page, expect

def test_verify_empty_cart(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.locator(".shopping_cart_link").click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.locator(".shopping_cart_badge")).not_to_be_visible()
    expect(page.locator(".cart_item")).to_have_count(0)


def test_remove_backpack_from_cart(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.locator("#add-to-cart-sauce-labs-backpack").click(timeout=5000)
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    page.locator(".shopping_cart_link").click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    page.locator("#remove-sauce-labs-backpack").click(timeout=5000)
    expect(page.locator(".shopping_cart_badge")).not_to_be_visible()
