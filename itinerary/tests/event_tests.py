# tests for events in an itinerary
from itin_examples import *

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


def validate_restaurants(itinerary):
    '''
    check that there are is at least 1 restaurant if the itinerary goes on for
    more than 4 hours (we can change this later)

    inputs:
        itinerary (list of dicts)

    outputs:
        0 for success
        1 for failure
    '''
    start = itinerary[2]
    end = itinerary[3]
    if (end - start) >= (4 * 60):
        for event in itinerary:
            if 'food' in event[0]['tags']:
                return 0
        return 1

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


# examples of unit tests
assert validate_no_duplicates(itin9) == 1
assert validate_no_duplicates(itin10) == 0
assert validate_venue_id_match(itin10) == 1
assert validate_venue_id_match(itin8) == 0
assert validate_event_date(itin8, '02-16-2018') == 1
assert validate_event_date(itin8, '02-16-2019') == 0
assert validate_event_price(itin8, 0) == 1
assert validate_event_price(itin8, 100000) == 0
