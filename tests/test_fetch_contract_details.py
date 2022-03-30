import unittest
from interactive_trader import fetch_contract_details
from ibapi.contract import Contract
import pandas as pd

class fetch_contract_details_test_case(unittest.TestCase):

    def setUp(self):
        contract = Contract()
        contract.symbol = 'EUR'
        contract.secType = 'CASH'
        contract.exchange = 'IDEALPRO'
        contract.currency = 'USD'
        self.contract_details = fetch_contract_details(contract)

    def test_contract_details_is_dataframe(self):
        self.assertIsInstance(self.contract_details, pd.DataFrame)

    def test_contract_details_has_correct_columns(self):
        hd_colnames = self.contract_details.columns
        correct_colnames = ["con_id", "symbol", "long_name", "industry",
                            "category", "subcategory", "sec_type", "stock_type",
                            "exchange", "primary_exchange", "currency",
                            "local_symbol", "market_name", "min_tick",
                            "order_types", "valid_exchanges", "price_magnifier",
                            "time_zone_id", "trading_hours", "liquid_hours"]
        self.assertListEqual(list(hd_colnames), correct_colnames)

    def test_contract_details_has_only_one_row(self):
        self.assertEqual(self.contract_details.shape[0], 1)

if __name__ == '__main__':
    unittest.main()