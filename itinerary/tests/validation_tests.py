import unittest
from validation import *
from itin_examples import *

class TestTimeValidation(unittest.TestCase):
    def test_validate_nooverlap(self):
        self.assertTrue(validate_nooverlap(itin1))
        self.assertFalse(validate_nooverlap(itin12))
        self.assertFalse(validate_nooverlap(itin13))
        self.assertFalse(validate_nooverlap(itin14))
        self.assertFalse(validate_nooverlap(itin9))

    def test_validate_chrono(self):
        self.assertTrue(validate_chrono(itin1))
        self.assertTrue(validate_chrono(itin10))
        self.assertTrue(validate_chrono(itin12))
        self.assertTrue(validate_chrono(itin13))
        self.assertFalse(validate_chrono(itin9))
        self.assertFalse(validate_chrono(itin14))

    def test_validate_isopen(self):
        self.assertTrue(validate_isopen(itin1,"mon"))
        self.assertTrue(validate_isopen(itin1,"tues"))
        self.assertTrue(validate_isopen(itin1,"wed"))
        self.assertTrue(validate_isopen(itin1,"thurs"))
        self.assertTrue(validate_isopen(itin1,"fri"))
        self.assertTrue(validate_isopen(itin1,"sat"))
        self.assertTrue(validate_isopen(itin1,"sun"))
        self.assertFalse(validate_isopen(itin15,"mon"))
        self.assertFalse(validate_isopen(itin15,"tues"))
        self.assertFalse(validate_isopen(itin15,"wed"))
        self.assertFalse(validate_isopen(itin15,"thurs"))
        self.assertFalse(validate_isopen(itin15,"fri"))
        self.assertFalse(validate_isopen(itin15,"sat"))
        self.assertFalse(validate_isopen(itin15,"sun"))

    def test_validate_within_usertime(self):
        self.assertFalse(validate_within_usertime(itin1,[800,1000]))
        self.assertFalse(validate_within_usertime(itin1,[630,850]))
        self.assertTrue(validate_within_usertime(itin1,[600,950]))

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

class TestEventValidation(unittest.TestCase):
    def test_validate_no_duplicates(self):
        self.assertEqual(validate_no_duplicates(itin9),1)
        self.assertFalse(validate_no_duplicates(itin10))

    def test_validate_venue_id_match(self):
        self.assertTrue(validate_venue_id_match(itin10))
        self.assertFalse(validate_venue_id_match(itin8))

    def test_validate_event_date(self):
        self.assertTrue(validate_event_date(itin8, '02-16-2018'))
        self.assertFalse(validate_event_date(itin8, '02-16-2019'))

    def test_validate_event_price(self):
        self.assertTrue(validate_event_price(itin8, 0))
        self.assertFalse(validate_event_price(itin8, 100000))

class TestItinValidation(unittest.TestCase):
    def test_validate_itin(self):
        self.assertTrue(validate_itin(itin1,"mon",[41.792210, -87.599940],"11-20-2018",0.0))
        self.assertEqual(validate_itin(itin1,"tue",[41.792210, -87.599940],"02-16-2019",0.0),1)
        self.assertEqual(validate_itin(itin10,"tue",[41.792210, -87.599940],"02-16-2019",0.0),1)
        self.assertEqual(validate_itin(itin1,"tue",[41.792210, -87.599940],"02-16-2018",0.0),1)
        self.assertEqual(validate_itin(itin8,"tue",[41.792210, -87.599940],"02-16-2019",0.0),0)



if __name__ == '__main__':
    unittest.main()
