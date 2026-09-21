import pytest
from playwright.sync_api import Page, expect

PRODUCT = "Samsung galaxy s6"
PRICE = 360


def open_product(page: Page):
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name=PRODUCT).click()


def add_to_cart(page: Page, times: int):
    for _ in range(times):
        page.once("dialog", lambda dialog: dialog.accept())
        page.get_by_role("link", name="Add to cart").click()
        page.wait_for_timeout(800)


def open_cart(page: Page):
    page.get_by_role("link", name="Cart", exact=True).click()


def product_rows(page: Page):
    return page.locator("#tbodyid tr").filter(has_text=PRODUCT)


def expect_qty_and_total(page: Page, qty: int):
    expect(product_rows(page)).to_have_count(qty)
    expect(page.locator("#totalp")).to_have_text(str(qty * PRICE))


def delete_from_cart(page: Page, times: int):
    for _ in range(times):
        before = product_rows(page).count()
        page.get_by_role("link", name="Delete").first.click()
        expect(product_rows(page)).to_have_count(before - 1)


@pytest.mark.smoke
@pytest.mark.regression
def test_add_one_product_to_cart(page: Page):
    open_product(page)
    add_to_cart(page, 1)
    open_cart(page)
    expect(page.get_by_role("cell", name=PRODUCT)).to_be_visible()


@pytest.mark.regression
def test_cart_qty_and_price_recalculate(page: Page):
    open_product(page)
    add_to_cart(page, 2)
    open_cart(page)
    expect_qty_and_total(page, 2)

    open_product(page)
    add_to_cart(page, 4)
    open_cart(page)
    expect_qty_and_total(page, 6)

    delete_from_cart(page, 4)
    expect_qty_and_total(page, 2)

    delete_from_cart(page, 1)
    expect_qty_and_total(page, 1)
