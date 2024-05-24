from dash import Dash, html, Output, Input, callback, dcc, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots # add nos propriedades de layout aos gráficos
import pandas as pd
import numpy as np
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

# dataset's

df = pd.read_excel('datasets/dre.xlsx')
# pd.set_option('display.max_columns', None)
# df.tail()
# print(df)

# dfcapex = pd.read_excel('datasets/drecapex.xlsx', usecols=['Investimentos (R$ Milhões)', '2018', '2019', '2020', '2021', '2022', '2023'])


# dataset com algums indicadores financeiros
df['% Lucro Bruto'] = df['Lucro bruto Total'] / df['Receita líquida']
df['(Despesas) e Receitas Operacionais'] = df['(Despesas) e \nReceitas Operacionais'].abs()

df['Ponto de Equilibrio R$'] = df['(Despesas) e Receitas Operacionais'] / df['% Lucro Bruto'].astype(float)

df['% Lucro Bruto'] = df['% Lucro Bruto'] * 100
df['% Lucro Bruto'] = df['% Lucro Bruto'].round(1)

df['% Ponto de Equilibrio'] = df['Ponto de Equilibrio R$'] / df['Receita Varejo'] * 100

df['% Lucratividade'] = df['Lucro (prejuízo) antes do resultado financeiro'] / df['Receita líquida de mercadorias'] * 100
df['% - Despesas e Receitas Operacionais'] = df['(Despesas) e Receitas Operacionais'] / df['Receita líquida'] * 100
df['(%) Ebitda'] = df['EBITDA'] / df['Receita líquida'] * 100

df['Receita líquida'] = df['Receita líquida'].astype(float)
df['Ponto de Equilibrio R$'] = df['Ponto de Equilibrio R$'].astype(float)

df['EBITDA Ajustada S/ Receita Líquida'] = df['Margem EBITDA \nAjustada sobre Receita Líquida Total'] * 100

# print(df)


#  variável configuração tamanho do dbc.Card([])
tab_card = {'height': '100%'}

#  variável configuração tamanho do dbc.Card([])
tab_indicator = {'height': '100%'}

#  variável configuração css
dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css")

# variável - configuração de temas
themes_options = [
    {'label' : 'MATERIA', 'value' : dbc.themes.MATERIA},
    {'label' : 'VAPOR', 'value' : dbc.themes.VAPOR},
    {'label' : 'QUARTZ', 'value' : dbc.themes.QUARTZ}
    ]

config_graph = {'displayModeBar': False, 'showTips': False}

# configuração - layout dos gráficos
main_config = {
    "hovermode": "x unified", 
    "legend":{"yanchor": "top", 
              "y": 0.99, "xanchor": "left", 
              "x": 0.0,
              "title": {"text": None},
              "font": {"color": "white"},
              "bgcolor": "rgba(0,0,0,0.5)"},
    "margin":{"l": 10, "r": 10, "t": 80, "b": 10}
}


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])

# layout do app
app.layout = dbc.Container(children=[

    # Row 1 Títulos
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1('Year Financial Analysis (dre)', style={"text-align": "center", 'font-size': '200%'}) #'color': 'rgba(53, 61, 98, 0.75)'

                        ], sm=11, align='center', style={'border-radius': '10px'}), #'background-color': 'rgba(50, 72, 174, 0.75)'

                        dbc.Col([
                            ThemeChangerAIO(aio_id='theme', radio_props={'value' : dbc.themes.MATERIA, 'options': themes_options})

                        ], sm=1)
                    ])
                ])
            ], style=tab_card)
        ], sm=4, lg=12),
    ], class_name='g-2 my-auto', style={'margin-top': '7px'}),

    # Row 2 Indicators
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='graphA', config=config_graph)
                        ])
                    ], style=tab_indicator)
                ])
            ]),
        ], sm=2, lg=2),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='graphB', config=config_graph)
                        ])
                    ], style=tab_indicator)
                ])
            ]),
        ], sm=2, lg=2),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='graphC', config=config_graph)
                        ])
                    ], style=tab_indicator)
                ])
            ]),
        ], sm=2, lg=2),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='graphD', config=config_graph)
                        ])
                    ], style=tab_indicator)
                ])
            ]),
        ], sm=6, lg=2),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='graphE', config=config_graph)
                        ])
                    ], style=tab_indicator)
                ])
            ]),
        ], sm=2, lg=2),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='graphF', config=config_graph)
                        ])
                    ], style=tab_indicator)
                ])
            ]),
        ], sm=2, lg=2),
    ], class_name='g-2 my-auto', style={'margin-top': '7px'}),

    # Row 3 Gráficos
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
        ], sm=6, lg=3),
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
        ], sm=6, lg=3),
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
        ], sm=6, lg=3),
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
        ], sm=12, lg=3),
    ], class_name='g-2 my-auto', style={'margin-top': '7px'}),

    # Row 4 Gráficos
    dbc.Row([
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
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='graph7', config=config_graph)
                        ])
                    ], style=tab_card)
                ])
            ])
        ], sm=6, lg=4),
    ], class_name='g-2 my-auto', style={'margin-top': '7px'}),

], fluid=True, class_name="dbc")


