import unittest

# convert time from military time (string) to minutes after midnight (int)
# returns an int
def converttime_yelp(milittime):
    return 0

# validate the length of the business dict
def validate_dictlength(bizdict):
    return False

# validate the name field of a dict
def validate_event_name(bizdict):
    if ('event_name' not in bizdict):
        return False
    name = bizdict['event_name']
    if (isinstance(name, str)):
        if (name.strip()):
            return True
    return False

def validate_venue_name(bizdict):
    if ('venue_name' not in bizdict):
        return False
    name = bizdict['venue_name']
    if (isinstance(name, str)):
        if (name.strip()):
            return True
    return False

# validate the opening time field of a dict
def validate_open_hour(bizdict):
    days = ['mon_start', 'tues_start', 'wed_start', 'thurs_start', 'fri_start',
        'sat_start', 'sun_start']
    for day in days:
        if (day not in bizdict):
            return False
        hour = bizdict[day]
        if (not isinstance(hour, int)):
            return False
        if (hour < 0 or hour > 1440):
            return False
    return True

# validate the closing time field of a dict
def validate_close_hour(bizdict):
    days = ['mon_end', 'tues_end', 'wed_end', 'thurs_end', 'fri_end',
        'sat_end', 'sun_end']
    for day in days:
        if (day not in bizdict):
            return False
        hour = bizdict[day]
        if (not isinstance(hour, int)):
            return False
        if (hour < 0 or hour > 1440):
            return False
    return True

# validate the relationship between the opening
# and closing hour fields of a dict
def validate_hours(bizdict):
    if (not validate_open_hour(bizdict) or not validate_close_hour(bizdict)):
        return False
    open_hours = ['mon_start', 'tues_start', 'wed_start', 'thurs_start', 'fri_start',
        'sat_start', 'sun_start']
    close_hours = ['mon_end', 'tues_end', 'wed_end', 'thurs_end', 'fri_end',
        'sat_end', 'sun_end']
    for day in range(7):
        start = open_hours[day]
        end = close_hours[day]
        if (start >= end):
            return False
    return True

# validate the category field of a dict
def validate_category(bizdict):
    if ('tags' not in bizdict):
        return False
    if (not isinstance('tags', list)):
        return False
    for tag in tags:
        if (not isinstance(tag, str)):
            return False
        if (not tag.strip()):
            return False
    return True

# validate the coordinates field of a business dict
def validate_coordinates(bizdict):
    return False

# validate the location field of a business dict
def validate_location(bizdict):
    return False

# validate the yelp-assigned ID of a business dict
def validate_yelpID(bizdict):
    return False

# SAMPLE DICTIONARIES FOR TESTING validate_dictlength

# right number of fields
sampledict = {
    "id": "WavvLdfdP6g8aZTtbBQHTw",
    "name": "Gary Danko",
    "hours": [
        {
            "hours_type": "REGULAR",
            "open": [
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 0,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 1,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 2,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 3,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 4,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 5,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 6,
                    "start": "1730"
                }
            ],
        "is_open_now": False
        }
    ],
    "categories": [
        {
            "alias": "newamerican",
            "title": "American (New)"
        }
    ],
    "coordinates": {
        "latitude": 37.80587,
        "longitude": -122.42058
    },
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "state": "CA",
        "zip_code": "94109",
        "country": "US",
        "display_address": [
            "800 N Point St",
            "San Francisco, CA 94109"
        ],
        "cross_streets": "Hyde St & Larkin St"
    },
}

# wrong number of fields
sampledict2 = {
    "id": "WavvLdfdP6g8aZTtbBQHTw",
    "name": "Gary Danko",
    "hours": [
        {
            "hours_type": "REGULAR",
            "open": [
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 0,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 1,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 2,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 3,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 4,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 5,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 6,
                    "start": "1730"
                }
            ],
        "is_open_now": False
        }
    ],
    "categories": [
        {
            "alias": "newamerican",
            "title": "American (New)"
        }
    ],
    "coordinates": {
        "latitude": 37.80587,
        "longitude": -122.42058
    },
}

# wrong number of fields
sampledict3 = {}

