# Standard library imports
import logging

# Third-party imports
from playwright.sync_api import Page

# Local application/library specific imports
# (None for now)

class BasePage:
    """
    Base class for all page objects.

    Attributes:
        page (Page): The Playwright Page object used for automation.
    """

    def __init__(self, page: Page) -> None:
        """
        Initialize the page with the provided Playwright Page object.

        Args:
            page (Page): The Playwright Page object used for automation.
        """
        self.page = page

    def goto(self, url: str) -> None:
        """
        Navigate to the specified URL.

        Args:
            url (str): The URL to navigate to.
        """
        logging.info(f"Navigating to {url}")
        self.page.goto(url)  # Use Playwright's goto method

    def get_title(self) -> str:
        """
        Retrieve the title of the current page.

        Returns:
            str: The title of the current page.
        """
        return self.page.title()  # Return the page title