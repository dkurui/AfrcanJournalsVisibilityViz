import dash                              # pip install dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
from dash_extensions import Lottie       # pip install dash-extensions
# pip install dash-bootstrap-components
import dash_bootstrap_components as dbc
import plotly.express as px              # pip install plotly
import pandas as pd                      # pip install pandas
from dash.dependencies import Input, Output, State
from dash import dash_table
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from datetime import date
from dash import dependencies
yes_url = 'https://assets7.lottiefiles.com/packages/lf20_oaw8d1yt.json'
no_url = 'https://assets7.lottiefiles.com/packages/lf20_g0rackmk.json'
options = dict(loop=False, autoplay=True, rendererSettings=dict(
    preserveAspectRatio='xMidYMid slice'))
data = pd.read_csv('ajv.csv')
journals = sorted(data['Journal tittle'])

data_frame = pd.DataFrame()
# Bootstrap themes by Ann: https://hellodash.pythonanywhere.com/theme_explorer
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
server = app.server

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H1('AFRICAN JOURNALS VISIBILITY VISUALIZATION', style={
                        'font-family': 'Verdana', 'text-align': 'center'}),
                # dbc.CardImg(src='/assets/Linkedin-Logo.png') # 150px by 45px
            ], className='mb-2'),

        ], width=12),

    ], className='mb-2 mt-5'),

    dbc.Row([
        dbc.Col([
                dbc.Card([
                    dbc.CardHeader('Total Number of Journals Considered', style={
                                   'font-family': 'Inter'}),
                    dbc.CardBody([
                        # html.P('12345'),
                        html.Div(
                            id='content-total', style={'color': 'darkviolet', 'font-weight': 'bold', 'font-size': '28px'}),
                        # html.P('See full list here'),

                    ], style={'textAlign': 'center'})
                ]),
                ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardHeader('Select/Search the Journal from the dropdown below to see its details', style={
                                   'font-family': 'Helevitica'}),
                    dbc.CardBody([
                        html.P(''),
                        # dcc.Input(id='dropdown-id', value='initial value', type='text'),
                        dcc.Dropdown(
                            options=[{'label': journal, 'value': journal}
                                     for journal in journals],
                            # value=data['Journal tittle'][0],  # Set the initial value based on your data
                            value='ACCORD Occasional Paper',  # Set the initial value based on your data
                            id='dropdown-id'
                        ),

                    ])
                ]),
                ], width=6),

    ], className='mb-2 mt-2'),

    dbc.Row([

        dbc.Col([
            dbc.Card([
                dbc.CardHeader(),
                dbc.CardBody([
                    html.H6('PLATFORM'),
                    # html.H2(id='content-platform', children="000", style={'color': 'black'}),
                    html.Div(id='content-platform', style={
                             'color': 'darkviolet', 'font-weight': 'bold', 'font-size': '12px'}),
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px', 'line-height': '1', 'font-size': '11px', 'height': '6rem'})
            ]),
            dbc.Card([
                dbc.CardBody([
                    html.P('Hosted on INASP\'S Journal online'),
                    html.Div(id='content-based-inasp',
                             style={'display': 'none'}),
                    html.Div(id='lottie-content-based-inasp')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px',
                          'line-height': '1', 'font-size': '9px', 'height': '7rem'})
            ], className='mt-2'),

        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.P('Indexed on Google scholar'),
                    html.Div(id='content-google-scholar',
                             style={'display': 'none'}),
                    html.Div(id='lottie-content-google-scholar')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px', 'line-height': '1', 'font-size': '11px', 'height': '7rem'})
            ]),
            dbc.Card([
                dbc.CardBody([
                    html.P('Indexed on Scopus'),
                    html.Div(id='content-scopus', style={'display': 'none'}),
                    html.Div(id='lottie-content-scopus')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px', 'line-height': '1', 'font-size': '11px', 'height': '7rem'})
            ], className='mt-2'),
        ], width=2),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.P('Indexed on at least one platform'),
                    html.Div(id='content-one-platform',
                             style={'display': 'none'}),
                    html.Div(id='lottie-content-one-platform')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px',
                          'line-height': '1', 'font-size': '11px', 'height': '7rem'})
            ]),
            dbc.Card([
                dbc.CardBody([
                    html.P('Open Access Journal'),
                    html.Div(id='content-oaj', style={'display': 'none'}),
                    html.Div(id='lottie-content-oaj')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px',
                          'line-height': '1', 'font-size': '11px', 'height': '7rem'})
            ], className='mt-2'),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.P('Listed in the Directory of Open Access (DOAJ)'),
                    html.Div(id='content-doaj', style={'display': 'none'}),
                    html.Div(id='lottie-content-doaj')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px',
                          'line-height': '1', 'font-size': '11px', 'height': '7rem'})
            ]),
            dbc.Card([
                dbc.CardBody([
                    html.P(
                        'Present on International Standard Serial Number (ISSN) portal'),
                    html.Div(id='content-issn', style={'display': 'none'}),
                     html.Div(id='lottie-content-issn')
                     ], style={'textAlign': 'center',
                               'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px',
                               'line-height': '1', 'font-size': '11px', 'height': '7rem'})
            ], className='mt-2'),
        ], width=3),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.P(
                        'Publisher is a member of Committee on publication Ethics (COPE)'),
                    html.Div(id='content-cope', style={'display': 'none'}),
                    html.Div(id='lottie-content-cope')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px',
                          'line-height': '1', 'font-size': '11px', 'height': '7rem'})
            ]),
            dbc.Card([
                dbc.CardBody([
                    html.P('Online Publisher based in Africa'),
                    html.Div(id='content-based-in-africa',
                             style={'display': 'none'}),
                    html.Div(id='lottie-content-based-in-africa')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px',
                          'line-height': '1', 'font-size': '11px', 'height': '7rem'})
            ], className='mt-2'),
        ], width=3),



    ], className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([

                ])
            ]),
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([

                ])
            ]),
        ], width=6),
    ], className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    'Select the options below to see journals that meet your criteria'),
                dbc.CardBody([
                    html.H6('OPTIONS'),
                    html.H5(id='', children="_____________"),

                    dcc.Checklist(
                        options=[
                            {'label': ' African Journal Online (AJOL)',
                             'value': 'African Journal Online (AJOL)'},
                            {'label': ' SABINET Journal repository',
                             'value': 'SABINET Journal repository'},
                            {'label': ' Indexed on Google Scholar',
                             'value': 'Indexed on Google Scholar'},
                            {'label': ' Indexed on Scopus',
                             'value': 'Indexed on Scopus'},
                            {'label': ' Indexed on at least one platform',
                             'value': 'Indexed on at least one platform'},
                            {'label': ' Open Access Journal',
                             'value': 'Open Access Journal'},
                            {'label': ' Journal listed in the Directory of Open Access (DOAJ)',
                             'value': 'Journal listed in the Directory of Open Access (DOAJ)'},
                            {'label': ' Present on International Standard Serial Number (ISSN) portal',
                             'value': 'Present on International Standard Serial Number (ISSN) portal'},
                            {'label': ' The publisher is a member of Committee on Publication Ethics (COPE)',
                             'value': 'The publisher is a member of Committee on publication Ethics (COPE)'},
                            {'label': ' Online publisher based in Africa',
                             'value': 'Online publisher based in Africa'},
                            {'label': " Hosted on INASP's Journal online",
                             'value': 'Hosted on INASP\'S Journal online'},
                        ],
                        id='checklist-id',
                        style={'textAlign': 'left',
                               'margin-bottom': '10px', 'font-size': '10px'},
                        value=[],  # Set the initial value of the checklist
                    ),

                    dcc.Store(id='selected-values-store')

                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px'}
                )

            ], className='mt-2', style={'height': '23.5rem'})

        ], width=5),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader('List of journals that met your criteria'),

                dbc.CardBody(
                    html.Div(
                        id='output',
                        style={
                            'height': '19rem',
                            'overflowY': 'auto',
                            'font-family': 'sans-serif',
                            'font-size': '11px',
                            'line-height': '1'
                        }
                    ),
                    style={'text-align': 'left', 'margin-top': '2', 'font-family': 'sans-serif',
                           'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px'}

                )
            ], className='mt-2')

        ], width=7),
    ], className='mb-2 mt-5'),

    dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.CardHeader(''),
                        dcc.Graph(id='bar-chart', figure={}),
                    ])
                ]),

            ], width=12),
            ], className='mb-2, mt-3'),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    'Select the platform to filter your data'),
                html.H5(id='', children=''),
                dbc.CardBody([
                    html.H6('OPTIONS'),
                    html.H5(id='', children="_____________"),

                    dcc.Checklist(
                        options=[
                            {'label': ' African Journal Online (AJOL)',
                             'value': 'African Journal Online (AJOL)'},
                            {'label': ' SABINET Journal repository',
                             'value': 'SABINET Journal repository'},
                        ],
                        id='platform-checklist-id',
                        style={
                            'textAlign': 'left', 'margin-bottom': '10px', 'font-size': '10px'},
                        value=[],  # Set the initial value of the checklist
                    ),

                    dcc.Store(id='selected-platform-store')

                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px'}
                )

            ])

        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(''),
                html.Div(id='gs_plat', style={
                         'color': 'darkviolet', 'font-weight': 'bold', 'font-size': '10px', 'text-align': 'center'}),
                dbc.CardBody([
                    dcc.Graph(id='gs-pie-chart', figure={}),
                ])
            ]),

        ], width=5),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(''),
                html.Div(id='s_plat',
                         style={'color': 'darkviolet', 'font-weight': 'bold', 'font-size': '10px', 'text-align': 'center'}),

                dbc.CardBody([
                    dcc.Graph(id='scopus-bar-chart', figure={}),
                ])
            ]),

        ], width=5),
    ], className='mb-2, mt-3'),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(''),
                html.Div(id='doaj_plat', style={
                         'color': 'darkviolet', 'font-weight': 'bold', 'font-size': '10px', 'text-align': 'center'}),
                dbc.CardBody([
                    dcc.Graph(id='doaj-donut-chart', figure={}),
                ])
            ]),
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(''),
                html.Div(id='one_plat', style={
                         'color': 'darkviolet', 'font-weight': 'bold', 'font-size': '10px', 'text-align': 'center'}),
                dbc.CardBody([
                    dcc.Graph(id='oneplat-column-chart', figure={}),
                ])
            ]),

        ], width=6)
    ], className='mb-2, mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    ''),
                html.Div(id='bia_plat', style={
                    'color': 'darkviolet', 'font-weight': 'bold', 'font-size': '10px', 'text-align': 'center'}),
                dbc.CardBody([
                    dcc.Graph(id='basedinafrica-pop-chart', figure={}),
                ])
            ]),
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(''),
                html.Div(id='oaj_plat', style={
                         'color': 'darkviolet', 'font-weight': 'bold', 'font-size': '10px', 'text-align': 'center'}),
                dbc.CardBody([
                    dcc.Graph(id='oaj-donut-chart', figure={}),
                ])
            ]),

        ], width=6)
    ], className='mb-2, mt-2'),
    dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(''),
                    html.Div(id='issn_plat', style={
                         'color': 'darkviolet', 'font-weight': 'bold', 'font-size': '10px', 'text-align': 'center'}),
                    dbc.CardBody([
                        dcc.Graph(id='issn-bar-chart', figure={}),
                    ])
                ]),
            ], width=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(''),
                    html.Div(id='cope_plat', style={
                         'color': 'darkviolet', 'font-weight': 'bold', 'font-size': '10px', 'text-align': 'center'}),
                    dbc.CardBody([
                        dcc.Graph(id='cope-column-chart', figure={}),
                    ])
                ]),

            ], width=6)
            ], className='mb-2, mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(''),
                html.Div(id='inasp_plat', style={
                    'color': 'darkviolet', 'font-weight': 'bold', 'font-size': '10px', 'text-align': 'center'}),
                dbc.CardBody([
                             dcc.Graph(id='inasp-bar-chart', figure={}),
                             ])
            ]),
        ], width=12),

    ], className='mb-2, mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(''),
                dbc.CardBody([

                ])
            ]),
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(''),
                dbc.CardBody([

                ])
            ]),

        ], width=6)
    ], className='mb-5, mt-2')

], fluid=False)


