import unittest
from format_price import format_price, get_thousands


class FormattingPriceTestCase(unittest.TestCase):
    def test_get_thousands(self):
        got_list = get_thousands(123456789)
        check_list = [789, 456, 123]
        self.assertListEqual(check_list, check_list)


if __name__ == '__main__':
    unittest.main()