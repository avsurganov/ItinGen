import math
import sys
sys.path.insert(0, '../')
from algo_helpers import *

''' TIME VALIDATION FUNCTIONS '''

# checks that the times given for itin items don't overlap
def validate_nooverlap(itin, user_start_time):
    if itin[0][2] < user_start_time:
        return False
    for i in range(len(itin)-1):
        # check if end time of event a is after start time of event a+1
        # for itin of format [(ev1,venue1,starttime, endtime), (ev2,venue2,starttime endtime) ... ]
        if itin[i][3] > itin[i+1][2]:
            return False
    return True


# checks that itin items are in chronological order
def validate_chrono(itin):
    for i in range(len(itin)-1):
        if itin[i][2] >= itin[i+1][2]:
            return False
    return True

# checks that times given for itin items are within event's open hours
def validate_isopen(itin, day):
    for i in range(len(itin)):
        event = itin[i][0]
        if "start" in event:
            starthours = 'start'
            endhours = 'end'
        else:
            starthours = str(day) + '_start'
            endhours = str(day) + '_end'
        if itin[i][2] < event[starthours] and event[starthours] != -10:
            return False
        if itin[i][3] > event[endhours] and event[endhours] != -10:
            return False
    return True

# the functionality here has been absorbed into the check_overlap function
# checks that itin items fall within specified user times
#def validate_within_usertime(itin, user_times=0):
#    return False


''' DISTANCE VALIDATION FUNCTIONS '''

# check that each venue in the itinerary is within dist (in miles; optionally
# specified by the user) from the user's starting location
def validate_max_distance(itin, start_location, dist):
    for venue in itin:
        venue_coord = venue_to_lat_long(venue[1])
        distance = find_distance(start_location, venue_coord)
        if distance > dist:
            return False
    return True

# check that each venue is within a reasonable distance of venues before
# and after it
# (dist is the same parameter as in the above function)
# this function ensures that venues in the itinerary are clustered to some
# extent, not just randomly spread out throughout the space defined by dist
def validate_event_distance(itin, dist):
    for i in range(len(itin)-1):
        prev_venue_coord = venue_to_lat_long(itin[i][1])
        next_venue_coord = venue_to_lat_long(itin[i+1][1])
        distance = find_distance(prev_venue_coord, next_venue_coord)
        if distance > dist * math.sqrt(2):
            return False
    return True

# check that the time between each pair of adjacent events in the itinerary
# is sufficient for travel between their venues, given user's transportation mode
def validate_travel_time(itin, transport):
    for i in range(len(itin)-1):
        prev_venue = itin[i][1]
        prev_end_time = itin[i][3]
        next_venue = itin[i+1][1]
        next_start_time = itin[i+1][2]
        between_time = next_start_time - prev_end_time
        distance = find_distance(venue_to_lat_long(prev_venue),venue_to_lat_long(next_venue))
        if (transport == "driving"):
            travel_time = distance * 2
        elif (transport == "transit"):
            travel_time = distance * 8
        else:
            travel_time = distance * 20
        if between_time < travel_time:
            return False
    return True


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


''' OVERALL VALIDATION FUNCTIONS '''

def validate_free(itin):
    for item in itin:
        if item[0]["price"] != -10:
            return False
    return True

def validate_types(itin):
    for item in itin:
        ev = item[0]
        ven = item[1]
        st = item[2]
        et = item[3]
        if not (isinstance(ev,dict)):
            return False
        if not (isinstance(ven,dict)):
            return False
        if not (isinstance(st,int)):
            return False
        if not (isinstance(et,int)):
            return False
    return True

# wrapper for all of the above validation functions
# also checks that every element in the itinerary is the right type
def validate_itin(itin,user_inputs):

    user_times = user_inputs['start_time']
    start_location = user_inputs['start_location']
    dist = user_inputs['distance_radius']
    transport = user_inputs['transportation']
    day = user_inputs['day']
    date = user_inputs['date']
    free = user_inputs['only_free']

    istypes = validate_types(itin)
    if not istypes:
        return False
    isvalid =  (validate_nooverlap(itin,user_times) and
                    validate_chrono(itin) and
                    validate_isopen(itin,day) and
                    validate_max_distance(itin,start_location,dist) and
                    validate_event_distance(itin,dist) and
                    validate_travel_time(itin,transport) and
                    not validate_no_duplicates(itin) and
                    not validate_venue_id_match(itin) and
                    not validate_event_date(itin,date))

    isfree = not free or validate_free(itin)
    return isvalid and isfree
