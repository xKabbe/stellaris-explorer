"""
File: test_dashboard.py
Author: Steven (Kabbe)
Description: This file contains unit tests for the dashboard of the Dash web application.

For more information, see: https://github.com/xKabbe/stellaris-explorer
"""
from dash.testing.application_runners import import_app

app = import_app("app.frontend.dashboard")


def test_app_layout(dash_duo) -> None:
    """
    Test the layout of the Dash web application.
    :param dash_duo: DashComposite instance for testing
    """
    dash_duo.start_server(app)

    assert dash_duo.find_element("h1").text == 'Example Dashboard'
    assert dash_duo.find_element("h2").text == 'A basic example of a Dash web application.'
