import unittest
from interactive_trader import fetch_matching_symbols
import pandas as pd

class fetch_matching_symbols_test_case(unittest.TestCase):

    def setUp(self):
        self.matching_symbols = fetch_matching_symbols('TSLA')

    def test_matching_symbols_is_dataframe(self):
        self.assertIsInstance(self.matching_symbols, pd.DataFrame)

    def test_matching_symbols_has_correct_columns(self):
        hd_colnames = self.matching_symbols.columns
        correct_colnames = ['con_id', 'symbol', 'sec_type', 'primary_exchange',
                            'currency']
        self.assertListEqual(list(hd_colnames), correct_colnames)

if __name__ == '__main__':
    unittest.main()