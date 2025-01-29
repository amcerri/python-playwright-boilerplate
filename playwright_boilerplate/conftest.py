# Standard library imports
import pytest

# Third-party imports
from playwright.sync_api import sync_playwright

# Local application/library specific imports
# (None for now)

@pytest.fixture(scope="session")
def browser_context():
    """
    Set up and tear down a browser context for the tests.

    Returns:
        object: The browser context object.
    """
    # Start Playwright
    with sync_playwright() as playwright_instance:
        # Launch the browser (headless by default)
        browser = playwright_instance.chromium.launch(headless=True)
        context = browser.new_context()

        # Yield the context to the tests
        yield context

        # Close context and browser after all tests finish
        context.close()
        browser.close()


@pytest.fixture
def setup(browser_context):
    """
    Provide a fresh page for each test.

    Args:
        browser_context (object): The browser context object.

    Returns:
        object: The page object for the test.
    """
    # Create a new page for each test
    page = browser_context.new_page()
    yield page
    # Close the page after the test completes
    page.close()