from dash import dcc
from dash import html

# Input layouts
layout_inputs = html.Div(
    [
        html.H3("Inputs"),
        html.Div(
            [
                dcc.Upload(
                    id="upload-data",
                    children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
                    style={
                        "width": "100%",
                        "height": "60px",
                        "lineHeight": "60px",
                        "borderWidth": "1px",
                        "borderStyle": "dashed",
                        "borderRadius": "5px",
                        "textAlign": "center",
                        "margin": "10px",
                    },
                    # Allow multiple files to be uploaded
                    multiple=True,
                ),
                html.Div(id="output-data-upload"),
            ]
        ),
    ]
)
