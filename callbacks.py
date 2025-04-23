# callbacks.py

from dash.dependencies import Input, Output
from app import app  # Import the app from app.py

# Define the callback function to update the output container
def register_callbacks(app):
    @app.callback(
        Output('output-container', 'children'),
        [Input('dropdown', 'value')]
    )
    def update_output(value):
        return f'You selected {value}'
