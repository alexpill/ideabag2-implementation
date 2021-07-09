from src.happy_number import *

import unittest

class HappyNumberTest(unittest.TestCase):
    def test_happy(self):
        self.assertTrue(is_happy_number(1))
        self.assertTrue(is_happy_number(7))
        self.assertTrue(is_happy_number(10))
        self.assertTrue(is_happy_number(13))
        self.assertTrue(is_happy_number(19))
        self.assertFalse(is_happy_number(33))
        self.assertFalse(is_happy_number(30))
        self.assertFalse(is_happy_number(5))

    def test_8_first_happy(self):
        happies = eight_first_happy()
        self.assertEqual(happies, [1, 7, 10, 13, 19, 23, 28, 31])

if __name__ == "__main__":
    unittest.main()