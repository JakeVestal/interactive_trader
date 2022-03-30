
from ibapi.contract import Contract
from fintech_ibkr import *
import pandas as pd

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

# Get your contract details
cp_details = fetch_contract_details(contract_cp)
stk_details = fetch_contract_details(contract_stk)
crypto_details = fetch_contract_details(contract_crypto)

print(cp_details)
print(stk_details)
print(crypto_details)

# print more columns like this:
with pd.option_context('display.max_columns', None):
    print(stk_details)
