import unittest
from interactive_trader import fetch_managed_accounts

class fetch_managed_accounts_test_case(unittest.TestCase):

    def setUp(self):
        self.managed_accounts = fetch_managed_accounts()

    def test_managed_accounts_is_list(self):
        self.assertIsInstance(self.managed_accounts, list)

    def test_managed_accounts_is_correct_format(self):
        results = [isinstance(x, str) for x in self.managed_accounts]
        self.assertTrue(all(results))

if __name__ == '__main__':
    unittest.main()