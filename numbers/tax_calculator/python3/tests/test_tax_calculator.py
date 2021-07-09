from src.tax_calculator import *
import unittest

class TaxCalculatorTest(unittest.TestCase):
    def test_tax(self):
        country = "France"
        price = 100
        calculator = TaxCalculator()
        calculator.price = price
        calculator.country = country
        self.assertEqual(calculator.get_full_price(), 120)

    # TODO: test wrong country
    # TODO: test wrong float

if __name__ == '__main__':
    unittest.main()
