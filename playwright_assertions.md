# Playwright Assertions (`expect`) Cheat Sheet

Reference for the web-first assertions available in `playwright.sync_api`.
Generated against Playwright 1.62 — every matcher below exists in the installed version.

```python
from playwright.sync_api import Page, expect
```

## Why `expect()` and not `assert`

Every matcher here **auto-retries** until it passes or the timeout expires (5s by default).
That is what makes tests stable — you never need `sleep()` or `wait_for_timeout()`.

```python
# Bad: checks once, immediately, and flakes
assert page.locator("#error").is_visible()

# Good: waits for the banner to appear
expect(page.locator("#error")).to_be_visible()
```

Every matcher has a negative twin: `to_be_visible()` / `not_to_be_visible()`.

---

## On a Locator — state

| Matcher | Passes when |
| --- | --- |
| `to_be_visible()` | element is in the DOM **and** rendered |
| `to_be_hidden()` | element is absent, or in the DOM but not rendered |
| `to_be_attached()` | element is in the DOM at all (may be invisible) |
| `to_be_enabled()` | element is not disabled |
| `to_be_disabled()` | element is disabled |
| `to_be_editable()` | input is neither `readonly` nor `disabled` |
| `to_be_checked()` | checkbox / radio is checked |
| `to_be_focused()` | element has keyboard focus |
| `to_be_empty()` | element has no text and no children |
| `to_be_in_viewport()` | element is scrolled into view |

```python
expect(page.locator("#login-button")).to_be_enabled()
expect(page.locator("#password")).to_be_editable()
```

## On a Locator — content

```python
expect(loc).to_have_text("Products")        # full text content, exact match
expect(loc).to_contain_text("sadface")      # substring — handy for error banners
expect(loc).to_have_value("standard_user")  # input / select / textarea value
expect(loc).to_have_values(["a", "b"])      # multi-select
expect(loc).to_have_count(6)                # how many elements the locator matches
```

`to_have_text` with a list checks a multi-element locator in order, and asserts the count too:

```python
expect(page.locator(".inventory_item_name")).to_have_text(
    ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
)
```

## On a Locator — attributes and styling

```python
expect(loc).to_have_attribute("type", "password")
expect(loc).to_have_id("login-button")
expect(loc).to_have_class("btn_action")      # the exact, complete class string
expect(loc).to_contain_class("error")        # one class among many
expect(loc).to_have_css("color", "rgb(226, 35, 26)")
expect(loc).to_have_js_property("checked", True)
```

## On a Locator — accessibility

```python
expect(loc).to_have_role("button")
expect(loc).to_have_accessible_name("Login")
expect(loc).to_have_accessible_description("Use your team account")
expect(loc).to_have_accessible_error_message("Password is required")  # aria-errormessage
expect(loc).to_match_aria_snapshot("""                                # whole a11y tree
  - button "Login"
""")
```

## On a Page

```python
expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
expect(page).to_have_title("Swag Labs")
```

## On an APIResponse

```python
expect(response).to_be_ok()   # status in 200-299
```

---

## Options

**Regex** works anywhere a string is accepted:

```python
import re
expect(page).to_have_url(re.compile(r"/inventory\.html$"))
```

**`timeout=`** (milliseconds) overrides the default on any matcher:

```python
expect(page.locator("[data-test='error']")).to_contain_text("locked out", timeout=10_000)
```

**`ignore_case=`** on the text matchers:

```python
expect(loc).to_have_text("products", ignore_case=True)
```

---

## Full matcher list

State: `to_be_attached` · `to_be_checked` · `to_be_disabled` · `to_be_editable` ·
`to_be_empty` · `to_be_enabled` · `to_be_focused` · `to_be_hidden` ·
`to_be_in_viewport` · `to_be_visible`

Content: `to_have_text` · `to_contain_text` · `to_have_value` · `to_have_values` ·
`to_have_count`

Attributes: `to_have_attribute` · `to_have_id` · `to_have_class` · `to_contain_class` ·
`to_have_css` · `to_have_js_property`

Accessibility: `to_have_role` · `to_have_accessible_name` ·
`to_have_accessible_description` · `to_have_accessible_error_message` ·
`to_match_aria_snapshot`

Page: `to_have_url` · `to_have_title`

APIResponse: `to_be_ok`

Each one also exists as `not_to_*`.
