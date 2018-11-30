

# VENUE VALIDATION FUNCTIONS

# validate the length of the venue dictionary created
def validate_venue_length(venue):
    if len(venue) != 10:
        return False
    else:
        return True

# validate the yelp-assigned ID of a venue dict
def validate_yelpID_venue(dict):
    if 'venue_id' not in dict:
        return False
    if not (isinstance(dict['venue_id'],str)):
        return False
    return True

# validate the coordinates field of a business dict
def validate_coordinates(venue):
    if 'latitude' not in venue:
        return False
    if 'longitude' not in venue:
        return False
    latitude = venue['latitude']
    longitude = venue['longitude']
    if not (isinstance(latitude,float)):
        return False
    if not (isinstance(longitude,float)):
        return False
    if latitude < -90 or latitude > 90:
        return False
    if longitude < -180 or longitude > 180:
        return False
    return True

# validate the location field of a business dict
def validate_location(venue):
    if 'address1' not in venue:
        return False
    if 'city' not in venue:
        return False
    if 'state' not in venue:
        return False
    if 'zip_code' not in venue:
        return False
    if not (isinstance(venue['address1'],str)):
        return False
    if not (isinstance(venue['city'],str)):
        return False
    if not (isinstance(venue['state'],str)):
        return False
    if not (isinstance(venue['zip_code'],str)):
        return False
    return True

# validate the name field of a dict
def validate_venue_name(bizdict):
    if ('venue_name' not in bizdict):
        return False
    name = bizdict['venue_name']
    if (isinstance(name, str)):
        if (name.strip()):
            return True
    return False

# EVENT VALIDATION FUNCTIONS

# validate the length of an event dictionary
def validate_event_length(event):
    if len(event) != 19:
        return False
    else:
        return True

# validate the yelp-assigned ID of an event dict
def validate_yelpID_event(dict):
    if 'venue_id' not in dict or 'event_id' not in dict:
        return False
    if not (isinstance(dict['venue_id'],str)) or not (isinstance(dict['event_id'],str)):
        return False
    return True

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
    open_hours = [bizdict['mon_start'],
                    bizdict['tues_start'],
                    bizdict['wed_start'],
                    bizdict['thurs_start'],
                    bizdict['fri_start'],
                    bizdict['sat_start'],
                    bizdict['sun_start']]
    close_hours = [bizdict['mon_end'],
                    bizdict['tues_end'],
                    bizdict['wed_end'],
                    bizdict['thurs_end'],
                    bizdict['fri_end'],
                    bizdict['sat_end'],
                    bizdict['sun_end']]
    for day in range(7):
        start = open_hours[day]
        end = close_hours[day]
        if (start > end):
            return False
    return True

# validate the category field of a dict
def validate_tags(bizdict):
    if ('tags' not in bizdict):
        return False
    for tag in bizdict['tags']:
        if (not isinstance(tag, str)):
            return False
        if (not tag.strip()):
            return False
    return True

# validate the name field of a dict
def validate_event_name(bizdict):
    if ('event_name' not in bizdict):
        return False
    name = bizdict['event_name']
    if (isinstance(name, str)):
        if (name.strip()):
            return True
    return False


# WRAPPERS

# wrapper for all venue validation tests
def validate_venue(venue):
    if (validate_venue_length(venue) and
        validate_yelpID_venue(venue) and
        validate_location(venue) and
        validate_coordinates(venue) and
        validate_venue_name(venue)):
        return True
    else:
        return False

# wrapper for all event validation tests
def validate_event(event):
    if (validate_event_length(event) and
        validate_yelpID_event(event) and
        validate_hours(event) and
        validate_event_name(event)):
        return True
    else:
        return False
