import unittest
import sys
sys.path.append("..")

from pull_events import *
from helper_itin_examples import *

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
        self.assertTrue(check_meal_overlap_temp(event7))
        self.assertFalse(check_meal_overlap_temp(event3))
        self.assertFalse(check_meal_overlap_temp(event4))
        self.assertFalse(check_meal_overlap_temp(event5))
        self.assertFalse(check_meal_overlap_temp(event6))


class TestCostChecks(unittest.TestCase):
    def test_check_free(self):
        self.assertTrue(check_free(event7))
        self.assertTrue(check_free(event4))
        self.assertFalse(check_free(event3))
        self.assertFalse(check_free(event5))
        self.assertFalse(check_free(event6))










if __name__ == '__main__':
    unittest.main()
