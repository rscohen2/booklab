# import dash



import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from layout import layout  # Import layout from layout.py
import pandas as pd
# Initialize the Dash app
app = dash.Dash(__name__)

# Sample data for the plot
df = pd.DataFrame({
    "Fruit": ["Apple", "Orange", "Banana", "Pear", "Grape"],
    "Amount": [10, 15, 7, 5, 12],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
})



# Layout of the app
app.layout = html.Div([
    html.H1("Fruit Amounts in Different Cities"),

    # Dropdown for selecting a city
    dcc.Dropdown(
        id="city-dropdown",
        options=[
            {"label": "New York", "value": "New York"},
            {"label": "Los Angeles", "value": "Los Angeles"},
            {"label": "Chicago", "value": "Chicago"},
            {"label": "Houston", "value": "Houston"},
            {"label": "Phoenix", "value": "Phoenix"},
        ],
        value="New York"  # Default selected value
    ),

    # Graph to display fruit amounts
    dcc.Graph(id="fruit-graph")
])


# Callback to update the graph based on selected city
@app.callback(
    Output("fruit-graph", "figure"),
    [Input("city-dropdown", "value")]
)
def update_graph(city):
    filtered_df = df[df["City"] == city]
    fig = px.bar(filtered_df, x="Fruit", y="Amount", title=f"Fruit Amounts in {city}")
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
