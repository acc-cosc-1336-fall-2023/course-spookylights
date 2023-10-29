import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget, widget_inv

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        Widget1 = 'widget1'
        quantity = 10
        self.assertEqual(add_inventory(Widget1,quantity), {'widget1': 10})
        quantity = 25
        self.assertEqual(add_inventory(Widget1, quantity), {'widget1':35})
        quantity = -10
        self.assertEqual(add_inventory(Widget1, quantity), {'widget1':25})

    def test_remove_inventory_widget(self):
        widget1 = 'widget1'
        widget2 = 'widget2'
        quantity1 = 10
        quantity2 = 5
        add_inventory(widget1, quantity1)
        add_inventory(widget2, quantity2)
        remove_inventory_widget(widget1)
        self.assertEqual(len(widget_inv), 1)
        self.assertIn('widget2', widget_inv)


