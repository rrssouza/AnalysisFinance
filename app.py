from dash import Dash, html, Output, Input, callback, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as ps
import numpy as np
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

# Variável de configuração tamanho do dbc.Card([])
tab_card = {'height': '100%'}
dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css")
themes_options = [
    {'label' : 'FLATLY', 'value' : dbc.themes.FLATLY},
    {'label' : 'DARKLY', 'value' : dbc.themes.DARKLY},
    {'label' : 'QUARTZ', 'value' : dbc.themes.QUARTZ}
    ]

config_graph = {'displayModerBar': False, 'showTips': False}

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

                        ], sm=10, align='center', style={'background-color': 'rgba(50, 72, 174, 0.75)', 'border-radius': '10px'}),

                        dbc.Col([
                            ThemeChangerAIO(aio_id='theme', radio_props={'value' : dbc.themes.DARKLY, 'options': themes_options})

                        ], sm=2)
                    ])
                ])
            ], style=tab_card)
        ], sm=4, lg=12),
    ], class_name='g-2 my-auto', style={'margin-top': '7px'}),

    # Row 2
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='graph1', config=config_graph)
                        ])
                    ], style=tab_card)
                ])
            ]),
        ], sm=12, lg=4),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='graph2', config=config_graph)
                        ])
                    ], style=tab_card)
                ])
            ]),
        ], sm=12, lg=4),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='graph3', config=config_graph)
                        ])
                    ], style=tab_card)
                ])
            ])
        ], sm=12, lg=4),
    ], class_name='g-2 my-auto', style={'margin-top': '7px'}),

    # Row 3
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='graph4', config=config_graph)
                        ])
                    ], style=tab_card)
                ])
            ]),
        ], sm=12, lg=4),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='graph5', config=config_graph)
                        ])
                    ], style=tab_card)
                ])
            ]),
        ], sm=12, lg=4),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='graph6', config=config_graph)
                        ])
                    ], style=tab_card)
                ])
            ])
        ], sm=12, lg=4),
    ], class_name='g-2 my-auto', style={'margin-top': '7px'}),

], fluid=True)

@callback(
        Output(component_id='graph1', component_property='figure'),
        Input(ThemeChangerAIO.ids.radio('theme'), component_property='value')
)
def graph1(theme):
    return


@callback(
        Output(component_id='graph2', component_property='figure')
)
def graph2():
    return


@callback(
        Output(component_id='graph3', component_property='figure')
)
def graph3():
    return


@callback(
        Output(component_id='graph4', component_property='figure')
)
def graph4():
    return


@callback(
        Output(component_id='graph5', component_property='figure')
)
def graph5():
    return

@callback(
        Output(component_id='graph6', component_property='figure')
)
def graph6():
    return


if __name__ == '__main__':
    app.run(debug=True)