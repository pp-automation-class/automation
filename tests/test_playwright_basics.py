import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
@pytest.mark.regression
def test_successful_login(page: Page):
    # page.set_default_timeout(10000)
    page.goto("https://www.saucedemo.com/")                 # Open https://www.saucedemo.com/
    
    expect(page).to_have_url("https://www.saucedemo.com/")
    # page.screenshot(path="screenshots/screenshot.png", full_page=True)

    page.locator("#user-name1").press_sequentially("standard_user", delay=100)    # Must press sequentially to avoid typing issues
    page.locator("//input[@id='password']").fill("secret_sauce")      # Fill the password field with "secret_sauce"
    page.locator("#login-button").click(timeout=1000)               # Click the login button
    # page.screenshot(path="screenshots/screenshot1.png", full_page=False)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html") # Expect the page to have the URL "https://www.saucedemo.com/inventory.html"
    expect(page.get_by_text("Products")).to_be_visible() # Expect the page to have the text "Products"


@pytest.mark.regression
def test_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Products")).to_be_visible()

@pytest.mark.regression
def test_unsuccessful_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user11")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory1.html")
    expect(page.get_by_text("Products")).to_be_visible()    


def test_add_to_cart(page: Page):
    # Login to the application
    page.goto("https://www.saucedemo.com/")
    # fill the username field with "standard_user"
    page.locator("#user-name").press_sequentially("standard_user", delay=100)
    # fill the password field with "secret_sauce"
    page.locator("//input[@id='password'] || //input[@placeholder='Password']").fill("secret_sauce")
    # click the login button
    page.locator("#login-button").click()
    # click the add to cart button
    page.locator("//button[text()='Add to cart']").click()
    # click the cart button
