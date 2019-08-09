import decimal
import unittest

from parameterized import parameterized

from src.shop.rounding import round_value


class TestRounding(unittest.TestCase):
    @parameterized.expand(
        [
            (decimal.Decimal("0.12345"), 2, decimal.ROUND_DOWN, decimal.Decimal("0.12")),
            (decimal.Decimal("0.12345"), 2, decimal.ROUND_UP, decimal.Decimal("0.13")),
            (decimal.Decimal("0.12345"), 4, decimal.ROUND_DOWN, decimal.Decimal("0.1234")),
            (decimal.Decimal("0.12345"), 4, decimal.ROUND_UP, decimal.Decimal("0.1235")),
            (decimal.Decimal("0.12345"), 6, decimal.ROUND_DOWN, decimal.Decimal("0.123450")),
            (decimal.Decimal("0.12345"), 6, decimal.ROUND_UP, decimal.Decimal("0.123450")),
        ]
    )
    def test_should_round_value_successfully(self, input_value, precision, rounding, expected_rounded_value):
        actual_rounded_value = round_value(input_value, precision, rounding)

        self.assertEqual(actual_rounded_value, expected_rounded_value)


if __name__ == "__main__":
    unittest.main()
