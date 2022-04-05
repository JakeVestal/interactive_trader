from dash import dash_table
import pandas as pd

errors = pd.DataFrame(columns=['reqId', 'errorCode', 'errorString'])

error_page = dash_table.DataTable(
    columns=[{"name": i, "id": i} for i in errors.columns],
    data=errors.to_dict('records'),
    id='errors-dt'
)
