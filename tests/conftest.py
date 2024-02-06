"""
This is a configuration file for pytest containing customizations and fixtures.
"""
import pytest
from pytest_socket import disable_socket


def pytest_runtest_setup():
    """Disable socket calls during tests to ensure network calls are prevented."""
    disable_socket()


@pytest.fixture(name="message")
def hello_world() -> str:
    """
    Example fixture

    Returns
        str : 'Hello World'

    Use this fixture in a testcase like:

    def test_hello_world(message: str) -> None:
        print(message) # will print 'Hello World'
        ...
    """
    return "Hello World"
