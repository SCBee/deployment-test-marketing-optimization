from dash import dcc
from dash import html

# Visualization Layout
layout_visualization = html.Div(
    [
        html.H3("Visualization"),
        # Element to output plotly chart
        dcc.Graph(id="output-data"),
    ]
)
