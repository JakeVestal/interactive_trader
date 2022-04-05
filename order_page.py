from dash import html

page_2 = html.P("Page 2 content goes here")

from dash import Dash, dash_table
from dash.dependencies import Input, Output
import datetime

import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
df = df[['continent', 'country', 'pop', 'lifeExp']]  # prune columns for example
df['Mock Date'] = [
    datetime.datetime(2020, 1, 1, 0, 0, 0) + i * datetime.timedelta(hours=13)
    for i in range(len(df))
]

order_page = dash_table.DataTable(
    columns=[
        {'name': 'Continent', 'id': 'continent', 'type': 'numeric'},
        {'name': 'Country', 'id': 'country', 'type': 'text'},
        {'name': 'Population', 'id': 'pop', 'type': 'numeric'},
        {'name': 'Life Expectancy', 'id': 'lifeExp', 'type': 'numeric'},
        {'name': 'Mock Dates', 'id': 'Mock Date', 'type': 'datetime'}
    ],
    data=df.to_dict('records'),
    filter_action='native',
    id='trade-blotter'
)