# Updating selected Journal
@app.callback(
    Output(component_id='content-total', component_property='children'),
    Output(component_id='content-platform', component_property='children'),
    Output(component_id='content-google-scholar',
           component_property='children'),
    Output(component_id='content-scopus', component_property='children'),
    Output(component_id='content-one-platform', component_property='children'),
    Output(component_id='content-oaj', component_property='children'),
    Output(component_id='content-doaj', component_property='children'),
    Output(component_id='content-issn', component_property='children'),
    Output(component_id='content-cope', component_property='children'),
    Output(component_id='content-based-in-africa',
           component_property='children'),
    Output(component_id='content-based-inasp', component_property='children'),

    Input(component_id='dropdown-id', component_property='value')
)
def update_output_div(journal):
    data_copy = data.copy()
    df = data_copy.loc[data_copy['Journal tittle'] == journal]
    total = len(data_copy)
    platform = df['Platform']
    google_scholar = df['Indexed on Google Scholar']
    scopus = df['Indexed on Scopus']
    one_platform = df['Indexed on at least one platform']
    oaj = df['Open Access Journal']
    doaj = df['Journal listed in the Directory of Open Access (DOAJ)']
    issn = df['Present on International Standard Serial Number (ISSN) portal']
    cope = df['The publisher is a member of Committee on publication Ethics (COPE)']
    based_in_africa = df['Online publisher based in Africa']
    inasp = df['Hosted on INASP\'S Journal online']

    return total, platform, google_scholar, scopus, one_platform, oaj, doaj, issn, cope, based_in_africa, inasp


