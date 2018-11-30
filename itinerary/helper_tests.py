import unittest
import sys

from pull_events import *
from helper_itin_examples import *

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

# not written because these functions check that the date in the event
# matches "today" - so tests written today will fail tomorrow
# we've confirmed from running it that these functions do their job,
# but because the functions call a library that gets the actual current
# date, running them at a later time would make it fail
# (and theres no way to conveniently take the date out of the functions
# given how we use them)
#class TestPermEventChecks(unittest.TestCase):
    #def test_time_date_check_perm(self):

class TestTempEventChecks(unittest.TestCase):
    #def test_time_check_temp(self):
    #def test_date_check_temp(self)
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

'''
get_t_events and get_p_events are not tested because
they both required queries to the database that aren't
possible to simulate for testing purposes
'''









if __name__ == '__main__':
    unittest.main()
