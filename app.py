from dash import Dash, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as ps
import numpy as np

# Variável de configuração tamanho do dbc.Card([])
tab_card = {'height': '100%'}
dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])

# layout do app
app.layout = dbc.Container(children=[
    # Row 1
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1('Analysis Financial (dre)', style={"text-align": "center", 'font-size': '400%', 'color': 'rgba(53, 61, 98, 0.75)'})

                        ], sm=12, align='center', style={'background-color': 'rgba(50, 72, 174, 0.75)', 'border-radius': '10px'})
                    ])
                ])
            ], style=tab_card)
        ], sm=4, lg=12),
    ], class_name='g-2 my-auto', style={'margin-top': '7px'}),

    # Row 2
    dbc.Row([], class_name='g-2 my-auto', style={'margin-top': '7px'}),

    # Row 3
    dbc.Row([], class_name='g-2 my-auto', style={'margin-top': '7px'}),

], fluid=True)


if __name__ == '__main__':
    app.run(debug=True)