import dash
import logging
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
#List of the years for population
years=["1980","1981","1982","1983","1984","1985","1986","1987","1988","1989",'1990',"1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003"
,"2004","2005","2006","2007","2008","2009","2010"]

#Read the CSV and format to index by data
df = pd.read_csv('populationbycountry19802010millions.csv')
df.reset_index(inplace=True)
df.set_index("country", inplace=True)
available_countries = df.index.unique()

#Set up the Div for the graph and dropdown menu
app.layout = html.Div([
    html.H1('Average Yearly Temperatures'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[{'label':name, 'value':name} for name in available_countries],
        value='Barbuda'
    ),
    dcc.Graph(id='my-graph')
])

#Update the graph anytime the value changes from the dropdown
@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):

     return {
        'data': [{
            'x': years,
            'y': df[df.index == selected_dropdown_value].drop(["index"], axis = 1).iloc[0,:]
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
