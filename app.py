import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State
from page_1 import page_1
from order_page import order_page
from page_3 import page_3
from navbar import navbar
from sidebar import sidebar, SIDEBAR_HIDDEN, SIDEBAR_STYLE
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from interactive_trader import *
from datetime import datetime
from ibapi.contract import Contract
from ibapi.order import Order
import time
import threading


CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

ibkr_async_conn = ibkr_app()

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        dcc.Store(id='side_click'),
        dcc.Location(id="url"),
        navbar,
        sidebar,
        html.Div(
            id="page-content",
            style=CONTENT_STYLE
        )
    ],
)

@app.callback(
    [
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),
    ],

    [Input("btn_sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDDEN
            content_style = CONTENT_STYLE1
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_STYLE
        content_style = CONTENT_STYLE
        cur_nclick = 'SHOW'

    return sidebar_style, content_style, cur_nclick

# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return page_1
    elif pathname == "/page-2":
        return order_page
    elif pathname == "/page-3":
        return page_3
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

@app.callback(Output('ibkr-async-conn-status', 'children'),
              Input('ibkr-async-conn-status', 'children'))
def async_handler(async_status):

    if async_status == "CONNECTED":
        raise PreventUpdate
        pass

    global ibkr_async_conn
    ibkr_async_conn.connect('127.0.0.1', 7497, 10645)

    timeout_sec = 5

    start_time = datetime.now()
    while not ibkr_async_conn.isConnected():
        time.sleep(0.01)
        if (datetime.now() - start_time).seconds > timeout_sec:
            ibkr_async_conn.disconnect()
            raise Exception(
                "set_up_async_connection",
                "timeout",
                "couldn't connect to IBKR"
            )

    def run_loop():
        ibkr_async_conn.run()

    api_thread = threading.Thread(target=run_loop, daemon=True)
    api_thread.start()

    while ibkr_async_conn.next_valid_id is None:
        time.sleep(0.01)

    return str(ibkr_async_conn.isConnected())

@app.callback(
    Output('placeholder-div', 'children'),
    Input('trade-button', 'n_clicks'),
    prevent_initial_call = True
)
def place_order(n_clicks):

    # Contract object: STOCK
    contract_stk = Contract()
    contract_stk.symbol = "TSLA"
    contract_stk.secType = "STK"
    contract_stk.currency = "USD"
    contract_stk.exchange = "SMART"
    contract_stk.primaryExchange = "ARCA"

    # Example LIMIT Order
    lmt_order = Order()
    lmt_order.action = "SELL"
    lmt_order.orderType = "LMT"
    lmt_order.totalQuantity = 100
    lmt_order.lmtPrice = 1105

    ##### FA Accounts #####
    # If you're a financial advisor (FA) then you're not finished creating your
    # orders at this point because you need to answer the question: which account
    # would you like to place the order on? All of them? Just one? Several? There
    # are a few ways to do this, for example, by using GROUPS: https://www.interactivebrokers.com/en/software/advisors/topics/accountgroups.htm
    # But probably the easiest way is to just pass in the ID of the account you
    # want to use, like this:
    lmt_order.account = 'DU1267861'
    # Don't want to mess this one up because your clients all signed up for
    # different strategies. You don't want to accidentally make trades for your
    # wild options strategy using the account owned by your conservative, careful
    # client who only trades index funds and dividend-paying stocks in the SP500!

    ibkr_async_conn.reqIds(1)

    # Place orders!
    ibkr_async_conn.placeOrder(
        ibkr_async_conn.next_valid_id,
        contract_stk,
        lmt_order
    )

    return ''

if __name__ == "__main__":
    app.run_server()