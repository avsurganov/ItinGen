import unittest
from validation import *
from itin_examples import *

class TestDistanceValidation(unittest.TestCase):
    def test_validate_distance(self):
        self.assertTrue(validate_distance(itin1))
        self.assertFalse(validate_distance(itin8))
        self.assertTrue(validate_distance(itin1, 2.5))
        self.assertFalse(validate_distance(itin1, 2))
    def test_validate_travel_time(self):
        self.assertFalse(validate_travel_time(itin1))
        self.assertTrue(validate_travel_time(itin2))
        self.assertFalse(validate_travel_time(itin3, "bike"))
        self.assertTrue(validate_travel_time(itin4, "bike"))
        self.assertFalse(validate_travel_time(itin4, "transit"))
        self.assertTrue(validate_travel_time(itin5, "transit"))
        self.assertFalse(validate_travel_time(itin6, "walk"))
        self.assertTrue(validate_travel_time(itin7, "walk"))

if __name__ == '__main__':
    unittest.main()
