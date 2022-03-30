
from ibapi.contract import Contract
from ibapi.order import Order
from fintech_ibkr import *

hostname = '127.0.0.1'
port = 7497
client_id = 10645 # can set and use your Master Client ID

value = "EUR.USD" # This is what your text input looks like on your app

# Contract object: CURRENCY PAIR
contract_cp = Contract()
contract_cp.symbol = 'EUR'
contract_cp.secType  = 'CASH'
contract_cp.exchange = 'IDEALPRO'  # 'IDEALPRO' is the currency exchange.
contract_cp.currency = 'USD'

# Contract object: STOCK
contract_stk = Contract()
contract_stk.symbol = "TSLA"
contract_stk.secType = "STK"
contract_stk.currency = "USD"
contract_stk.exchange = "SMART"
contract_stk.primaryExchange = "ARCA"

# Contract object: CRYPTO
contract_crypto = Contract();
contract_crypto.symbol = "ETH"
contract_crypto.secType = "CRYPTO"
contract_crypto.currency = "USD"
contract_crypto.exchange = "PAXOS"

# Example MARKET Order
mkt_order = Order()
mkt_order.action = "BUY"
mkt_order.orderType = "MKT"
mkt_order.totalQuantity = 100

# Example LIMIT Order
lmt_order = Order()
lmt_order.action = "SELL"
lmt_order.orderType = "LMT"
lmt_order.totalQuantity = 100
lmt_order.lmtPrice = 1012

##### FA Accounts #####
# If you're a financial advisor (FA) then you're not finished creating your
# orders at this point because you need to answer the question: which account
# would you like to place the order on? All of them? Just one? Several? There
# are a few ways to do this, for example, by using GROUPS: https://www.interactivebrokers.com/en/software/advisors/topics/accountgroups.htm
# But probably the easiest way is to just pass in the ID of the account you
# want to use, like this:
mkt_order.account = 'DU1267861'
lmt_order.account = 'DU1267861'
# Don't want to mess this one up because your clients all signed up for
# different strategies. You don't want to accidentally make trades for your
# wild options strategy using the account owned by your conservative, careful
# client who only trades index funds and dividend-paying stocks in the SP500!

# Place orders!
order_response_stk_lmt = place_order(contract_stk, lmt_order)
order_response_cp_mkt = place_order(contract_cp, mkt_order)
order_response_crypto_mkt = place_order(contract_crypto, mkt_order)

# Print the info returned by placing orders:
print(order_response_stk_lmt)
print(order_response_crypto_mkt)
print(order_response_cp_mkt)

# You can select what you want from the response, for example:
print(order_response_cp_mkt['perm_id'])
