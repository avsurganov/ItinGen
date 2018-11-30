import unittest
import sys


from pull_events import *
from helper_itin_examples import *
from algo_helpers import *
from user_input_examples import *
from itin_examples import *

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

'''
get_t_events and get_p_events are not tested because
they both required queries to the database that aren't
possible to simulate for testing purposes
'''









if __name__ == '__main__':
    unittest.main()
