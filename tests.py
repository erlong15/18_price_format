import unittest
from format_price import format_price, get_thousands


class FormattingPriceTestCase(unittest.TestCase):
    def test_get_thousands(self):
        got_list = get_thousands(123456789)
        check_list = [789, 456, 123]
        self.assertListEqual(check_list, check_list)

    def test_format_price(self):
        test_price = 12345678.123450
        test_format = "12 345 678.12"
        self.assertEqual(test_format, format_price(test_price))

    def test_format_incorrect_price(self):
        bad_prices = [
            '123O7.28',
            '123456.1234',
            -12343.01
            ]
        test_format = 'Цена уточняется'
        for test_price in bad_prices:
            self.assertEqual(test_format, format_price(test_price))


if __name__ == '__main__':
    unittest.main()