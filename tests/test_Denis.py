from playwright.sync_api import Page, expect


def test_successful_login(page: Page):
    page.goto("https://www.saucedemo.com/")          # Open https://www.saucedemo.com/

    page.locator("#user-name").press_sequentially("standard_user", delay=100) # Fill the username field with "standard_user"
    page.locator("//input[@id='password']").press_sequentially("secret_sauce", delay=100)   # Fill the password field with "secret_sauce"
    page.locator("#login-button").click()                                     # Click the login button

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")      # Expect the URL to be "https://www.saucedemo.com/inventory.html"
    expect(page.get_by_text("Products")).to_be_visible()                      # Expect the page to have the text "Products" visible

    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()     # Click "Add to cart" for the backpack only
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")


def test_about_page(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").press_sequentially("standard_user", delay=300) # Fill the username field with "standard_user"
    page.locator("#password").press_sequentially("secret_sauce", delay=300)   # Fill the password field with "secret_sauce"
    page.locator("#login-button").click()                                     # Click the login button

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")      # Expect the URL to be "https://www.saucedemo.com/inventory.html"
    expect(page.get_by_text("Products")).to_be_visible()                      # Expect the page to have the text "Products" visible

    page.locator("#react-burger-menu-btn").click()                            # Open the sidebar menu
    about_link = page.locator("[data-test='about-sidebar-link']")
    expect(about_link).to_be_visible()                                        # Expect the "About" link to be visible
    about_link.click()                                                        # Click the "About" sidebar link

    expect(page).to_have_url("https://saucelabs.com/")                        # About leaves the app for saucelabs.com


def test_login_amazon(page: Page):
    page.goto("https://www.amazon.com/")

    page.get_by_role("button", name="Open All Categories Menu").click()
    page.get_by_role("link", name="Hello, sign in").click()
    page.get_by_role("textbox", name="Enter mobile number or email").fill("test@test.com")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("textbox", name="Password").fill("test123")
    page.get_by_role("button", name="Sign in").click()

    expect(page.get_by_text("Your password is incorrect")).to_be_visible()    # Expect the login to be rejected
