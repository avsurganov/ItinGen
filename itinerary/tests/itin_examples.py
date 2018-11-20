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
