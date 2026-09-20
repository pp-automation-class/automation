# Playwright assertions cheat sheet

Reference for `expect()` in the Python sync API, checked against **Playwright 1.62.0**
(the version pinned in this repo). Run `uv run python -c "from importlib.metadata import
version; print(version('playwright'))"` if you want to confirm it hasn't moved.

```python
from playwright.sync_api import Page, expect
```

## How `expect()` differs from `assert`

`expect()` **auto-waits and retries** until the condition passes or the timeout expires
(5 seconds by default). A plain `assert` reads the page once and fails immediately if the
app hasn't finished rendering.

```python
assert page.locator("#a").is_visible()          # one snapshot, flaky
expect(page.locator("#a")).to_be_visible()      # retries for 5s, stable
```

That is why `test_valid_users_can_login` can pass for `performance_glitch_user`: the
inventory renders about 5 seconds late, and `expect(...).to_be_visible(timeout=15_000)`
simply keeps checking.

Every assertion below also has a `not_to_...` form: `not_to_be_visible()`,
`not_to_have_text(...)`, `not_to_have_class(...)` and so on.

## Locator assertions — element state

| Assertion | Passes when |
| --- | --- |
| `to_be_visible()` | in the DOM **and** has a non-empty bounding box |
| `to_be_hidden()` | not in the DOM, or present but not rendered |
| `to_be_attached()` | in the DOM, whether or not it is visible |
| `to_be_enabled()` | not `disabled` |
| `to_be_disabled()` | `disabled` |
| `to_be_editable()` | can be typed into (not readonly, not disabled) |
| `to_be_checked(checked=, indeterminate=)` | checkbox / radio is in that state |
| `to_be_focused()` | is `document.activeElement` |
| `to_be_empty()` | no text and no child elements |
| `to_be_in_viewport(ratio=)` | scrolled into view |

## Locator assertions — content

| Assertion | Passes when |
| --- | --- |
| `to_have_text(expected)` | text matches in **full** (list for multi-element locators) |
| `to_contain_text(expected)` | text contains the substring |
| `to_have_value(value)` | input/textarea/select has that value |
| `to_have_values(values)` | a `<select multiple>` has exactly those options selected |
| `to_have_count(count)` | the locator resolves to that many elements |
| `to_have_attribute(name, value)` | HTML attribute matches |
| `to_have_class(expected)` | the **whole** `class` string matches |
| `to_contain_class(expected)` | one class is present among others |
| `to_have_id(id)` | `id` matches |
| `to_have_css(name, value, pseudo=)` | computed CSS value matches |
| `to_have_js_property(name, value)` | JS property on the DOM node matches |

## Locator assertions — accessibility

| Assertion | Passes when |
| --- | --- |
| `to_have_role(role)` | ARIA role matches |
| `to_have_accessible_name(name)` | accessible name matches |
| `to_have_accessible_description(description)` | accessible description matches |
| `to_have_accessible_error_message(error_message)` | accessible error message matches |
| `to_match_aria_snapshot(expected)` | the subtree matches an ARIA snapshot |

## Page assertions

| Assertion | Passes when |
| --- | --- |
| `to_have_url(url_or_reg_exp, ignore_case=)` | the current URL matches |
| `to_have_title(title_or_reg_exp)` | `<title>` matches |
| `to_match_aria_snapshot(expected)` | the page matches an ARIA snapshot |

## API response assertions

| Assertion | Passes when |
| --- | --- |
| `to_be_ok()` | status is in the 200–299 range |

Used with `page.request` / `APIRequestContext`, not with a locator.

## Common options

- `timeout=` — milliseconds, per assertion. `expect(...).to_be_visible(timeout=15_000)`.
- `ignore_case=True` — on the text, accessibility and URL assertions.
- `use_inner_text=True` — on `to_have_text` / `to_contain_text`, compares rendered text
  instead of `textContent`.
- A **regex** works anywhere a string does: `expect(page).to_have_url(re.compile(r"/inventory\.html$"))`.
- `expect.set_options(timeout=10_000)` changes the default timeout for the whole run.

## Gotchas worth remembering

### `to_have_class` compares the entire attribute

A failed saucedemo input is `class="input_error form_input error"`, so
`to_have_class("error")` **fails** — it compares the full string. Two working forms:

```python
expect(field).to_have_class(re.compile(r"\berror\b"))   # used in test_login_negative.py
expect(field).to_contain_class("error")                 # newer, no import needed
```

### Pin the error message to its element

```python
expect(page.get_by_text("Epic sadface: ...")).to_be_visible()          # anywhere on the page
expect(page.locator("[data-test='error']")).to_have_text("Epic ...")   # the banner, exact text
```

The second form is stricter and is what `test_login_negative.py` uses.

### `not_to_be_visible()` also passes when the element never existed

So it is a weak check for "the thing went away" unless you assert it was visible first:

```python
error = page.locator("[data-test='error']")
expect(error).to_be_visible()      # it appeared
page.locator("button.error-button").click()
expect(error).to_be_hidden()       # and now it is gone
```

### Locators are lazy, assertions are not

`page.locator("#a")` does not touch the page; it is a recipe. Nothing is queried until an
assertion or an action runs, which is why a locator can be built before the element exists.

## Soft assertions

`expect.soft(...)` records the failure and lets the test keep running; all of them are
reported together at the end. Good for checking several independent things in one test.

```python
expect.soft(page.locator("#a")).to_have_text("one")
expect.soft(page.locator("#b")).to_have_text("two")   # still runs if the first failed
```

Use a normal `expect()` when the rest of the test cannot work without it — for example
the login step that every later assertion depends on.
