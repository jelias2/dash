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
available_countries = df.index.unique()
#available_countries = ['Vietnam','Panama',]

app.layout = html.Div([
    html.H1('Average Yearly Temperatures'),
    dcc.Dropdown(
        id='my-dropdown',
        # options=[
        #     {'label': 'Vietnam', 'value': 'Vietnam'},
        #     {'label': 'Panama', 'value': 'Panama'},
        #     {'label': 'Apple', 'value': 'AAPL'}
        options=[{'label':name, 'value':name} for name in available_countries
        ],
        value='Barbuda'
    ),
    dcc.Graph(id='my-graph')
])

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):

     df = pd.read_csv('populationbycountry19802010millions.csv')
     df.reset_index(inplace=True)
     df.set_index("country", inplace=True)
     odf = df[df.index == selected_dropdown_value]
     print( odf.drop(["index"], axis = 1).iloc[0,:])

     return {

        'data': [{
            'x': years,
            'y': df[df.index == selected_dropdown_value].drop(["index"], axis = 1).iloc[0,:]
            #'y': odf
        }],
        'layout':{
            'title': selected_dropdown_value,
            'xaxis':{
                'title':'Years'
            },
            'yaxis':{
                 'title':'Population in Millions'
            }
        }
    }

if __name__ == '__main__':
    logging.debug("Starting run_server")
    app.run_server(host='0.0.0.0',debug=True)
