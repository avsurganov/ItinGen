

''' TIME VALIDATION FUNCTIONS '''

# checks that the times given for itin items don't overlap
def validate_nooverlap(itin, user_times=0):
    return False

# checks that itin items are in chronological order
def validate_chrono(itin):
    return False

# checks that times given for itin items are within event's open hours
def validate_isopen(itin, day):
    return False

# checks that itin items fall within specified user times
def validate_within_usertime(itin, user_times=0):
    return False


''' DISTANCE VALIDATION FUNCTIONS '''

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


''' EVENT VALIDATION FUNCTIONS '''

def validate_no_duplicates(itinerary):
    '''
    check that there are no duplicates in the itinerary

    inputs:
        itinerary (list of dicts)

    outputs:
        0 for success
        1 for failure
    '''
    ids = set()
    for event in itinerary:
        if event[0]['event_id'] in ids:
            return 1
        ids.add(event[0]['event_id'])

    return 0


def validate_venue_id_match(itinerary):
    '''
    check that the events and the venues have the same venue id

    inputs:
        itinerary (list of dicts)

    outputs:
        0 for success
        1 for failure
    '''
    for event in itinerary:
        if event[0]['venue_id'] != event[1]['venue_id']:
            return 1

    return 0


def validate_event_date(itinerary, date):
    '''
    check that the events in the itinerary are valid for the date that the
    user input/generated

    inputs:
        itinerary (list of dicts)
        date (str) - 'mm-dd-yyyy' (could potentially change date format later)

    outputs:
        0 for success
        1 for failure
    '''
    for event in itinerary:
        # only need to check date for one time events
        # permanent events checked by time
        if 'date' in event[0]:
            if date != event[0]['date']:
                return 1

    return 0


def validate_event_price(itinerary, price):
    '''
    check that the event price is below the user specified price

    inputs:
        itinerary (list of dicts)
        price (float)

    outputs:
        0 for success
        1 for failure
    '''
    for event in itinerary:
        p = event[0]['price']
        if p == -10:
            # there was no price, move on
            pass
        else:
            if p > price:
                return 1
            
    return 0
