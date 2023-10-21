import unittest

from src.examples.g_lists_and_tuples.lists import get_list_return_value, get_list_total_for, get_list_total_while, list_reference_parameter, test_config

class Test_Config(unittest.TestCase):

    def test_config(self):
        self.assertEqual(test_config(), True)

    def test_get_total_w_while(self):
        list1 = [5, 10, 20]
        self.assertEqual(get_list_total_while(list1), 35)

    def test_get_list_total_for(self):
        list1 = [5, 10, 20]
        self.assertEqual(get_list_total_for(list1), 35)

    def test_list_ref_param_not_a_copy(self):
        list = [5, 10, 20]
        list_reference_parameter(list)

        self.assertEqual(list, [0, 10, 20])

    def test_list_return_value(self):
        list = [5, 10, 20]
        print("before", id(list))
        get_list_return_value(list)
        print("after", id(list))
        self.assertEqual(list, [0, 10, 20])