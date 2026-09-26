import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
@pytest.mark.regression
def test_add_one_product_to_cart(page: Page):
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Samsung galaxy s6").click()
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("link", name="Add to cart").click()
    page.get_by_role("link", name="Cart", exact=True).click()
    expect(page.get_by_role("cell", name="Samsung galaxy s6")).to_be_visible()



    for _ in range(3):
        page.once("dialog", lambda dialog: dialog.accept())
        page.get_by_role("link", name="Add to cart ").click()
        page.wait_for_timeout(800)
        page.get_by_role("link", name="Cart", exact=True).click()
        expect(page.get_by_role("row").filter(has_text="Samsung galaxy s6").nth(1)).to_have_text("2")
        expect(page.locator("#totalp")).to_have_text("720")
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Samsung galaxy s6").click()
    for _ in range(4):
        page.once("dialog", lambda dialog: dialog.accept())
        page.get_by_role("link", name="Add to cart").click()
        page.wait_for_timeout(800)
    page.get_by_role("link", name="Cart", exact=True).click()
    expect(page.get_by_role("row").filter(has_text="Samsung galaxy s6")).to_have_count(6)
    expect(page.locator("#totalp")).to_have_text("2160")
