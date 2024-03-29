'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DO NOT EDIT THIS FILE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
# tests/happy_test.py

import unittest
from unittest.mock import patch
from happy_hour import is_happy_hour

class TestHappyHour(unittest.TestCase):

    @patch('builtins.input', side_effect=['2022-12-25', '18:00'])
    def test_not_happy_hour_on_christmas(self, mock_input):
        self.assertFalse(is_happy_hour(mock_input(), mock_input()))

    @patch('builtins.input', side_effect=['2022-04-17', '17:30'])
    def test_not_happy_hour_on_easter(self, mock_input):
        self.assertFalse(is_happy_hour(mock_input(), mock_input()))

    @patch('builtins.input', side_effect=['2022-01-16', '16:45'])
    def test_not_happy_hour_on_sunday(self, mock_input):
        self.assertFalse(is_happy_hour(mock_input(), mock_input()))

    @patch('builtins.input', side_effect=['2022-01-10', '17:30'])
    def test_happy_hour_on_regular_day(self, mock_input):
        self.assertTrue(is_happy_hour(mock_input(), mock_input()))

    @patch('builtins.input', side_effect=['2022-01-10', '15:30'])
    def test_not_happy_hour_on_regular_day(self, mock_input):
        self.assertFalse(is_happy_hour(mock_input(), mock_input()))

if __name__ == '__main__':
    unittest.main()