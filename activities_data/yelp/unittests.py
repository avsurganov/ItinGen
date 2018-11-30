import unittest
from get_yelpdata import *

# SAMPLE DICTIONARIES FOR TESTING EVENT DICTS

# right number of fields
# right types in every field
sampledict1 = {
    "venue_id": "yelpXAh7Xce30KGmL_CTCdHAhg",
    "event_name": "Shedd Aquarium",
    "event_id": "yelpXAh7Xce30KGmL_CTCdHAhg",
    "mon_start": 540,
    "mon_end": 1020,
    "tues_start": 540,
    "tues_end": 1020,
    "wed_start": 540,
    "wed_end": 1020,
    "thurs_start": 540,
    "thurs_end": 1020,
    "fri_start": 540,
    "fri_end": 1020,
    "sat_start": 540,
    "sat_end": 1080,
    "sun_start": 540,
    "sun_end": 1080,
    "tags": [
        "aquariums"
    ],
    "price": -10
}

# right number of fields
# wrong types in every field
sampledict2 = {
    "venue_id": 75,
    "event_name": False,
    "event_id": 3.2,
    "mon_start": "hi",
    "mon_end": "hello",
    "tues_start": False,
    "tues_end": 17.5,
    "wed_start": -450.3,
    "wed_end": "hi",
    "thurs_start": 'howdy',
    "thurs_end": True,
    "fri_start": None,
    "fri_end": False,
    "sat_start": "saturday",
    "sat_end": "saturday",
    "sun_start": False,
    "sun_end": "bye",
    "tags": [
        7
    ],
    "price": False
}

# wrong number of fields
sampledict3 = {
    "venue_id": "yelpZuYoA_AdmeR0pSP1xBU3PA",
    "event_name": "Old Town Aquarium",
    "mon_start": 720,
    "mon_end": 1140,
    "tues_start": 720,
    "tues_end": 1200,
    "wed_start": 720,
    "wed_end": 1140,
    "thurs_start": 720,
    "thurs_end": 1200,
    "fri_start": 720,
    "fri_end": 1140,
    "sat_start": 660,
    "sat_end": 1080,
    "sun_start": 720,
    "sun_end": 1080,
    "tags": [
        "aquariumservices",
        "aquariums"
    ]
}



# SAMPLE DICTIONARIES FOR TESTING VENUE DICTS

#right number of fields
#right type in every field
sampledict15 = {
    "venue_id": "yelpRQmbLZvI7XyFQd2JgNDVig",
    "venue_name": "Lincoln Park Zoo",
    "latitude": 41.9209148287011,
    "longitude": -87.6336050034629,
    "address1": "2001 N Clark St",
    "address2": "",
    "address3": "",
    "city": "Chicago",
    "state": "IL",
    "zip_code": "60614"
}

#right number of fields
#wrong type in every field
sampledict16 = {
    "venue_id": False,
    "venue_name": 9,
    "latitude": "hi",
    "longitude": True,
    "address1": 17,
    "address2": 17,
    "address3": 17,
    "city": False,
    "state": 5.3,
    "zip_code": 60513
}

#right number of fields
#every coordinate out of range - upper
sampledict17 = {
    "venue_id": "yelpen_X257_3-Y6rL7hS9uaTQ",
    "venue_name": "Scales & Tales Traveling Zoo",
    "latitude": 95.85902,
    "longitude": 187.65358,
    "address1": "",
    "address2": "",
    "address3": "",
    "city": "Chicago",
    "state": "IL",
    "zip_code": "60608"
}

#right number of fields
#every coordinate out of range - lower
sampledict18 = {
    "venue_id": "yelpen_X257_3-Y6rL7hS9uaTQ",
    "venue_name": "Scales & Tales Traveling Zoo",
    "latitude": -95.85902,
    "longitude": -187.65358,
    "address1": "",
    "address2": "",
    "address3": "",
    "city": "Chicago",
    "state": "IL",
    "zip_code": "60608"
}

#wrong number of fields
sampledict19 = {
    "venue_id": "yelp9dSzFbsWrt0xxV1dAYLKmA",
    "venue_name": "Willowbrook Wildlife Center",
    "latitude": 41.84288,
    "longitude": -88.06033,
    "address1": "525 S Park Blvd",
    "address2": "",
    "address3": "",
    "city": "Glen Ellyn",
    "state": "IL",
}


class TestTimeConversion(unittest.TestCase):
    def test_converttime_yelp(self):
        self.assertEqual(converttime_yelp("0000"), 0)
        self.assertEqual(converttime_yelp("0200"), 120)
        self.assertEqual(converttime_yelp("0215"), 135)
        self.assertEqual(converttime_yelp("1000"), 600)
        self.assertEqual(converttime_yelp("2359"), 1439)
        self.assertEqual(converttime_yelp("2400"), 0)
        with self.assertRaises(Exception):
            converttime_yelp("0")
        with self.assertRaises(Exception):
            converttime_yelp("00")
        with self.assertRaises(Exception):
            converttime_yelp("000")
        with self.assertRaises(Exception):
            converttime_yelp("2500")
        with self.assertRaises(Exception):
            converttime_yelp("2401")

class TestVenueProperties(unittest.TestCase):
    def test_validate_venue_length(self):
        self.assertTrue(validate_venue_length(sampledict15))
        self.assertFalse(validate_venue_length(sampledict19))
    def test_validate_yelpID_venue(self):
        self.assertTrue(validate_yelpID_venue(sampledict15))
        self.assertFalse(validate_yelpID_venue(sampledict16))
    def test_validate_venue_name(self):
        self.assertTrue(validate_venue_name(sampledict15))
        self.assertFalse(validate_venue_name(sampledict16))
    def test_validate_coordinates(self):
        self.assertTrue(validate_coordinates(sampledict15))
        self.assertFalse(validate_coordinates(sampledict16))
        self.assertFalse(validate_coordinates(sampledict17))
        self.assertFalse(validate_coordinates(sampledict18))
    def test_validate_location(self):
        self.assertTrue(validate_location(sampledict15))
        self.assertFalse(validate_location(sampledict16))

class TestEventProperties(unittest.TestCase):
    def test_validate_event_length(self):
        self.assertTrue(validate_event_length(sampledict1))
        self.assertFalse(validate_event_length(sampledict3))
    def test_validate_yelpID_event(self):
        self.assertTrue(validate_yelpID_event(sampledict1))
        self.assertFalse(validate_yelpID_event(sampledict2))
        self.assertFalse(validate_yelpID_event(sampledict3))
    def test_validate_event_name(self):
        self.assertTrue(validate_event_name(sampledict1))
        self.assertFalse(validate_event_name(sampledict2))
    def test_validate_open_hour(self):
        self.assertTrue(validate_open_hour(sampledict1))
        self.assertFalse(validate_open_hour(sampledict2))
    def test_validate_close_hour(self):
        self.assertTrue(validate_close_hour(sampledict1))
        self.assertFalse(validate_close_hour(sampledict2))
    def test_validate_hours(self):
        self.assertTrue(validate_hours(sampledict1))
        self.assertFalse(validate_hours(sampledict2))
    def test_validate_tags(self):
        self.assertTrue(validate_tags(sampledict1))
        self.assertFalse(validate_tags(sampledict2))



if __name__ == '__main__':
    unittest.main()
