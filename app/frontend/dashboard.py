"""
File: dashboard.py
Author: Steven (Kabbe)
Description: Basic example of a Dash web application showcasing interactive visualizations using Python.

For more information, see: https://github.com/xKabbe/stellaris-explorer
"""
import dash
from dash import dcc, html


app = dash.Dash(__name__)
app.layout = html.Div(children=[html.H1(children='Example Dashboard'),
                                html.H2(children='A basic example of a Dash web application.'),
                                dcc.Graph(id='example-graph',
                                          figure={'data': [{'x': [1, 2, 3, 4],
                                                            'y': [10, 11, 12, 13],
                                                            'type': 'line', 'name': 'Trace 1'},
                                                           {'x': [1, 2, 3, 4],
                                                            'y': [14, 15, 16, 17],
                                                            'type': 'line', 'name': 'Trace 2'}],
                                                  'layout': {'title': 'Line Chart Example'}})])
