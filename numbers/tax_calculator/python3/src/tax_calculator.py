#!/usr/bin/env python3

"""Ask for a price and a country and return the price after VAT taxes

Will ask the user for a price (any currency, it's just applying a certain
percentage) and returns the same price after applying the taxes of the country
also asked to the user.
"""

__author__ = "Alexandre Pilleyre"
__copyright__ = "Copyright 2021, Alexandre Pilleyre"
__credits__ = ["Alexandre Pilleyre", "mclintprojects"]
# mclintprojects for providing IdeaBag2 app

__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Alexandre Pilleyre"
__email__ = ""  # TODO: fill
__status__ = "Dev"

from .scrapping_extract_from_wikipedia import extract_taxes

class TaxCalculator:
    def __init__(self):
        self._taxes = extract_taxes()
        self._price = None
        self._country = None

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price_):
        if type(price_) is str:
            try:
                price_ = float(price_)
            except ValueError:
                print("Price must be a float")
                exit(1)
        self._price = price_

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        if country not in self._taxes:
            print("Not a valid country (or not in DB)")
            exit(1)
        elif type(self._taxes[country]) is not float:
            print("This country is tax free or the tax is unknown in DB")
        self._country = country

    def get_full_price(self):
        if self.country is None or self.price is None:
            print("Please provides both country and price")
        tax = self._taxes[self.country]
        if type(tax) is not float: tax = 0
        return self.price + self.price *  tax / 100


def main():
    calculator = TaxCalculator()
    calculator.country = input("Country: ")
    calculator.price = input("Price: ")
    print(f"Full price: {calculator.get_full_price()}")

if __name__ == "__main__":
    main()