@callback(
        Output(component_id='graph1', component_property='figure'),
        Input(ThemeChangerAIO.ids.radio('theme'), component_property='value')
)
def graph1(theme):

    dfRP = df.groupby(['Ano','Receita líquida'])['Ponto de Equilibrio R$'].sum().reset_index()

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=dfRP['Ano'],
                          y=dfRP['Receita líquida'],
                          name='Rec',
                          text=dfRP['Receita líquida'].round(2),
                          width=[0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                          marker=dict(cornerradius="14%"),
                          textposition='auto',
                          insidetextfont=dict(family='Times', size=10)))

    fig2.add_trace(go.Bar(x=dfRP['Ano'],
                          y=dfRP['Ponto de Equilibrio R$'],
                          marker=dict(cornerradius="14%"),
                          name='P.Eq',
                          # text=dfRP['Ponto de Equilibrio R$'].round(2),
                          # textposition='auto',
                          # insidetextfont=dict(family='Times', size=14)
                          ))


    fig2.update_layout(main_config,
                       height=250,
                       title='Receita Líquida x Ponto de Equilibrio',
                       #xaxis_title='Receita Liquida x Ponto de Equilibrio',
                       yaxis_title='Valores de Receitas',
                       barmode='group',
                       template=template_from_url(theme))

    return fig2


@callback(
        Output(component_id='graph2', component_property='figure'),
        Input(ThemeChangerAIO.ids.radio('theme'), component_property='value')
)
def graph2(theme):
    
    dfLB = df.groupby('Ano', sort=False)['% Lucro Bruto'].sum().reset_index()

    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=dfLB['Ano'],
                        y=dfLB['% Lucro Bruto'],
                        name='Porcetagem de Lucro Bruto',
                        text=dfLB['% Lucro Bruto'].round(2),
                        width=[0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                        marker=dict(cornerradius="14%"),
                        textposition='auto',
                        insidetextfont=dict(family='Times', size=10)
                        ))
    
    fig1.update_layout(main_config,
                       height=250,
                       title='(%) Lucro Bruto',
                       # xaxis_title='(%) Lucro Bruto',
                       yaxis_title='% Percentual',
                       template=template_from_url(theme))
    
    #fig1.add_annotation(text='(% Lucro Bruto',
                        #xref='paper',
                        #yref='paper',
                        #font=dict(size=12, color='gray'),
                        #align='center',
                        #bgcolor='rgba(0,0,0,0.8)',
                        #x=0.50,
                        #y=0.99,
                        #showarrow=False)
    
    return fig1


