import unittest

from src.examples.e_functions.value_return_functions import test_config, is_number_odd, local_function_variable

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_is_number_odd(self):
        self.assertEqual(is_number_odd(3), True)

    def test_local_function_variable(self):
        self.assertEqual(local_function_variable(10), 100)