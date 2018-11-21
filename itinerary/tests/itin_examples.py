# this file contains example itineraries to run tests on
# itinerary structure:
# itin = [(event, venue, start, end),
#         (event, venue, start, end),
#         (event, venue, start, end),
#         (event, venue, start, end),
#         (event, venue, start, end),
#         ...]
# where each event is:
# {
#     "event_id": (str),
#     "event_name": (str),
#     "venue_id": (str),
#     "start": (int)(minutes),
#     "end": (int)(minutes),
#     "date": (str),
#     "tags": (list),
#     "price": (float)
# }
# OR
# {
#     event_id: string
#     event_name: string
#     venue_id: str
#     mon_start
#     mon_end
#     tues_start
#     tues_end
#     wed_start
#     wed_end
#     thurs_start
#     thurs_end
#     fri_start
#     fri_end
#     sat_start
#     sat_end
#     sun_start
#     sun_end
#     : ints (in minutes from midnight)
#     time_spent: int in minutes
#     tags: list of strings
#     price: float (dollars)
# }
# where each venue is:
# {
#     "venue_id": (str),
#     "venue_name": (str),
#     "latitude": (float),
#     "longitude": (float),
#     "address1": (string),
#     "address2": (string),
#     "address3": (string),
#     "city": (string),
#     "state": (string),
#     "zip_code": (string)
# }
# where each start is an int that represents minutes from midnight
# where each end is an int that represent minutes from midnight


######################
# manual itineraries #
######################

event1 = {
          "venue_id": "yelpAkcZ1fUyB3RocKLYGFu20Q",
          "event_name": "Art Institute of Chicago",
          "event_id": "yelpAkcZ1fUyB3RocKLYGFu20Q",
          "mon_start": 630,
          "mon_end": 1020,
          "tues_start": 630,
          "tues_end": 1020,
          "wed_start": 630,
          "wed_end": 1020,
          "thurs_start": 630,
          "thurs_end": 1200,
          "fri_start": 630,
          "fri_end": 1020,
          "sat_start": 630,
          "sat_end": 1020,
          "sun_start": 630,
          "sun_end": 1020,
          "tags": [
            "artschools",
            "landmarks",
            "artmuseums"
          ],
          "price": -10
         }

venue1 = {
          "venue_id": "yelpAkcZ1fUyB3RocKLYGFu20Q",
          "venue_name": "Art Institute of Chicago",
          "latitude": 41.8796,
          "longitude": -87.623713,
          "address1": "111 S Michigan Ave",
          "address2": "",
          "address3": "",
          "city": "Chicago",
          "state": "IL",
          "zip_code": "60603"
         }

event2 = {
          "venue_id": "yelp8sZZM3Dr0G46JYBT9h599A",
          "event_name": "International Museum of Surgical Science",
          "event_id": "yelp8sZZM3Dr0G46JYBT9h599A",
          "mon_start": 570,
          "mon_end": 1020,
          "tues_start": 570,
          "tues_end": 1020,
          "wed_start": 570,
          "wed_end": 1020,
          "thurs_start": 570,
          "thurs_end": 1020,
          "fri_start": 570,
          "fri_end": 1020,
          "sat_start": 600,
          "sat_end": 1020,
          "sun_start": 600,
          "sun_end": 1020,
          "tags": [
            "museums",
            "venues"
          ],
          "price": -10
         }

venue2 = {
          "venue_id": "yelp8sZZM3Dr0G46JYBT9h599A",
          "venue_name": "International Museum of Surgical Science",
          "latitude": 41.9102601910586,
          "longitude": -87.6266419992433,
          "address1": "1524 N Lake Shore Dr",
          "address2": "",
          "address3": "",
          "city": "Chicago",
          "state": "IL",
          "zip_code": "60610"
         }

event3 = {
          "event_id": "TMAPIvv1A7ZA8wGkdfoeXP",
          "event_name": "Elton John: Farewell Yellow Brick Road",
          "venue_id": "TMAPIKovZpa2MCe",
          "start": 1200,
          "end": -10,
          "date": "02-16-2019",
          "tags": [
            "Music",
            "Rock",
            "Pop",
            "Undefined",
            "Undefined"
          ],
          "price": 59.5
         }

venue3 = {
          "venue_id": "TMAPIKovZpa2MCe",
          "venue_name": "Allstate Arena",
          "latitude": 42.00499247,
          "longitude": -87.88750024,
          "address1": "6920 North Mannheim Road",
          "address2": "",
          "address3": "",
          "city": "Rosemont",
          "state": "IL",
          "zip_code": "60018"
}

# invalid travel time (driving)
itin1 = [(event1, venue1, 660, 780),
        (event2, venue2, 785, 920)]

# valid travel time (driving)
itin2 = [(event1, venue1, 660, 780),
        (event2, venue2, 790, 920)]

# invalid travel time (biking)
itin3 = [(event1, venue1, 660, 780),
        (event2, venue2, 795, 920)]

# valid travel time (biking)
# invalid travel time (transit)
itin4 = [(event1, venue1, 660, 780),
        (event2, venue2, 800, 920)]

# valid travel time (transit)
itin5 = [(event1, venue1, 660, 780),
        (event2, venue2, 810, 920)]

# invalid travel time (walking)
itin6 = [(event1, venue1, 660, 780),
        (event2, venue2, 820, 920)]

# valid travel time (walking)
itin7 = [(event1, venue1, 660, 780),
        (event2, venue2, 830, 920)]

# used to:
#   validate date
#   validate price
itin8 = [(event1, venue1, 660, 780),
        (event3, venue3, 830, 920)]

# duplicate events
itin9 = [(event1, venue1, 660, 780),
        (event1, venue1, 660, 780)]

# venue_id does not match
itin10 = [(event2, venue1, 660, 780)]

# invalid travel time overall 
itin11 = [(event2, venue2, 660, 780),
          (event1, venue1, 810, 830),
          (event3, venue3, 850, 900)]