@app.callback(
    Output('lottie-content-google-scholar', 'children'),
    [Input('content-google-scholar', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1


@app.callback(
    Output('lottie-content-scopus', 'children'),
    [Input('content-scopus', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1


@app.callback(
    Output('lottie-content-one-platform', 'children'),
    [Input('content-one-platform', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1


@app.callback(
    Output('lottie-content-oaj', 'children'),
    [Input('content-oaj', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1


@app.callback(
    Output('lottie-content-doaj', 'children'),
    [Input('content-doaj', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1


@app.callback(
    Output('lottie-content-issn', 'children'),
    [Input('content-issn', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1


@app.callback(
    Output('lottie-content-cope', 'children'),
    [Input('content-cope', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1


@app.callback(
    Output('lottie-content-based-in-africa', 'children'),
    [Input('content-based-in-africa', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1


@app.callback(
    Output('lottie-content-based-inasp', 'children'),
    [Input('content-based-inasp', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px",
                       height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1


def filter_data(platform, google_scholar, scopus, one_platform, oaj, doaj, issn, cope, based_in_africa, inasp):
    df = data.copy()
    final_df = df.loc[(df['Platform'] == platform) & (df['Indexed on Google Scholar'] == google_scholar) & (df['Indexed on Scopus'] == scopus) &
                      (df['Indexed on at least one platform'] == one_platform) & (df['Open Access Journal'] == oaj) &
                      (df['Journal listed in the Directory of Open Access (DOAJ)'] == doaj) & (df['Present on International Standard Serial Number (ISSN) portal'] == issn) &
                      (df['The publisher is a member of Committee on publication Ethics (COPE)'] == cope) & (df['Online publisher based in Africa'] == based_in_africa) &
                      (df['Hosted on INASP\'S Journal online'] == inasp)
                      ]
    return final_df['Journal tittle']


def fil(cols):
    dataf = data.copy()
    if len(cols) > 0:
        for i in cols:
            dataf = dataf.loc[dataf[i] == 1]
            fin_df = pd.DataFrame(dataf, columns=['Journal tittle'])
        return fin_df
    else:
        fin_df = pd.DataFrame(dataf, columns=['Journal tittle'])
        return fin_df


@app.callback(
    Output('selected-values-store', 'data'),
    [Input('checklist-id', 'value')]
)
def save_selected_values(selected_values):
    return selected_values


@app.callback(
    Output('selected-platform-store', 'data'),
    [Input('platform-checklist-id', 'value')]
)
def save_selected_platform(selected_platforms):
    return selected_platforms


@app.callback(
    Output('gs_plat', 'children'),
    Output('s_plat', 'children'),
    Output('doaj_plat', 'children'),
    Output('one_plat', 'children'),
    Output('oaj_plat', 'children'),
    Output('bia_plat', 'children'),
    Output('issn_plat', 'children'),
    Output('cope_plat', 'children'),
    Output('inasp_plat', 'children'),



    [Input('selected-platform-store', 'data')]
)
def update_source(selected_values):
    if (len(selected_values) == 0):
        header = 'All Jourals in either African Journal Online (AJOL) or SABINET Journal Repository'
        header1 = 'All Jourals in either African Journal Online (AJOL) or SABINET Journal Repository'
        header2 = 'All Jourals in either African Journal Online (AJOL) or SABINET Journal Repository'
        header3 = 'All Jourals in either African Journal Online (AJOL) or SABINET Journal Repository'
        header4 = 'All Jourals in either African Journal Online (AJOL) or SABINET Journal Repository'
        header5 = 'All Jourals in either African Journal Online (AJOL) or SABINET Journal Repository'
        header6 = 'All Jourals in either African Journal Online (AJOL) or SABINET Journal Repository'
        header7 = 'All Jourals in either African Journal Online (AJOL) or SABINET Journal Repository'
        header8 = 'All Jourals in either African Journal Online (AJOL) or SABINET Journal Repository'

    else:
        if (('African Journal Online (AJOL)' in selected_values) and ('SABINET Journal repository' in selected_values)):
            header = 'Journal in both African Journal Online (AJOL) and SABINET Journal Repository'
            header1 = 'Journal in both African Journal Online (AJOL) and SABINET Journal Repository'
            header2 = 'Journal in both African Journal Online (AJOL) and SABINET Journal Repository'
            header3 = 'Journal in both African Journal Online (AJOL) and SABINET Journal Repository'
            header4 = 'Journal in both African Journal Online (AJOL) and SABINET Journal Repository'
            header5 = 'Journal in both African Journal Online (AJOL) and SABINET Journal Repository'
            header6 = 'Journal in both African Journal Online (AJOL) and SABINET Journal Repository'
            header7 = 'Journal in both African Journal Online (AJOL) and SABINET Journal Repository'
            header8 = 'Journal in both African Journal Online (AJOL) and SABINET Journal Repository'

        elif ('SABINET Journal repository' in selected_values):
            header = 'Journals in SABINET Journal repository'
            header1 = 'Journals in SABINET Journal repository'
            header2 = 'Journals in SABINET Journal repository'
            header3 = 'Journals in SABINET Journal repository'
            header4 = 'Journals in SABINET Journal repository'
            header5 = 'Journals in SABINET Journal repository'
            header6 = 'Journals in SABINET Journal repository'
            header7 = 'Journals in SABINET Journal repository'
            header8 = 'Journals in SABINET Journal repository'

        else:
            header = 'Journals in African Journal Online (AJOL)'
            header1 = 'Journals in African Journal Online (AJOL)'
            header2 = 'Journals in African Journal Online (AJOL)'
            header3 = 'Journals in African Journal Online (AJOL)'
            header4 = 'Journals in African Journal Online (AJOL)'
            header5 = 'Journals in African Journal Online (AJOL)'
            header6 = 'Journals in African Journal Online (AJOL)'
            header7 = 'Journals in African Journal Online (AJOL)'
            header8 = 'Journals in African Journal Online (AJOL)'

    return header, header1, header2, header3, header4, header5, header6, header7, header8


# JOURNALS PER PLATFORM BAR GRAPH ************************************************************
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('selected-values-store', 'data')]
)
def platform_bar(plats):
    df = data.copy()
    ajol = len(
        df[df['Platform'] == 'African Journal Online (AJOL)'])
    sabinet = len(
        df[df['Platform'] == 'SABINET Journal repository'])
    dff = pd.DataFrame(data=[[ajol, sabinet]], columns=[
                       'African Journal Online (AJOL)', 'SABINET Journal repository'])
    colors = ['#0C4F67', '#DD3A9E']
    fig_bar = make_subplots(rows=1, cols=1)
    fig_bar.add_trace(
        go.Bar(y=dff.columns, x=dff.values[0], marker=dict(
            color=colors), text=dff.values[0], textposition='auto', orientation='h'),
        row=1, col=1
    )
    fig_bar.update_layout(
        template='seaborn',
        title='Number of Journals per Platform',
        margin=dict(l=20, r=20, t=30, b=20),
        height=200
    )

    fig_bar.update_xaxes(title_text="Count")
    fig_bar.update_yaxes(title_text="Platform")

    return fig_bar


# GOOGLE SCHOLAR PIE CHART ***************************************************************
@app.callback(
    Output('gs-pie-chart', 'figure'),
    [Input('selected-platform-store', 'data')]
)
def google_scholar(plats):
    df = data.copy()
    if len(plats) > 0:
        for i in plats:
            df = df[data['Platform'] == i]
    else:
        df = df
    #     df = data[data['Platform'] == platform]
    g_yes = len(df[df['Indexed on Google Scholar'] == 1])
    g_no = len(df[df['Indexed on Google Scholar'] == 0])
    if g_yes > 0:
        google_yes = round(g_yes / (g_yes + g_no) * 100, 2)
        google_no = round(g_no / (g_yes + g_no) * 100, 2)
        labels = ['Yes: {} ({:.2f}%)'.format(g_yes, google_yes),
                  'No: {} ({:.2f}%)'.format(g_no, google_no)]
        values = [google_yes, google_no]
        colors = ['#D1D0D1', '#9A1651']

        fig_pie = go.Figure(
            data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])
        # Set the desired font size here
        fig_pie.update_traces(textfont_size=20)
        fig_pie.update_layout(title="Journals Indexed on Google Scholar", template='seaborn',
                              margin=dict(l=20, r=20, t=30, b=20), height=300)
    else:

        # empty piechat
        fig_pie = go.Figure(
            data=[go.Pie(labels=[], values=[], marker=dict(colors=[]), hole=1)])
        fig_pie.update_layout(title="", template='seaborn',
                              margin=dict(l=20, r=20, t=30, b=20))

    return fig_pie


# SCOPUS PIE CHART **************************************************************************
@app.callback(
    Output('scopus-bar-chart', 'figure'),
    [Input('selected-platform-store', 'data')]
)
def scopus(plats):
    df = data.copy()
    if len(plats) > 0:
        for i in plats:
            df = df[data['Platform'] == i]
    else:
        df = df
    #     df = data[data['Platform'] == platform]
    g_yes = len(df[df['Indexed on Scopus'] == 1])
    g_no = len(df[df['Indexed on Scopus'] == 0])
    if g_yes > 0:
        google_yes = round(g_yes / (g_yes + g_no) * 100, 2)
        google_no = round(g_no / (g_yes + g_no) * 100, 2)
        labels = ['Yes: {} ({:.2f}%)'.format(g_yes, google_yes),
                  'No: {} ({:.2f}%)'.format(g_no, google_no)]
        values = [google_yes, google_no]
        colors = ['#03195E', '#FFB025']

        fig_pie = go.Figure(
            data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])
        # Set the desired font size here
        fig_pie.update_traces(textfont_size=20)
        fig_pie.update_layout(title="Journals Indexed on Scopus", template='seaborn',
                              margin=dict(l=20, r=20, t=30, b=20), height=300)
    else:

        # empty piechat
        fig_pie = go.Figure(
            data=[go.Pie(labels=[], values=[], marker=dict(colors=[]), hole=1)])
        fig_pie.update_layout(title="Journals Indexed on Scopus", template='seaborn',
                              margin=dict(l=20, r=20, t=30, b=20))

    return fig_pie

# Present on International Standard Serial Number (ISSN) portal PIE CHART ************************************************************************


@app.callback(
    Output('issn-bar-chart', 'figure'),
    [Input('selected-platform-store', 'data')]
)
def issn(plats):
    df = data.copy()
    if len(plats) > 0:
        for i in plats:
            df = df[data['Platform'] == i]
    else:
        df = df
    #     df = data[data['Platform'] == platform]
    g_yes = len(
        df[df['Present on International Standard Serial Number (ISSN) portal'] == 1])
    g_no = len(
        df[df['Present on International Standard Serial Number (ISSN) portal'] == 0])
    if g_yes > 0:
        google_yes = round(g_yes / (g_yes + g_no) * 100, 2)
        google_no = round(g_no / (g_yes + g_no) * 100, 2)
        labels = ['Yes: {} ({:.2f}%)'.format(g_yes, google_yes),
                  'No: {} ({:.2f}%)'.format(g_no, google_no)]
        values = [google_yes, google_no]
        colors = ['#F3790C', '#A83B11']

        fig_pie = go.Figure(
            data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])
        # Set the desired font size here
        fig_pie.update_traces(textfont_size=20)
        fig_pie.update_layout(title="Journal Present on ISSN portal", template='seaborn',
                              margin=dict(l=20, r=20, t=30, b=20), height=400)
    else:

        # empty piechat
        fig_pie = go.Figure(
            data=[go.Pie(labels=[], values=[], marker=dict(colors=[]), hole=1)])
        fig_pie.update_layout(title="Journal Present on ISSN portal", template='seaborn',
                              margin=dict(l=20, r=20, t=30, b=20))

    return fig_pie

# DOAJ DONUT GRAPH *****************************************************************


@app.callback(
    Output('doaj-donut-chart', 'figure'),
    [Input('selected-platform-store', 'data')]
)
def doaj(plats):
    df = data.copy()
    if len(plats) > 0:
        for i in plats:
            df = df[data['Platform'] == i]
    else:
        df = df

    g_yes = len(
        df[df['Journal listed in the Directory of Open Access (DOAJ)'] == 1])
    g_no = len(
        df[df['Journal listed in the Directory of Open Access (DOAJ)'] == 0])

    if g_yes > 0:
        google_yes = round(g_yes / (g_yes + g_no) * 100, 2)
        google_no = round(g_no / (g_yes + g_no) * 100, 2)

        labels = ['Yes: {} ({:.2f}%)'.format(g_yes, google_yes),
                  'No: {} ({:.2f}%)'.format(g_no, google_no)]
        values = [google_yes, google_no]
        colors = ['#372261', '#B35A97']

        fig_donut = go.Figure(data=[
            go.Pie(labels=labels, values=values,
                   marker=dict(colors=colors), hole=0.5)
        ])

        # Set the desired font size here
        fig_donut.update_traces(textfont_size=20)
        fig_donut.update_layout(title="Journals listed in the Directory of Open Access (DOAJ)", template='seaborn',
                                margin=dict(l=20, r=20, t=30, b=20), height=400)
    else:
        # empty donut chart
        fig_donut = go.Figure(data=[
            go.Pie(labels=[], values=[], marker=dict(colors=[]), hole=0.7)
        ])

        fig_donut.update_layout(title="Listed in the Directory of Open Access (DOAJ)", template='seaborn',
                                margin=dict(l=20, r=20, t=30, b=20))

    return fig_donut


# Open Access Journal DONUT GRAPH *****************************************************************
@app.callback(
    Output('oaj-donut-chart', 'figure'),
    [Input('selected-platform-store', 'data')]
)
def oaj(plats):
    df = data.copy()
    if len(plats) > 0:
        for i in plats:
            df = df[data['Platform'] == i]
    else:
        df = df

    g_yes = len(
        df[df['Open Access Journal'] == 1])
    g_no = len(
        df[df['Open Access Journal'] == 0])

    if g_yes > 0:
        google_yes = round(g_yes / (g_yes + g_no) * 100, 2)
        google_no = round(g_no / (g_yes + g_no) * 100, 2)

        labels = ['Yes: {} ({:.2f}%)'.format(g_yes, google_yes),
                  'No: {} ({:.2f}%)'.format(g_no, google_no)]
        values = [google_yes, google_no]
        colors = ['#FF7E0C', '#9A1650']

        fig_donut = go.Figure(data=[
            go.Pie(labels=labels, values=values,
                   marker=dict(colors=colors), hole=0.5)
        ])

        # Set the desired font size here
        fig_donut.update_traces(textfont_size=20)
        fig_donut.update_layout(title="Open Access Journal", template='seaborn',
                                margin=dict(l=20, r=20, t=30, b=20), height=400)
    else:
        # empty donut chart
        fig_donut = go.Figure(data=[
            go.Pie(labels=[], values=[], marker=dict(colors=[]), hole=0.7)
        ])

        fig_donut.update_layout(title="Open Access Journal", template='seaborn',
                                margin=dict(l=20, r=20, t=30, b=20))

    return fig_donut


# The publisher is a member of Committee on publication Ethics (COPE) *****************************************************************
@app.callback(
    Output('cope-column-chart', 'figure'),
    [Input('selected-platform-store', 'data')]
)
def cope(plats):
    df = data.copy()
    if len(plats) > 0:
        for i in plats:
            df = df[df['Platform'] == i]
    else:
        df = df

    g_yes = len(
        df[df['The publisher is a member of Committee on publication Ethics (COPE)'] == 1])
    g_no = len(
        df[df['The publisher is a member of Committee on publication Ethics (COPE)'] == 0])
    dff = pd.DataFrame(data=[[g_yes, g_no]], columns=['YES', 'NO'])

    if g_yes > 0:
        colors = ['#A34571', '#602D8C']

        fig_bar = make_subplots(rows=1, cols=1)

        fig_bar.add_trace(
            go.Bar(y=dff.columns, x=dff.values[0], marker=dict(
                color=colors), text=dff.values[0], textposition='auto', orientation='h'),
            row=1, col=1
        )

        fig_bar.update_layout(
            template='seaborn',
            title='The publisher is a member of COPE',
            margin=dict(l=20, r=20, t=30, b=20),
            height=400
        )

        fig_bar.update_xaxes(title_text="Count")
        fig_bar.update_yaxes(title_text="The publisher is a member of COPE")

    else:
        fig_bar = go.Figure()

    return fig_bar


# THosted on INASP'S Journal online BAR GRAPH *****************************************************************
@app.callback(
    Output('inasp-bar-chart', 'figure'),
    [Input('selected-platform-store', 'data')],
)
def inasp(plats):
    df = data.copy()
    if len(plats) > 0:
        for i in plats:
            df = df[df['Platform'] == i]
    else:
        df = df

    g_yes = len(
        df[df['Hosted on INASP\'S Journal online'] == 1])
    g_no = len(
        df[df['Hosted on INASP\'S Journal online'] == 0])
    dff = pd.DataFrame(data=[[g_yes, g_no]], columns=['YES', 'NO'])

    if g_yes > 0:
        colors = ['#F3C702', '#AA2120']

        fig_bar = make_subplots(rows=1, cols=1)

        fig_bar.add_trace(
            go.Bar(y=dff.columns, x=dff.values[0], marker=dict(
                color=colors), text=dff.values[0], textposition='auto', orientation='h'),
            row=1, col=1
        )

        fig_bar.update_layout(
            template='seaborn',
            title='Hosted on INASP\'S Journal onlineE',
            margin=dict(l=20, r=20, t=30, b=20),
            height=200
        )

        fig_bar.update_xaxes(title_text="Count")
        fig_bar.update_yaxes(title_text="Hosted on INASP\'S Journal onlineE")

    else:
        fig_bar = go.Figure()

    return fig_bar


# ONE PLATFORM BAR GRAPH *****************************************************************


@app.callback(
    Output('oneplat-column-chart', 'figure'),
    [Input('selected-platform-store', 'data')]
)
def onePlatform(plats):
    df = data.copy()
    if len(plats) > 0:
        for i in plats:
            df = df[df['Platform'] == i]
    else:
        df = df

    g_yes = len(df[df['Indexed on at least one platform'] == 1])
    g_no = len(df[df['Indexed on at least one platform'] == 0])
    dff = pd.DataFrame(data=[[g_yes, g_no]], columns=['YES', 'NO'])

    if g_yes > 0:
        colors = ['#031A5E', '#FF7E0E']

        fig_bar = make_subplots(rows=1, cols=1)

        fig_bar.add_trace(
            go.Bar(y=dff.columns, x=dff.values[0], marker=dict(
                color=colors), text=dff.values[0], textposition='auto', orientation='h'),
            row=1, col=1
        )

        fig_bar.update_layout(
            template='seaborn',
            title='Journals Indexed on at least one platform',
            margin=dict(l=20, r=20, t=30, b=20),
            height=400
        )

        fig_bar.update_xaxes(title_text="Count")
        fig_bar.update_yaxes(title_text="Indexed on at least one platform")

    else:
        fig_bar = go.Figure()

    return fig_bar


# Online publisher based in Africa POLULATION GRAPH *****************************************************************
@app.callback(
    Output('basedinafrica-pop-chart', 'figure'),
    [Input('selected-platform-store', 'data')]
)
def publisherinAfrica(plats):
    df = data.copy()
    if len(plats) > 0:
        for i in plats:
            df = df[df['Platform'] == i]
    else:
        df = df

    g_yes = len(df[df['Online publisher based in Africa'] == 1])
    g_no = len(df[df['Online publisher based in Africa'] == 0])
    dat = [['YES', g_yes, 0], ['NO', g_no, 0]]
    dff = pd.DataFrame(data=dat, columns=[
                       'Online publisher based in Africa', 'Count', 'Online publisher based in Africa.'])
    if g_yes > 0:
        fig_bar = px.bar(dff, x='Online publisher based in Africa.', y='Count',
                         color='Online publisher based in Africa', title='', color_discrete_sequence=['green', 'red'], text='Count',)
        fig_bar.update_layout(xaxis=dict(showticklabels=False), height=400)
    else:
        fig_bar = go.Figure()

    return fig_bar


# DISPLAY OF JOURNALS ON A TABLE BASED ON THE CRITERIA SELETED *****************************************************************
@app.callback(
    Output('output', 'children'),
    [Input('selected-values-store', 'data')]
)
def display_selected_values(selected_values):
    if selected_values is not None:
        data_df = fil(selected_values)
        data_df['Number'] = range(1, len(data_df) + 1)
        num = len(data_df)

        # Swap the columns in the DataFrame
        data_df = data_df[['Number'] + list(data_df.columns[:-1])]

        data_table = dash_table.DataTable(
            id='data-table',
            columns=[{"name": col, "id": col} for col in data_df.columns],
            data=data_df.to_dict('records'),
            style_table={'font-family': 'sans-serif'},
            style_cell_conditional=[
                {'if': {'column_id': 'Date'}, 'textAlign': 'left'},
                {'if': {'column_id': 'Region'}, 'textAlign': 'left'}
            ],
            style_data={
                'color': 'black',
                'backgroundColor': 'white',
                'textAlign': 'left',
                'font-family': 'sans-serif',
            },
            style_data_conditional=[
                {'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(220, 220, 220)'}
            ],
            style_header={
                'backgroundColor': 'rgb(210, 210, 210)',
                'color': 'black',
                'fontWeight': 'bold',
                'textAlign': 'left',
                'font-family': 'sans-serif',
            }
        )

        return html.Div(data_table)
    else:
        return html.Div("No values selected")


if __name__ == '__main__':
    app.run_server(debug=False, port=8003)
