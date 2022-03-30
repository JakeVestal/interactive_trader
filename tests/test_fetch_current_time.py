import datetime
import unittest
from interactive_trader import fetch_current_time
from datetime import datetime

class fetch_current_time_test_case(unittest.TestCase):

    def setUp(self):
        self.current_time = fetch_current_time()

    def test_fetch_current_time(self):
        self.assertIsInstance(self.current_time, datetime)

if __name__ == '__main__':
    unittest.main()