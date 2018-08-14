# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

years=["1980","1981","1982","1983","1984","1985","1986","1987","1988","1989",'1990',"1991","1992","1993","1994","1995","1996","1997","1998","1999","2000",
"2001","2002","2003","2004","2005","2006","2007","2008","2009","2010"]

df = pd.read_csv('populationbycountry19802010millions.csv')
df.reset_index(inplace=True)
df.set_index("country", inplace=True)
#available_countries = df.index.unique()
available_countries = ['Vietnam']


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': years, 'y': df[df.index == 'Vietnam'].iloc[0,:], 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
