import re
from playwright.async_api import Page, expect


def test_example1(page: Page):
    page.goto("https://playwright.dev")

    #expect(page).to_have_title(re.compile("Playwright"))
