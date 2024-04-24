from dash import Dash, html, Output, Input, callback, dcc, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

# dataset clean
df = pd.read_excel('dre.xlsx')
# pd.set_option('display.max_columns', None)
# df.tail()
# print(df)

# dataset com algums indicadores financeiros criados
df['% Lucro Bruto'] = df['Lucro bruto Total'] / df['Receita líquida']
df['(Despesas) e \nReceitas Operacionais'] = df['(Despesas) e \nReceitas Operacionais'].abs()

df['Ponto de Equilibrio R$'] = df['(Despesas) e \nReceitas Operacionais'] / df['% Lucro Bruto'].astype(float)

df['% Ponto de Equilibrio'] = df['Ponto de Equilibrio R$'] / df['Receita Varejo'] * 100

df['% Lucratividade'] = df['Lucro (prejuízo) antes do resultado financeiro'] / df['Receita líquida de mercadorias'] * 100
df['% - Despesas e Receitas Operacionais'] = df['(Despesas) e \nReceitas Operacionais'] / df['Receita líquida'] * 100
df['(%) Ebitda'] = df['EBITDA'] / df['Receita líquida'] * 100

df['Receita líquida'] = df['Receita líquida'].astype(float)
df['Ponto de Equilibrio R$'] = df['Ponto de Equilibrio R$'].astype(float)

# print(df)


# Variável de configuração tamanho do dbc.Card([])
tab_card = {'height': '100%'}
dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css")
themes_options = [
    {'label' : 'FLATLY', 'value' : dbc.themes.FLATLY},
    {'label' : 'DARKLY', 'value' : dbc.themes.DARKLY},
    {'label' : 'QUARTZ', 'value' : dbc.themes.QUARTZ}
    ]

config_graph = {'displayModeBar': False, 'showTips': False}


main_config = {
    "hovermode": "x unified",
    "legend":{"yanchor": "top", 
              "y": 0.8, "xanchor": "left", 
              "x": 0.0,
              "title": {"text": None},
              "font": {"color": "white"},
              "bgcolor": "rgba(0,0,0,0.5)"},
    "margin":{"l": 10, "r": 10, "t": 80, "b": 10}
}


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
                            html.H1('Analysis Financial (dre)', style={"text-align": "center", 'font-size': '400%'}) #'color': 'rgba(53, 61, 98, 0.75)'

                        ], sm=10, align='center', style={'border-radius': '10px'}), #'background-color': 'rgba(50, 72, 174, 0.75)'

                        dbc.Col([
                            ThemeChangerAIO(aio_id='theme', radio_props={'value' : dbc.themes.QUARTZ, 'options': themes_options})

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

    dfLB = df.groupby('Ano', sort=False)['% Lucro Bruto'].sum().reset_index()

    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=dfLB['Ano'],
                        y=dfLB['% Lucro Bruto'],
                        name='Porcetagem de Lucro Bruto',
                        text=dfLB['% Lucro Bruto'].round(2),
                        textposition='auto',
                        insidetextfont=dict(family='Times', size=9)
                        ))
    fig1.update_layout(main_config,
                       height=450,
                       title='(%) Lucro Bruto',
                       xaxis_title='(%) Lucro Bruto',
                       yaxis_title='(%) Porcento',
                       template=template_from_url(theme))
    fig1.add_annotation(text='(% Lucro Bruto',
                        xref='paper',
                        yref='paper',
                        font=dict(size=12, color='gray'),
                        align='center',
                        bgcolor='rgba(0,0,0,0.8)',
                        x=0.50,
                        y=0.99,
                        showarrow=True)

    return fig1

'''
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
'''

if __name__ == '__main__':
    app.run(debug=True)
