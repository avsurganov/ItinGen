def create_itinerary(user_args):
    '''
    this is the master function that will generate an itinerary given the
    user inputs

    inputs:
        user_args (unknown) - some data structure that is passed back from
                              the front end, should contain:
                              + start time
                              + start location
                              + distance radius
                              + choose only free events
                              + transportation method
                              + user id
    '''
    ############################################################
    # Variables to keep track of various things during runtime #
    ############################################################
    radius_mem = [0, 0]
    itin_mem = 0
    itinerary = []

    ####################################################
    # Step 0: Assume that we have all of the user_args #
    ####################################################
    start_time = 0 # should be int
    start_location = (0.0, 0.0) # should be (lat, lon)
    distance_radius = 0.0 # float miles
    only_free = False # boolean
    transportation = 'car' # str can be ['car', 'public', 'walk']

    ####################################################################
    # Step 1: Estimate the number of events that we will likely select #
    #         within this itinerary                                    #
    ####################################################################
    avg_mins_per_event = 120
    est_num_events = ((12 * 60) - start_time) / avg_mins_per_event

    ######################################################################
    # Step 2: Retrieve events from the database based on the user id and #
    #         the ratio of categories to get, then remove bad events and #
    #         return back a list of events in the form:                  #
    #         [[event, venue], [event, venue], [event, venue], ...]      #
    ######################################################################
    events = []

    #########################################################################
    # Step 3: Calculate the distance for each [event, venue] from the start #
    #         location to create [event, venue, distance] and the sort the  #
    #         events by that distance in decreasing distance order          #
    #########################################################################
    events = []

    ########################################################
    # Step 4: Go through the steps to create the itinerary #
    ########################################################
    # manually set the radius for the first iteration
    radius_mem[0] = distance_radius
    radius_mem[1] = distance_radius
    # find first index within that radius
    i = -1
    for x, e in events:
        if e[2] <= radius_mem[1]:
            i = x
            break
    # if still -1 exit the program
    if i == -1:
        exit(1)
    # now that we know the index, lets make a copy with just the valid indices
    valid_events = events[i:]
    # lets create the full itinerary now
    cont = True
    while cont:
        # try to increment the itinerary
        increment_itinerary(itinerary, valid_events)
        # check if itinerary is finished
        if check_finished(itinerary):
            cont = False
        else:
            # the given itinerary is not done, we need to get a new radius
            # and find the new valid itins based on distance
            if determine_radius(itinerary, itin_mem, \
                                radius_mem, est_num_events):
                cont = False
            else:
                # find first index within that radius
                i = -1
                for x, e in events:
                    if e[2] <= radius_mem[1]:
                        i = x
                        break
                if i == -1:
                    valid_events = []
                else:
                    valid_events = events[i:]




def increment_itinerary(itinerary, valid_events):
    '''
    given an itinerary and a list of events try to add on another event to the
    itinerary
    '''
    return 0


def check_finished(itinerary):
    '''
    check if the given itinerary is done
    '''
    return 0


def determine_radius(itinerary, itin_mem, radius_mem, est_num_events):
    '''
    determine what the new search radius should be
    '''
    if len(itinerary) > itin_mem:
        # an item was successfully added
        itin_mem = len(itinerary)
        radius_mem[0] == radius_mem[1]
        # now we need to decrement the radius by some amount
        radius_mem[1] = decrement_radius(radius_mem[0], est_num_events)
        return 0
    elif len(itinerary) == itin_mem:
        # an item was not added successfully
        radius_mem[1] = increment_radius(radius_mem[1], est_num_events)
        if radius_mem[1] >= radius_mem[0]:
            # no more possible moves
            return 1
        return 0


def decrement_radius(radius, est_num_events):
    '''
    decrement the given radius
    '''
    return 0


def increment_radius(radius, est_num_events):
    '''
    increment the given radius
    '''
    return 0
