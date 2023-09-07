import unittest

from src.examples.c_decisions.decisions import test_config, is_odd, is_vowel, is_consonant

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_is_odd(self):
        self.assertEqual(True, is_odd(1))
        self.assertEqual(False, is_odd(2))

    def test_is_vowel(self):
        self.assertEqual(True, is_vowel('a'))
        self.assertEqual(False, is_vowel('b'))

    def test_is_consonant(self):
        self.assertEqual(True, is_consonant('b'))
        self.assertEqual(False, is_consonant('a'))
