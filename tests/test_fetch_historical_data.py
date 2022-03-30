import unittest
from ibapi.contract import Contract
from interactive_trader import fetch_historical_data
import pandas as pd

class fetch_historical_data_test_case(unittest.TestCase):

    def setUp(self):
        contract = Contract()
        contract.symbol = 'EUR'
        contract.secType = 'CASH'
        contract.exchange = 'IDEALPRO'  # 'IDEALPRO' is the currency exchange.
        contract.currency = 'USD'
        self.historical_data = fetch_historical_data(contract)

    def test_historical_data_is_dataframe(self):
        self.assertIsInstance(self.historical_data, pd.DataFrame)

    def test_historical_data_has_correct_columns(self):
        hd_colnames = self.historical_data.columns
        correct_colnames = ['date', 'open', 'high', 'low', 'close', 'volume',
                            'bar_count', 'average']
        self.assertListEqual(list(hd_colnames), correct_colnames)

if __name__ == '__main__':
    unittest.main()