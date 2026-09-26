import pytest  # Import pytest to use test markers like regression and xfail
from playwright.sync_api import Page, expect  # Import the Page type and the expect assertion helper from Playwright

BASE_URL = "https://www.demoblaze.com/"  # Base address of the site under test
PRODUCT = "Samsung galaxy s6"  # Product name, kept for future cart tests
FILL_REQUIRED_ALERT = "Please fill out Name and Creditcard."  # Alert text the site shows when required fields are empty


@pytest.mark.regression  # Mark this test as part of the regression suite
@pytest.mark.xfail(reason="Demoblaze allows ordering with an empty cart", strict=True)  # Known bug: test is expected to fail; turns red if the bug gets fixed
def test_place_order_with_empty_cart(page: Page):  # Test: placing an order with an empty cart must be blocked
    page.goto(BASE_URL + "index.html")  # Open the home page
    page.get_by_role("link", name="Cart", exact=True).click()  # Click the "Cart" link in the top menu
    expect(page.locator("#tbodyid tr")).to_have_count(0)  # Check the cart table has no product rows

    page.get_by_role("button", name="Place Order").click()  # Click "Place Order" to open the order form
    expect(page.locator("#orderModal")).to_be_visible()  # Check the order form (modal window) is shown
    page.locator("#name").fill("John")  # Type a name into the "Name" field
    page.locator("#card").fill("4111111111111111")  # Type a test card number into the "Credit card" field
    page.get_by_role("button", name="Purchase").click()  # Click "Purchase" to submit the order

    expect(page.get_by_role("heading", name="Thank you for your purchase!")).not_to_be_visible()  # Check the success message did NOT appear (order was not placed)


@pytest.mark.regression  # Mark this test as part of the regression suite
def test_purchase_with_all_fields_empty(page: Page):  # Test: submitting the order form with all fields empty
    page.goto(BASE_URL + "cart.html")  # Open the cart page directly
    page.get_by_role("button", name="Place Order").click()  # Click "Place Order" to open the order form
    expect(page.locator("#orderModal")).to_be_visible()  # Precondition: check the order form is open

    alert_messages = []  # Empty list to store the text of any alert that appears

    def handle_alert(dialog):  # Function that runs automatically when the browser shows an alert
        alert_messages.append(dialog.message)  # Save the alert text into the list
        dialog.accept()  # Close the alert by clicking "OK" so the page is not blocked

    page.once("dialog", handle_alert)  # Attach the handler for the next alert on the page
    page.get_by_role("button", name="Purchase").click()  # Click "Purchase" without filling any field
    page.wait_for_timeout(1000)  # Wait 1 second to give the alert time to appear
    assert alert_messages == [FILL_REQUIRED_ALERT]  # Check exactly one alert appeared with text "Please fill out Name and Creditcard."

    expect(page.locator("#orderModal")).to_be_visible()  # Check the order form is still open
    expect(page.get_by_role("heading", name="Thank you for your purchase!")).not_to_be_visible()  # Check no order was placed (no success message)


@pytest.mark.regression  # Mark this test as part of the regression suite
def test_purchase_without_name(page: Page):  # Test: submitting the order form with every field filled except Name
    page.goto(BASE_URL + "cart.html")  # Open the cart page directly
    page.get_by_role("button", name="Place Order").click()  # Click "Place Order" to open the order form
    expect(page.locator("#orderModal")).to_be_visible()  # Precondition: check the order form is open

    page.locator("#country").fill("USA")  # Type a country into the "Country" field
    page.locator("#city").fill("New York")  # Type a city into the "City" field
    page.locator("#card").fill("4111111111111111")  # Type a test card number into the "Credit card" field
    page.locator("#month").fill("12")  # Type the month into the "Month" field
    page.locator("#year").fill("2026")  # Type the year into the "Year" field
    expect(page.locator("#name")).to_have_value("")  # Check the "Name" field is left empty

    alert_messages = []  # Empty list to store the text of any alert that appears

    def handle_alert(dialog):  # Function that runs automatically when the browser shows an alert
        alert_messages.append(dialog.message)  # Save the alert text into the list
        dialog.accept()  # Close the alert by clicking "OK" so the page is not blocked

    page.once("dialog", handle_alert)  # Attach the handler for the next alert on the page
    page.get_by_role("button", name="Purchase").click()  # Click "Purchase" with the Name field empty
    page.wait_for_timeout(1000)  # Wait 1 second to give the alert time to appear
    assert alert_messages == [FILL_REQUIRED_ALERT]  # Check exactly one alert appeared with text "Please fill out Name and Creditcard."

    expect(page.get_by_role("heading", name="Thank you for your purchase!")).not_to_be_visible()  # Check no order was placed (no success message)
