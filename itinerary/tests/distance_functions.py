
# check that each venue in the itinerary is within dist (in miles; optionally
# specified by the user) from the user's starting location
def validate_max_distance(itin, start_location, dist=10):
    return False

# check that each venue is within a reasonable distance of venues before
# and after it
# (dist is the same parameter as in the above function)
# this function ensures that venues in the itinerary are clustered to some
# extent, not just randomly spread out throughout the space defined by dist
def validate_event_distance(itin, dist=10):
    return False

# check that the time between each pair of adjacent events in the itinerary
# is sufficient for travel between their venues, given user's transportation mode
def validate_travel_time(itin, transport="drive"):
    return False
