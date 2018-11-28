import time
# testing file for ticketmaster api calls
# activities that use the ticketmaster api:
# - sports
# - music]
# NEWER NOTES HAVE A LOWER LINE NUMBER
# NEWEST
# NOTE: these are all executed during the run time of the data collection
#       process and there are no standalone tests to run for the process of
#       collecting data (more effecient to check data while processing)
# NOTE: this has been moved from the tests directory into this directory
#       since the last iteration. The reason is because these checks need to
#       run during the execution of the scipt and it was difficult to import
#       the functions from an outside directory
# NOTE: none of the events that we are getting from the ticketmaster api will
#       be put into the permanent events table; everything is going into the
#       one time event table
# NOTE: many more tests will be added as more code is written and unique
#       cases may appear
# OLDEST


# check that single venue data is valid
# structure of data to be put into venue database:
#
# [
#         {
#             "venue_id": (str),
#             "venue_name": (str),
#             "latitude": (float),
#             "longitude": (float),
#             "address1": (string),
#             "address2": (string),
#             "address3": (string),
#             "city": (string),
#             "state": (string),
#             "zip_code": (string)
#         },
#         {
#             "venue_id": (str),
#             "venue_name": (str),
#             "latitude": (float),
#             "longitude": (float),
#             "address1": (string),
#             "address2": (string),
#             "address3": (string),
#             "city": (string),
#             "state": (string),
#             "zip_code": (string)
#         },
#         ...
# ]
#
def tm_venue_check(venue):
    '''
    check an individual venue dict to make sure that all of the components are
    there and are the correct type before adding it into dictionary
    NOTE: this check is being performed constantly as we process venue data and
          add it into the json file before pushing it all into the database

    intput:
        venue (dict) - holds venue data
    ouput:
        valid (boolean) - True or False
    '''
    valid = True
    if not type(venue.get("venue_id", None)) == str:
        print("\tTYPE ERROR: venue_id should be str")
        valid = False
    if not type(venue.get("venue_name", None)) == str:
        print("\tTYPE ERROR: venue_name should be str")
        valid = False
    if not type(venue.get("latitude", None)) == float:
        print("\tTYPE ERROR: latitude should be float")
        valid = False
    if not type(venue.get("longitude", None)) == float:
        print("\tTYPE ERROR: longitude should be float")
        valid = False
    if not type(venue.get("address1", None)) == str:
        print("\tTYPE ERROR: address1 should be str")
        valid = False
    if not type(venue.get("address2", None)) == str:
        print("\tTYPE ERROR: address2 should be str")
        valid = False
    if not type(venue.get("address3", None)) == str:
        print("\tTYPE ERROR: address3 should be str")
        valid = False
    if not type(venue.get("city", None)) == str:
        print("\tTYPE ERROR: city should be str")
        valid = False
    if not type(venue.get("state", None)) == str:
        print("\tTYPE ERROR: state should be str")
        valid = False
    if not type(venue.get("zip_code", None)) == str:
        print("\tTYPE ERROR: zip_code should be str")
        valid = False

    return valid


# check that single event data is valid
# structure of data to be put into one time events database:
#
# [
#         {
#             "event_id": (str),
#             "event_name": (str),
#             "venue_id": (str),
#             "start": (int)(minutes),
#             "end": (int)(minutes),
#             "date": (str),
#             "tags": (list),
#             "price": (float)
#         },
#         {
#             "event_id": (str),
#             "event_name": (str),
#             "venue_id": (str),
#             "start": (int)(minutes),
#             "end": (int)(minutes),
#             "date": (str),
#             "tags": (list),
#             "price": (float)
#         },
#         ...
# ]
#
def tm_event_check(event):
    '''
    check an individual event dict to make sure that all of the components are
    there and are the correct type
    NOTE: similar to the venue_check, this check is done every time we process
          a new event and before we put it into the file to be pushed to the
          database

    input:
        event (dict) - holds all data for a single event
    output:
        valid (boolean) - True or False
    '''
    valid = True
    if not type(event.get("event_id", None)) == str:
        print("\tTYPE ERROR: event_id should be str")
        valid = False
    if not type(event.get("event_name", None)) == str:
        print("\tTYPE ERROR: event_name should be str")
        valid = False
    if not type(event.get("venue_id", None)) == str:
        print("\tTYPE ERROR: venue_id should be str")
        valid = False
    if not type(event.get("start", None)) == int:
        print("\tTYPE ERROR: start should be int")
        valid = False
    if not type(event.get("end", None)) == int:
        print("\tTYPE ERROR: end should be int")
        valid = False
    if not type(event.get("date", None)) == str:
        print("\tTYPE ERROR: date should be str")
        valid = False
    if not type(event.get("tags", None)) == list:
        print("\tTYPE ERROR: tags should be list")
        valid = False
    if not type(event.get("price", None)) == float:
        print("\tTYPE ERROR: price should be float")
        valid = False

    return valid


# check that all events have a valid venue id
def check_all_venue_id(events, venues, venue_ids, venue_bu):
    '''
    before pushing the data that we just processed into the database, we need
    to confirm that all of the events that we processed have a valid venue_id

    input:
        events (list) - list of dicts that we plan to push into the database
        venue_ids (set) - a set of venues that are in our database or are going
                        to be added into the database
        venues (list) - list of dicts of venues
    output:
        valid (boolean) - True or False
        del_list (list) - list of indexes to delete
    '''
    del_list = []

    for i, e in enumerate(events):
        valid = True
        venue_id = e["venue_id"]
        if venue_id not in venue_ids:
            valid = False
            event_name = e["event_name"]
            print("\tEVENT ERROR: event %s has invalid venue_id" % event_name)
            print("\t\tEVENT ID: %s" % e["event_id"])
            print("\tLOOKING FOR SOLUTION: looking for a name match")
            for v in venues:
                if v["venue_name"] == e["venue_name"]:
                    valid = True
                    print("\tFOUND NEW MATCH: found from existing venues")
                    events[i]["venue_id"] = v["venue_id"]
                    break
            # worse case scenario we can look through our backups
            if not valid:
                for v in venue_bu:
                    if v["venue_id"] == venue_id:
                        valid = True
                        print("FOUND NEW MATCH: found from backup venues")
                        venues.append(v)
        if not valid:
            del_list.append(i) # delete the bad events

    return del_list


# check the return value of the request
def check_r_status(r):
    '''
    checks the status code of the request that we just made and the header
    information

    inputs:
        r (request response) - response from the request
    outputs:
        0 - if everything is ok
        -1 - if something is wrong
    '''
    if r.status_code == 200:
        return 0 # everything is fine
    else:
        # display what is wrong
        if r.status_code == 401:
            print("ERROR: 401 - %s" % r.json()["fault"]["faultstring"])
        elif r.status_code == 404:
            print("ERROR: 404 - Not Found")
        elif r.status_code == 400:
            print("ERROR 400 - %s" % r.json()["errors"][0]["detail"])
        elif r.status_code == 429:
            print("ERROR 429 - %s" % r.sjon()["fault"]["faultstring"])
            print("SOLUTION: pause to rate limit")
            time.sleep(2)
        else:
            print("ERROR: error not known, printing full error")
            print(r.status_code)
            print(r.headers)
            print(r.json())

        return -1
