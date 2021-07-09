from src.factorial_finder import *

import unittest

class FactorialFinderTest(unittest.TestCase):
    def test_recur(self):
        self.assertEqual(factorial_recur(0), 1)
        self.assertEqual(factorial_recur(1), 1)
        self.assertEqual(factorial_recur(10), 3628800)

    def test_iter(self):
        self.assertEqual(factorial_iter(0), 1)
        self.assertEqual(factorial_iter(1), 1)
        self.assertEqual(factorial_iter(10), 3628800)

if __name__ == "__main__":
    unittest.main()