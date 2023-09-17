import unittest

from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

class Test_Config(unittest.TestCase):

    def test_get_options_ratio(self):
        self.assertEqual(.25, get_options_ratio(5, 20))
        self.assertEqual(.5, get_options_ratio(10, 20))

    def test_get_faculty_rating(self):
        self.assertEqual("Excellent", get_faculty_rating(.91))
        self.assertEqual("Very Good", get_faculty_rating(.85))
        self.assertEqual("Good", get_faculty_rating(.71))
        self.assertEqual("Needs Improvement", get_faculty_rating(.66))
        self.assertEqual("Unacceptable", get_faculty_rating(.45))