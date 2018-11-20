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
