import unittest
from validation import *
from itin_examples import *

class TestDistanceValidation(unittest.TestCase):

    def test_validate_max_distance(self):
        self.assertTrue(validate_max_distance(itin1, [41.792210, -87.599940]))
        self.assertFalse(validate_max_distance(itin8, [41.792210, -87.599940]))
        self.assertTrue(validate_max_distance(itin8, [41.792210, -87.599940], 22))
        self.assertFalse(validate_max_distance(itin1, [41.792210, -87.599940], 7))

    def test_validate_event_distance(self):
        self.assertTrue(validate_event_distance(itin1))
        self.assertFalse(validate_event_distance(itin8))
        self.assertTrue(validate_max_distance(itin8, 20))
        self.assertFalse(validate_max_distance(itin1, 2))

    def test_validate_travel_time(self):
        self.assertFalse(validate_travel_time(itin1, "drive"))
        self.assertTrue(validate_travel_time(itin2, "drive"))
        self.assertFalse(validate_travel_time(itin3, "bike"))
        self.assertTrue(validate_travel_time(itin4, "bike"))
        self.assertFalse(validate_travel_time(itin4))
        self.assertTrue(validate_travel_time(itin5))
        self.assertFalse(validate_travel_time(itin6, "walk"))
        self.assertTrue(validate_travel_time(itin7, "walk"))
        self.assertFalse(validate_travel_time(itin11))

if __name__ == '__main__':
    unittest.main()
