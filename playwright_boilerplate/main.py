# Standard library imports
import pytest

# Third-party imports
# (None for now)

# Local application/library specific imports
# (None for now)

def main() -> None:
    """
    Entry point for running the test suite.
    """
    # Execute pytest with verbose and no-capture flags
    pytest.main(["-v", "-s"])


if __name__ == "__main__":
    main()