"""
File: conftest.py
Author: Steven (Kabbe)
Description: Pytest configuration file for Stellaris Explorer project.

For more information, see: https://github.com/xKabbe/stellaris-explorer
"""
import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Fixture to modify browser context arguments for tests.
    :param browser_context_args: Original browser context arguments
    :return: Modified browser context arguments with a specified viewport size
    """
    return {**browser_context_args,
            "viewport": {"width": 1920, "height": 1080}}