@callback(
        Output(component_id='graph3', component_property='figure'),
        Input(ThemeChangerAIO.ids.radio('theme'), component_property='value')
)
def graph3(theme):

    dfDO = df.groupby('Ano')['% - Despesas e Receitas Operacionais'].sum().reset_index()

    fig3 = go.Figure()
    fig3.add_trace(go.Bar(x=dfDO['Ano'],
                      y=dfDO['% - Despesas e Receitas Operacionais'],
                      name='(%) Despesas e Receitas Operacionais',
                      text=dfDO['% - Despesas e Receitas Operacionais'].round(1),
                      width=[0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                      marker=dict(cornerradius="14%"),
                      textposition='auto',
                      insidetextfont=dict(family='Times', size=10))
                      )

    fig3.update_layout(main_config,
                       height=250,
                       title='(%) Despesas e Receitas Operacionais',
                       # xaxis_title='(%) Despesas e Receitas Operacionais',
                       yaxis_title=' % Percentual',
                       template=template_from_url(theme)
                       )
    
    #fig3.add_annotation(text='(%) Despesas Operacionais',
                        #xref='paper',
                        #yref='paper',
                        #font=dict(size=12, color='gray'),
                        #align='center',
                        #bgcolor='rgba(0,0,0,0.8)',
                        #x=0.50,
                        #y=0.99,
                        #showarrow=False)

    return fig3


@callback(
        Output(component_id='graph4', component_property='figure'),
        Input(ThemeChangerAIO.ids.radio('theme'), component_property='value')
)
def graph4(theme):

    dfLUC = df.groupby('Ano')['% Lucratividade'].sum().reset_index().round(1)

    fig4 = go.Figure()
    fig4.add_trace(go.Bar(x=dfLUC['Ano'],
                          y=dfLUC['% Lucratividade'],
                          name='% Lucratividade',
                          text=dfLUC['% Lucratividade'].round(1),
                          width=[0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                          marker=dict(cornerradius="14%"),
                          textposition='auto',
                          insidetextfont=dict(family='Times', size=10)
                          ))
    
    fig4.update_layout(main_config,
                       height=250,
                       title='(%) Lucratividade',
                       # xaxis_title='(%) Lucratividade Ano',
                       yaxis_title=' % Percentual',
                       template=template_from_url(theme)
                       )
    
    #fig4.add_annotation(text='% Lucratividade',
                        #xref='paper',
                        #yref='paper',
                        #font=dict(size=12, color='gray'),
                        #align='center',
                        #bgcolor='rgba(0,0,0,0.8)',
                        #x=0.50,
                        #y=0.99,
                        #showarrow=False)

    return fig4


@callback(
        Output(component_id='graph5', component_property='figure'),
        Input(ThemeChangerAIO.ids.radio('theme'), component_property='value')
)
def graph5(theme):

    dfEBT = df.groupby('Ano')['(%) Ebitda'].sum().reset_index().round(1)

    fig5 = go.Figure()
    fig5.add_trace(go.Bar(x=dfEBT['Ano'],
                          y=dfEBT['(%) Ebitda'],
                          name='Ebitda',
                          text=dfEBT['(%) Ebitda'].round(1),
                          width=[0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                          marker=dict(cornerradius="14%"),
                          textposition='auto',
                          insidetextfont=dict(family='Times', size=10)
                          ))
    
    fig5.update_layout(main_config,
                       height=250,
                       title='(%) Ebitda',
                       # xaxis_title='(%) Ebitda Ano',
                       yaxis_title='% Percentual',
                       template=template_from_url(theme)
                       )

    #fig5.add_annotation(text='(%) Ebitda',
                        #xref='paper',
                        #yref='paper',
                        #font=dict(size=12, color='gray'),
                        #align='center',
                        #bgcolor='rgba(0,0,0,0.8)',
                        #x=0.50,
                        #y=0.99,
                        #showarrow=False)
    
    return fig5


@callback(
        Output(component_id='graph6', component_property='figure'),
        Input(ThemeChangerAIO.ids.radio('theme'), component_property='value')
)
def graph6(theme):

    dfEBTAJ = df.groupby('Ano')['EBITDA Ajustada S/ Receita Líquida'].sum().reset_index().round(1)

    fig6 = go.Figure()
    fig6.add_trace(go.Bar(x=dfEBTAJ['Ano'],
                          y=dfEBTAJ['EBITDA Ajustada S/ Receita Líquida'],
                          name='Ebitda Ajustado S/ Receita Líquida',
                          text=dfEBTAJ['EBITDA Ajustada S/ Receita Líquida'].round(1),
                          width=[0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                          marker=dict(cornerradius="14%"),
                          textposition='auto',
                          insidetextfont=dict(family='Times', size=10)
                        ))
    
    fig6.update_layout(main_config,
                       height=250,
                       title='(%) EBITDA Ajustada S/ Receita Líquida',
                       #xaxis_title='EBITDA Ajustada S/ Receita Líquida',
                       yaxis_title='% Percentual',
                       template=template_from_url(theme)
                       )

    #fig6.add_annotation(text='EBITDA Ajustada S/ Receita Líquida',
                        #xref='paper',
                        #yref='paper',
                        #font=dict(size=12, color='gray'),
                        #align='center',
                        #bgcolor='rgba(0,0,0,0.8)',
                        #x=0.50,
                        #y=0.99,
                        #showarrow=False)

    return fig6


@callback(
        Output(component_id='graph7', component_property='figure'),
        Input(ThemeChangerAIO.ids.radio('theme'), component_property='value')
)
def graph7(theme):

    dfcapex = pd.read_excel('datasets/drecapex.xlsx', usecols=['Investimentos (R$ Milhões)', '2018', '2019', '2020', '2021', '2022', '2023'])

    dfcapex.rename(columns={0: 'Investimentos (R$ Milhões)', 1: '2018', 2: '2019', 3: '2020', 4:'2021', 5:'2022', 6:'2023'}, inplace=True)

    dfcapexA = dfcapex.T.reset_index()


    dfcapexA.rename(columns={'index': 'Ano', 0: 'Novas Lojas' , 1: 'Reformas e Remodelagens', 2: 'Cadeia de Suprimentos', 3: 'Digital e Tecnologia'}, inplace=True)
    dfcapexA = dfcapexA.drop(0, axis=0)


    fig7 = go.Figure()
    fig7.add_trace(go.Scatter(x=dfcapexA['Ano'],
                              y=dfcapexA['Novas Lojas'],
                              name='Nova Lojas',
                              text=dfcapexA['Novas Lojas'],
                              textposition='top center',
                              textfont=dict(family='Times', size=10)
                      ))
    fig7.add_trace(go.Scatter(x=dfcapexA['Ano'],
                              y=dfcapexA['Reformas e Remodelagens'],
                              name='Reformas e Remodelagens'
                      ))
    fig7.add_trace(go.Scatter(x=dfcapexA['Ano'],
                              y=dfcapexA['Cadeia de Suprimentos'],
                              name='Cadeia de Suprimentos'
                      ))
    fig7.add_trace(go.Scatter(x=dfcapexA['Ano'],
                              y=dfcapexA['Digital e Tecnologia'],
                              name='Digital e Tecnologia'
                      ))
    fig7.update_layout(main_config,
                       height=250,
                       title='CAPEX',
                       #xaxis_title='CAPEX',
                       yaxis_title='Valores',
                       template=template_from_url(theme)
                    )
    return fig7

    
@callback(
        Output(component_id='graphA', component_property='figure'),
        Input(ThemeChangerAIO.ids.radio('theme'), component_property='value')
)
def graphA(theme):

    dfindicators = df.groupby('Ano')['Receita líquida'].sum().reset_index()

    figA = go.Figure()
    figA.add_trace(go.Indicator(mode='number',
                                value=dfindicators['Receita líquida'].iloc[0],
                                title={"text": f"<span style='font-size:90%'>{dfindicators['Ano'].iloc[0]}</span><br><span style='font-size:90%'>Receita Líquida</span>"},
                                number={'prefix': 'R$ '}
                                ))
    
    figA.update_layout(main_config, height=80,
                       template=template_from_url(theme)
                       )
    
    figA.update_layout({"margin": {"l": 0, "r": 0, "t": 60, "b": 0}}
                       )

    return figA


@callback(
        Output(component_id='graphB', component_property='figure'),
        Input(ThemeChangerAIO.ids.radio('theme'), component_property='value')
)
def graphB(theme):

    dfindicators = df.groupby('Ano')['Receita líquida'].sum().reset_index()

    figB = go.Figure()
    figB.add_trace(
    go.Indicator(mode='number',
                 value=dfindicators['Receita líquida'].iloc[1],
                 title={"text": f"<span style='font-size:90%'>{dfindicators['Ano'].iloc[1]}</span><br><span style='font-size:90%'>Receita Líquida</span>"},
                 number={'prefix': 'R$ '}
                 ))
    
    figB.update_layout(main_config, height=80,
                       template=template_from_url(theme)
                       )
    
    figB.update_layout({"margin": {"l": 0, "r": 0, "t": 60, "b": 0}})

    return figB


@callback(
        Output(component_id='graphC', component_property='figure'),
        Input(ThemeChangerAIO.ids.radio('theme'), component_property='value')
)
def graphC(theme):

    dfindicators = df.groupby('Ano')['Receita líquida'].sum().reset_index()

    figC = go.Figure()
    figC.add_trace(
    go.Indicator(mode='number',
                 value=dfindicators['Receita líquida'].iloc[2],
                 title={"text": f"<span style='font-size:90%'>{dfindicators['Ano'].iloc[2]}</span><br><span style='font-size:90%'>Receita Líquida</span>"},
                 number={'prefix': 'R$ '}
                 ))
    
    figC.update_layout(main_config, height=80,
                       template=template_from_url(theme)
                       )
    
    figC.update_layout({"margin": {"l": 0, "r": 0, "t": 60, "b": 0}})

    return figC


@callback(
        Output(component_id='graphD', component_property='figure'),
        Input(ThemeChangerAIO.ids.radio('theme'), component_property='value')
)
def graphD(theme):

    dfindicators = df.groupby('Ano')['Receita líquida'].sum().reset_index()

    figD = go.Figure()
    figD.add_trace(
    go.Indicator(mode='number',
                 value=dfindicators['Receita líquida'].iloc[3],
                 title={"text": f"<span style='font-size:90%'>{dfindicators['Ano'].iloc[3]}</span><br><span style='font-size:90%'>Receita Líquida</span>"},
                 number={'prefix': 'R$ '}
                 ))
    
    figD.update_layout(main_config, height=80,
                       template=template_from_url(theme)
                       )
    
    figD.update_layout({"margin": {"l": 0, "r": 0, "t": 60, "b": 0}})

    return figD


@callback(
        Output(component_id='graphE', component_property='figure'),
        Input(ThemeChangerAIO.ids.radio('theme'), component_property='value')
)
def graphE(theme):

    dfindicators = df.groupby('Ano')['Receita líquida'].sum().reset_index()

    figE = go.Figure()
    figE.add_trace(
    go.Indicator(mode='number',
                 value=dfindicators['Receita líquida'].iloc[4],
                 title={"text": f"<span style='font-size:90%'>{dfindicators['Ano'].iloc[4]}</span><br><span style='font-size:90%'>Receita Líquida</span>"},
                 number={'prefix': 'R$ '}
                 ))
    
    figE.update_layout(main_config, height=80,
                       template=template_from_url(theme)
                       )
    
    figE.update_layout({"margin": {"l": 0, "r": 0, "t": 60, "b": 0}})

    return figE



@callback(
        Output(component_id='graphF', component_property='figure'),
        Input(ThemeChangerAIO.ids.radio('theme'), component_property='value')
)
def graphF(theme):

    dfindicators = df.groupby('Ano')['Receita líquida'].sum().reset_index()

    figF = go.Figure()
    figF.add_trace(
    go.Indicator(mode='number',
                 value=dfindicators['Receita líquida'].iloc[5],
                 title={"text": f"<span style='font-size:90%'>{dfindicators['Ano'].iloc[5]}</span><br><span style='font-size:90%'>Receita Líquida</span>"},
                 number={'prefix': 'R$ '}
                 ))
    
    figF.update_layout(main_config, height=80,
                       template=template_from_url(theme)
                       )
    
    figF.update_layout({"margin": {"l": 0, "r": 0, "t": 60, "b": 0}})

    return figF


if __name__ == '__main__':
    app.run(debug=True)
