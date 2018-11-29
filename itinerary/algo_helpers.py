import random
from math import sin, cos, sqrt, atan2, radians, acos, fabs, pi
from operator import itemgetter
import googlemaps

############################
# PRIMARY HELPER FUNCTIONS #
############################

def increment_itinerary(itinerary, valid_events, user_data):
    '''
    given an itinerary and a list of events try to add on another event to the
    itinerary
    '''
    # if there is nothing just return immediately
    if len(valid_events) == 0:
        return
    # check events in random order
    indices = [i for i in range(len(valid_events))]
    random.shuffle(indices)
    # iterate through the events by index
    for index in indices:
        cur_event = valid_events[index]
        if check_valid(cur_event, itinerary, user_data):
            # done with this increment
            return


def check_valid(cur_event, itinerary, user_data):
    '''
    this functions tests if it is ok to add the event into the itinerary
    if the event can fit then this function will also decide on the start time
    and end time for the event and then slot it into the itinerary

    inputs:
        cur_event (tuple) - (event, venue, distance)
        itinerary (list) - [(event, venue, start, end), ...]

    returns:
        True - if the event can be fit in
        False - if the event cannot be fit in
    '''
    ##################################################
    # check that the event is in correct semi-circle #
    ##################################################
    center = user_data['start_location']
    if len(itinerary) == 0:
        coords1 = center
    else:
        coords1 = venue_to_lat_long(itinerary[-1][1])
    coords2 = venue_to_lat_long(cur_event[1])
    if not validate_angle(coords1, center, coords2):
        return False
    #####################################
    # check event is not double counted #
    #####################################
    if check_double_count(cur_event[0], itinerary):
        return False
    #################################################
    # check start time, this will be the last check #
    #################################################
    start_time = determine_start_time(itinerary, cur_event, user_data['transportation'])
    if start_time == -10:
        # this event is not valid
        return False
	if not validate_restaurant(cur_event[0], start_time):
		return False
	end_time = determine_end_time(itinerary, cur_event, start_time)
	if end_time == -10
		# this event is not valid
		return False
    else:
        # this was the last check so the event is 100% valid
        # add it to the itinerary and return true
        # format is: (event, venue, start, end)
        add_item = (cur_event[0], cur_event[1], start_time, end_time)
        itinerary.append(add_item)
        return True


def check_finished(itinerary):
    '''
    check if the given itinerary is done

    returns:
        True - if itinerary is done
        False - if itinerary is not done
    '''
    if len(itinerary) == 0:
        # if itinerary is empty we are probably not done
        return False
    # check end time of last event
    # if ends past 9pm do not add anymore events
    if itinerary[-1][-1] >= (21 * 60):
        # stop adding events
        return True

####################
# RADIUS FUNCTIONS #
####################

def determine_radius(itinerary, itin_mem, radius_mem):
    '''
    determine what the new search radius should be
    '''
    if len(itinerary) > itin_mem:
        # an item was successfully added
        itin_mem = len(itinerary)
        radius_mem[0] == radius_mem[1]
        # now we need to decrement the radius by some amount
        d_area = decrement_helper(radius_mem, itinerary)
        radius_mem[1] = decrement_radius(radius_mem[0], d_area)
        return 0
    elif len(itinerary) == itin_mem:
        # an item was not added successfully
        d_area = decrement_helper(radius_mem, itinerary)
        radius_mem[1] = increment_radius(radius_mem[1], d_area)
        if radius_mem[1] >= radius_mem[0]:
            # no more possible moves
            return 1
        return 0


def decrement_radius(radius, dA):
    '''
    decrement the given radius
    '''
    new_rad = sqrt((pi * prev_rad ** 2 - dA) / pi)
    if new_rad < 0:
        return prev_rad
    else:
        return new_rad


def increment_radius(radius, dA):
    '''
    increment the given radius
    '''
    new_rad = sqrt((dA / 5 + pi * prev_rad ** 2) / pi)

    return new_rad


def decrement_helper(radius_mem, itinerary):
    '''
    calculate the area that we want to move

    there are 2 values hardcoded in right now, think about changing them to
    take in global variables
    '''
    n = ((24 * 60) - itinerary[-1][-1]) / 120
    d_area = (pi * (radius_mem[0] ** 2)) - (pi * (7 ** 2))
    d_area = d_area / n

    return d_area

#########################
# DISTANCE CALCULATIONS #
#########################

def venue_to_lat_long(venue):
    lat = venue.get('latitude')
    long = venue.get('longitude')
    return [lat, long]