# wrong number of fields
sampledict4 = {
    "id": "WavvLdfdP6g8aZTtbBQHTw",
    "dummy_field": "dummy_value",
    "extra_dummy_field": "extra_dummy_value",
    "name": "Gary Danko",
    "hours": [
        {
            "hours_type": "REGULAR",
            "open": [
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 0,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 1,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 2,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 3,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 4,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 5,
                    "start": "1730"
                }
            ],
        "is_open_now": False
        }
    ],
    "categories": [
        {
            "alias": "newamerican",
            "title": "American (New)"
        }
    ],
    "coordinates": {
        "latitude": 37.80587,
        "longitude": -122.42058
    },
}



# VALIDATION SAMPLE DICTIONARIES: for validate_name, validate_open_hour,
# validate_close_hour, validate_category, validate_coordinates,
# validate_location, and validate_yelpID



# coord: missing latitude
# location: missing address line 1
# id: missing id
# name: missing name
# opening hour: missing
# closing hour: missing
sampledict5 = {
    "hours": [
        {
            "hours_type": "REGULAR",
            "open": [
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 0,
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 1,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 2,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "day": 3,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 4,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 5,
                    "start": "1730"
                }
            ],
        "is_open_now": False
        }
    ],
    "coordinates": {
        "longitude": -122.42058
    },
    "location": {
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "state": "CA",
        "zip_code": "94109",
        "country": "US",
    },
    "categories": [
        {'title': 'American (New)', 'alias': 'newamerican'},
        {'title': 'Bakeries', 'alias': 'bakeries'},
        {'title': 'Coffee & Tea', 'alias': 'coffee'}
    ]
}

# coord: missing longitude
# location: missing city
# id: wrong type
# name: wrong type
# opening hour: wrong type
# closing hour: wrong type
# category: wrong type
sampledict6 = {
    "hours": [
        {
            "hours_type": "REGULAR",
            "open": [
                {
                    "is_overnight": False,
                    "end": 18,
                    "day": 0,
                    "start": 2800,
                }
            ],
        "is_open_now": False
        }
    ],
    "name": 5,
    "coordinates": {
        "latitude": 37.80587,
    },
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "state": "CA",
        "zip_code": "94109",
        "country": "US",
    },
    "id": 17,
    "categories": [
        {'title': 5, 'alias': 'newamerican'},
        {'title': 'Bakeries', 'alias': 'bakeries'},
        {'title': 'Coffee & Tea', 'alias': 'coffee'}
    ]
}

# coord: latitiude out of range - upper
# location: missing state
# id: wrong type
# name: empty
# opening hour: wrong type
# ending hour: wrong type
# category: wrong type
sampledict7 = {
    "name": '',
    "hours": [
        {
            "hours_type": "REGULAR",
            "open": [
                {
                    "is_overnight": False,
                    "end": False,
                    "day": 0,
                    "start": True,
                }
            ],
        "is_open_now": False
        }
    ],
    "coordinates": {
        "latitude": 95.0,
        "longitude": -122.42058
    },
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "zip_code": "94109",
        "country": "US",
    },
    "id": 34.67,
    "categories": [
        {'title': 'American (New)', 'alias': False},
        {'title': 'Bakeries', 'alias': 'bakeries'},
        {'title': 'Coffee & Tea', 'alias': 'coffee'}
    ]
}

# coord: latitiude out of range - lower
# location: missing zip code
# id: wrong type
# name: wrong type
# opening hour: wrong type
# closing hour: wrong type
sampledict8 = {
    "name": True,
    "hours": [
        {
            "hours_type": "REGULAR",
            "open": [
                {
                    "is_overnight": False,
                    "end": 235.4,
                    "day": 0,
                    "start": 78.5,
                }
            ],
        "is_open_now": False
        }
    ],
    "coordinates": {
        "latitude": -100.5,
        "longitude": -122.42058
    },
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "state": "CA",
        "country": "US",
    },
    "id": True,
    "categories": [
        {'title': 'American (New)', 'alias': 'newamerican'},
        {'title': 37.5, 'alias': 'bakeries'},
        {'title': 'Coffee & Tea', 'alias': 'coffee'}
    ]
}

