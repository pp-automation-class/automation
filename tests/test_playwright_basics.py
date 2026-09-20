import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
@pytest.mark.regression
def test_successful_login(page: Page):
    page.set_default_timeout(5000)
    page.goto("https://www.saucedemo.com/")          # Open https://www.saucedemo.com/
    page.screenshot(path="screenshots/screenshot.png", full_page=True)

    page.locator("#user-name1").press_sequentially("standard_user", delay=100) # Fill the username field with "standard_user"
    page.locator("//input[@id='password']").press_sequentially("secret_sauce", delay=100)   # Fill the password field with "secret_sauce"
    page.locator("#login-button").click(timeout=1000)                                       # Click the login button
    page.screenshot(path="screenshots/screenshot1.png", full_page=True)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")      # Expect the URL to be "https://www.saucedemo.com/inventory.html"
    expect(page.get_by_text("Products")).to_be_visible()                      # Expect the page to have the text "Products" visible

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

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.get_by_text("Epic sadface: Username and password do not match any user in this service")).to_be_visible()
