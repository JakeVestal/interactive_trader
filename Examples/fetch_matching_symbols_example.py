
from fintech_ibkr import *

symbol = "TSLA"
matching_symbols = fetch_matching_symbols(symbol)

print(matching_symbols)
