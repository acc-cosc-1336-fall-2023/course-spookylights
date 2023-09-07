import unittest

from src.examples.a_example.devprocess import add_numbers, get_remainder, operator_precedence_1, operator_precedence_2, square_value

class Test_Config(unittest.TestCase):

    def test_add_numbers_2(self):
        self.assertEqual(2, add_numbers(1, 1))

    def test_operator_precedence_1(self):
        self.assertEqual(14, operator_precedence_1(12, 6, 3))

    def test_operator_precedence_2(self):
        self.assertEqual(6, operator_precedence_2(12, 6, 3))
    
    def test_square_value(self):
        self.assertEqual(4, square_value(2))
        self.assertEqual(16, square_value(4))

    def test_get_remainder(self):
        self.assertEqual(0, get_remainder(2, 2))
        self.assertEqual(1, get_remainder(5, 2))