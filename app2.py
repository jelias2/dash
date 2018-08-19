import dash
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import logging
#from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.Dash()

years=["1980","1981","1982","1983","1984","1985","1986","1987","1988","1989",'1990',"1991","1992","1993","1994","1995","1996","1997","1998","1999","2000",
"2001","2002","2003","2004","2005","2006","2007","2008","2009","2010"]

df = pd.read_csv('populationbycountry19802010millions.csv')
df.reset_index(inplace=True)
df.set_index("country", inplace=True)
#available_countries = df.index.unique()
available_countries = ['Vietnam']

app.layout = html.Div([
    html.H1('Average Yearly Temperatures'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Vietnam', 'value': 'Vietnam'},
            {'label': 'Barbuda', 'value': 'Barbuda'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='Vietnam'
    ),
    dcc.Graph(id='my-graph')
])

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    # df = web.DataReader(
    #     selected_dropdown_value, data_source='google',
    #     start=dt(2017, 1, 1), end=dt.now())
    return {
        'data': [{
            'x': years,
            'y': df[df.index == 'Vietnam'].drop(["index"], axis = 1).iloc[0,:]
        }]
    }

if __name__ == '__main__':
    logging.debug("Starting run_server")
    app.run_server(host='0.0.0.0',debug=True)