# coord: longitude out of range - lower
# location: missing county
# name: wrong type
# opening hour: out of range - upper
# closing hour: out of range - upper
# category: wrong type
sampledict9 = {
    "name": 54.7,
    "hours": [
        {
            "hours_type": "REGULAR",
            "open": [
                {
                    "is_overnight": False,
                    "end": "2401",
                    "day": 0,
                    "start": "2401",
                }
            ],
        "is_open_now": False
        }
    ],
    "coordinates": {
        "latitude": 37.805,
        "longitude": -186.7
    },
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "state": "CA",
        "zip_code": "94109",
    },
    "categories": [
        "restaurant",
        {'title': 'Bakeries', 'alias': 'bakeries'},
        {'title': 'Coffee & Tea', 'alias': 'coffee'}
    ]
}

# coord: longitude out of range - upper
# location: address 1 wrong type
# opening hour: out of range - lower
# closing hour: out of range - lower
# category: empty
sampledict10 = {
    "hours": [
        {
            "hours_type": "REGULAR",
            "open": [
                {
                    "is_overnight": False,
                    "end": "000",
                    "day": 0,
                    "start": "000",
                }
            ],
        "is_open_now": False
        }
    ],
    "coordinates": {
        "latitude": 37.805,
        "longitude": 194.25
    },
    "location": {
        "address1": 7,
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "state": "CA",
        "zip_code": "94109",
        "country": "US",
    },
    "categories": [],
}

# coord: latitude wrong type
# location: city wrong type
# category: missing category
sampledict11 = {
    "hours": [
        {
            "hours_type": "REGULAR",
            "open": [
                {
                    "is_overnight": False,
                    "end": "1730",
                    "day": 0,
                    "start": "1720",
                }
            ],
        "is_open_now": False
        }
    ],
    "coordinates": {
        "latitude": "a",
        "longitude": -122.42058
    },
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": 54,
        "state": "CA",
        "zip_code": "94109",
        "country": "US",
    },
}

# coord: longitude wrong type
# location: state wrong type
# hours: start and end at the same time
sampledict12 = {
    "coordinates": {
        "latitude": 37.805,
        "longitude": False
    },
    "hours": [
        {
            "hours_type": "REGULAR",
            "open": [
                {
                    "is_overnight": False,
                    "end": "1720",
                    "day": 0,
                    "start": "1720",
                }
            ],
        "is_open_now": False
        }
    ],
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "state": False,
        "zip_code": "94109",
        "country": "US",
    },
}

# location: zip code wrong type
# hours: end before start
sampledict13 = {
    "hours": [
        {
            "hours_type": "REGULAR",
            "open": [
                {
                    "is_overnight": False,
                    "end": "1000",
                    "day": 0,
                    "start": "1720",
                }
            ],
        "is_open_now": False
        }
    ],
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "state": "CA",
        "zip_code": 94109,
        "country": "US",
    },
}

# location: country wrong type
sampledict14 = {
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "state": "CA",
        "zip_code": "94109",
        "country": 3.5,
    },
}


class TestTimeConversion(unittest.TestCase):
    def test_converttime_yelp(self):
        self.assertEqual(converttime_yelp("0000"), 0)
        self.assertEqual(converttime_yelp("0200"), 120)
        self.assertEqual(converttime_yelp("0215"), 135)
        self.assertEqual(converttime_yelp("1000"), 600)
        self.assertEqual(converttime_yelp("2359"), 1439)
        self.assertEqual(converttime_yelp("2400"), 0)
        with self.assertRaises(TypeError):
            converttime_yelp("0")
        with self.assertRaises(TypeError):
            converttime_yelp("00")
        with self.assertRaises(TypeError):
            converttime_yelp("000")
        with self.assertRaises(TypeError):
            converttime_yelp("2500")
        with self.assertRaises(TypeError):
            converttime_yelp("2401")

class TestDictProperties(unittest.TestCase):
    def test_validate_dictlength(self):
        self.assertTrue(validate_dictlength(sampledict))
        self.assertFalse(validate_dictlength(sampledict2))
        self.assertFalse(validate_dictlength(sampledict3))
        self.assertFalse(validate_dictlength(sampledict4))