def find_distance(coords1, coords2):
    earth_radius = 3957.25
    lat1 = radians(coords1[0])
    lat2 = radians(coords2[0])
    long1 = radians(coords1[1])
    long2 = radians(coords2[1])
    a = sin((lat2-lat1)/2)**2 + cos(lat1)*cos(lat2)*sin((long2-long1)/2)**2
    return fabs(earth_radius*2*atan2(sqrt(a), sqrt(1-a)))


def find_angle(coords1, center, coords2):
    earth_radius = 3957.25
    a = find_distance(coords1, center)/(2*pi*earth_radius)
    b = find_distance(center, coords2)/(2*pi*earth_radius)
    c = find_distance(coords1, coords2)/(2*pi*earth_radius)
    num = cos(c)-cos(a)*cos(b)
    den = sin(a)*sin(b)
    if (fabs(den) < 0.001):
		if (a+b-c < 0.001):
			return 180.0
		else:
			return 0.0
    return acos(num/den)


def validate_angle(coords1, center, coords2, limit=0.5):
    angle = find_angle(coords1, center, coords2)
    rad_lim = limit*pi
    if (angle <= rad_lim):
        return True
    else:
        return False

def sort_distances(events, center):
	event_distances = []
	for event in events:
		venue = event[1]
		distance = find_distance(venue_to_lat_long(venue), center)
		event_distances.append(event+(distance,))
	event_distances.sort(key=itemgetter(2), reverse=True)
	return event_distances

#########################
# TIME HELPER FUNCTIONS #
#########################
def day_to_str(dayint):
	if dayint == 0:
		return "mon"
	if dayint == 1:
		return "tues"
	if dayint == 2
		return "wed"
	if dayint == 3:
		return "thurs"
	if dayint == 4:
		return "fri"
	if dayint == 5:
		return "sat"
	if dayint == 6:
		return "sun"

def get_close (event):
	close_time = event.get('end')
	if open_time is None:
		weekday = datetime.datetime.today().weekday()
		day_str = day_to_str(weekday)
		close_time = event.get(day_str + '_end')


def determine_start_time(itinerary, event, transport, use_google):
    '''
    find the start time of the next event
    return start time in minutes from midnight
    return -10 if event ends within 30 mins of arrival time
    '''
    last_venue = itinerary[-1][1]
    next_event = event[0]
    next_venue = event[1]
    last_venue_coords = {"lat": last_venue["latitude"], "lng": last_venue["longitude"]}
    next_venue_coords = {"lat": next_venue["latitude"], "lng": next_venue["longitude"]}
    end_time_in_mins = itinerary[-1][3]
    is_past_midnight = end_time_in_mins // 1440
    end_time = end_time_in_mins - 1440 * is_past_midnight
    hours = end_time // 60
    mins = end_time % 60
	distance = find_distance(venue_to_lat_long(last_venue),venue_to_lat_long(next_venue))
	if (transport = 'driving'):
		travel_time = distance * 2
	elif (transport = 'transit'):
		travel_time = distance * 5
	elif (transport = 'walking'):
		travel_time = distance * 20

    # validate start time of the next event
    start_time = end_time_in_mins + travel_time
    if 'start' in next_event:
        if start_time + 30 > next_event['end'] and next_event['end'] != -10:
            return -10
        if start_time < next_event['start']:
            return next_event['start']
    else:
        # implementation depends on how we store permanent events that close after midnight
        # this implementation assumes that all times stored are below 1440
        is_past_midnight = start_time // 1440
        date = datetime.datetime.today() + datetime.timedelta(days=is_past_midnight)
        time = start_time - 1440 * is_past_midnight
        weekday = day_to_str(date.weekday())
        start = next_event[weekday + '_start']
        end = next_event[weekday + '_end']
        if time + 30 > end:
            return -10
        if time < start:
            return start + 1440 * is_past_midnight

    return start_time

def determine_end_time(itinerary, event, start_time):
	tags = event[0].get('tags')
	end_time = get_close(event)
	if (end_time == -10):
		return start_time + random.randint(6, 15)*10
	elif (end_time <= start_time):
		return -10
	if (end_time - start_time < 60):
		return end_time
	if ('food' in tags):
		return start_time + 60
	else:
		time = random.randint(6, 15)*10
		if (start_time + time > end_time):
			return end_time
		else:
			return start_time + time



def validate_restaurant(event, start_time):
	tags = event.get('tags')
	if start_time < (12*60) or start_time > (19.5*60) or (start_time > 13 * 60 and start_time < 18.5*60):
		if 'food' in tags:
			return True
		else:
			return False



################
# MISC HELPERS #
################

def check_double_count(event, itinerary):
    '''
    check to see if the event is already in the itinerary

    returns:
        True - if event is already in itinerary
        False - if event does not exist in itinerary
    '''
    for i in itinerary:
        if event['event_id'] == i[0]['event_id']:
            return True

    return False
