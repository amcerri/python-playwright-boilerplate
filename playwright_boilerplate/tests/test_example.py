# Standard library imports
import logging

# Third-party imports
import pytest
from playwright.sync_api import Page

# Local application/library specific imports
from pages.base_page import BasePage


@pytest.mark.usefixtures("setup")
def test_example(setup: Page) -> None:
    """
    Simple test example using the BasePage.

    Args:
        setup (Page): Fixture that provides a new Playwright page for each test.
    """
    base_page = BasePage(setup)  # Initialize a BasePage with the provided Page
    base_page.goto("https://example.com")  # Navigate to Example.com

    logging.info("Asserting the page title contains 'Example Domain'")
    assert "Example Domain" in base_page.get_title()