# layout.py

from dash import html, dcc

# Define the layout
layout = html.Div([
    html.H1("Dash App with Circular Import Fix"),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Option 1', 'value': '1'},
            {'label': 'Option 2', 'value': '2'}
        ],
        value='1'
    ),
    html.Div(id='output-container')
])
