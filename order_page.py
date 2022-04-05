from dash import dash_table
import datetime
import pandas as pd

blotter = pd.DataFrame(
    columns=['order_id', 'perm_id', 'status', 'filled', 'remaining',
             'avg_fill_price', 'parent_id', 'last_fill_price',
             'client_id', 'why_held', 'mkt_cap_price']
)

order_page = dash_table.DataTable(
    columns=[{"name": i, "id": i} for i in blotter.columns],
    data=blotter.to_dict('records'),
    id='trade-blotter'
)


