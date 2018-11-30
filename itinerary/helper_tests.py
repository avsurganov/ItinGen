import unittest
import sys


from pull_events import *
from helper_itin_examples import *
from algo_helpers import *
from user_input_examples import *
from itin_examples import *

'''
Functions that aren't tested and why:
    - time and date checking functions for temp and perm events
      because they check the date against today's actual date
      so tests written today would fail tomorrow. We have validated
      that they do work based on the itineraries we have generated
    - get_t_events and get_p_events because they both required
      queries to the database that aren't possible to simulate
      for testing purposes
'''

class TestDayConversion(unittest.TestCase):
    def test_day_to_str(self):
        self.assertEqual(day_to_str(0),"mon")
        self.assertEqual(day_to_str(1),"tues")
        self.assertEqual(day_to_str(2),"wed")
        self.assertEqual(day_to_str(3),"thurs")
        self.assertEqual(day_to_str(4),"fri")
        self.assertEqual(day_to_str(5),"sat")
        self.assertEqual(day_to_str(6),"sun")
        self.assertNotEqual(day_to_str(0),"tues")
        self.assertNotEqual(day_to_str(4),"mon")
        self.assertNotEqual(day_to_str(6),"thurs")

class TestTempEventChecks(unittest.TestCase):
    def test_check_meal_overlap_temp(self):
        self.assertTrue(check_meal_overlap_temp(evente))
        self.assertFalse(check_meal_overlap_temp(eventa))
        self.assertFalse(check_meal_overlap_temp(eventb))
        self.assertFalse(check_meal_overlap_temp(eventc))
        self.assertFalse(check_meal_overlap_temp(eventd))


class TestCostChecks(unittest.TestCase):
    def test_check_free(self):
        self.assertTrue(check_free(evente))
        self.assertTrue(check_free(eventb))
        self.assertFalse(check_free(eventa))
        self.assertFalse(check_free(eventc))
        self.assertFalse(check_free(eventd))


class TestAlgoHelpers(unittest.TestCase):
    def test_check_valid(self):
        self.assertFalse(check_valid((event1, venue1, 480, 580), itin7, user_data1))

    def test_check_finished(self):
        self.assertFalse(check_finished([]))
        self.assertTrue(check_finished(itin18))

    def test_validate_restaurant(self):
        self.assertFalse(validate_restaurant(event3, 720))
        self.assertTrue(validate_restaurant(event4, 720))

    def test_double_count(self):
        self.assertTrue(check_double_count(event1, itin1))
        self.assertFalse(check_double_count(event3, itin1))









if __name__ == '__main__':
    unittest.main()