class TestBizProperties(unittest.TestCase):
    def test_validate_name(self):
        self.assertTrue(validate_name(sampledict))
        self.assertFalse(validate_name(sampledict5))
        self.assertFalse(validate_name(sampledict6))
        self.assertFalse(validate_name(sampledict7))
        self.assertFalse(validate_name(sampledict8))
        self.assertFalse(validate_name(sampledict9))
    def test_validate_open_hour(self):
        self.assertTrue(validate_open_hour(sampledict))
        self.assertTrue(validate_open_hour(sampledict4))
        self.assertFalse(validate_open_hour(sampledict5))
        self.assertFalse(validate_open_hour(sampledict6))
        self.assertFalse(validate_open_hour(sampledict7))
        self.assertFalse(validate_open_hour(sampledict8))
        self.assertFalse(validate_open_hour(sampledict9))
        self.assertFalse(validate_open_hour(sampledict10))
    def test_validate_close_hour(self):
        self.assertTrue(validate_close_hour(sampledict))
        self.assertTrue(validate_close_hour(sampledict4))
        self.assertFalse(validate_close_hour(sampledict5))
        self.assertFalse(validate_close_hour(sampledict6))
        self.assertFalse(validate_close_hour(sampledict7))
        self.assertFalse(validate_close_hour(sampledict8))
        self.assertFalse(validate_close_hour(sampledict9))
        self.assertFalse(validate_close_hour(sampledict10))
    def test_validate_hours(self):
        self.assertTrue(validate_hours(sampledict11))
        self.assertTrue(validate_hours(sampledict4))
        self.assertFalse(validate_hours(sampledict5))
        self.assertFalse(validate_hours(sampledict6))
        self.assertFalse(validate_hours(sampledict7))
        self.assertFalse(validate_hours(sampledict8))
        self.assertFalse(validate_hours(sampledict9))
        self.assertFalse(validate_hours(sampledict10))
        self.assertFalse(validate_hours(sampledict12))
        self.assertFalse(validate_hours(sampledict13))
    def test_validate_category(self):
        self.assertTrue(validate_category(sampledict5))
        self.assertFalse(validate_category(sampledict6))
        self.assertFalse(validate_category(sampledict7))
        self.assertFalse(validate_category(sampledict8))
        self.assertFalse(validate_category(sampledict9))
        self.assertFalse(validate_category(sampledict10))
        self.assertFalse(validate_category(sampledict11))
    def test_validate_coordinates(self):
        self.assertFalse(validate_coordinates(sampledict3))
        self.assertFalse(validate_coordinates(sampledict5))
        self.assertFalse(validate_coordinates(sampledict6))
        self.assertFalse(validate_coordinates(sampledict7))
        self.assertFalse(validate_coordinates(sampledict8))
        self.assertFalse(validate_coordinates(sampledict9))
        self.assertFalse(validate_coordinates(sampledict10))
        self.assertFalse(validate_coordinates(sampledict11))
        self.assertFalse(validate_coordinates(sampledict12))
        self.assertTrue(validate_coordinates(sampledict))
    def test_validate_location(self):
        self.assertFalse(validate_location(sampledict5))
        self.assertFalse(validate_location(sampledict6))
        self.assertFalse(validate_location(sampledict7))
        self.assertFalse(validate_location(sampledict8))
        self.assertFalse(validate_location(sampledict9))
        self.assertFalse(validate_location(sampledict10))
        self.assertFalse(validate_location(sampledict11))
        self.assertFalse(validate_location(sampledict12))
        self.assertFalse(validate_location(sampledict13))
        self.assertFalse(validate_location(sampledict14))
        self.assertTrue(validate_location(sampledict))
    def test_validate_yelpID(self):
        self.assertFalse(validate_yelpID(sampledict5))
        self.assertFalse(validate_yelpID(sampledict6))
        self.assertFalse(validate_yelpID(sampledict7))
        self.assertFalse(validate_yelpID(sampledict8))
        self.assertTrue(validate_yelpID(sampledict))


if __name__ == '__main__':
    unittest.main()
