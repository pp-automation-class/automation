from playwright.sync_api import Page, expect

def test_add_sauce_labs_backpack_to_cart(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.locator("#add-to-cart-sauce-labs-backpack").click(timeout=5000)
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    page.locator(".shopping_cart_link").click()
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()


def test_add_backpack_and_bolt_t_shirt_to_cart(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.locator("#add-to-cart-sauce-labs-backpack").click(timeout=5000)
    page.locator("#add-to-cart-sauce-labs-bolt-t-shirt").click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("2")
    page.locator(".shopping_cart_link").click()
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
    expect(page.get_by_text("Sauce Labs Bolt T-Shirt", exact=True)).to_be_visible()
