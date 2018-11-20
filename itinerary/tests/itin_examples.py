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

itin1 = [(event1, venue1, 660, 780),
        (event2, venue2, 820, 920)]
