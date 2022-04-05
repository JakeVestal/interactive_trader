
# This is an example of a test script.
# When you've correctly coded your 'historicalData' override method in
#  synchronous_functions.py, this script should return a dataframe that's
#  ready to be loaded into the candlestick graph constructor.

from ibapi.contract import Contract
from interactive_trader import *

value = "EUR.USD" # This is what your text input looks like on your app

# Create a contract object
contract = Contract()
contract.symbol = value.split(".")[0]
contract.secType  = 'CASH'
contract.exchange = 'IDEALPRO'  # 'IDEALPRO' is the currency exchange.
contract.currency = value.split(".")[1]

# Get your historical data
historical_data = fetch_historical_data(contract)

# Print it! This should be a dataframe that's ready to go.
print(historical_data)

# This script is an excellent place for scratch work as you figure this out.



