import unittest

from src.homework.j_classes.class_a import Die

class Test_Config(unittest.TestCase):

    def test_roll(self):
        die_values = range(1,7)
        die_roll = Die()
        self.assertIn(die_roll.get_rolled_value(), die_values)
        self.assertIn(die_roll.get_rolled_value(), die_values)
        self.assertIn(die_roll.get_rolled_value(), die_values)