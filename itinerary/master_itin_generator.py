from algo_skeleton import *
from pull_events import *
from math import fabs
import sys
from pymongo import MongoClient

# main function to make itinerary
def generate_itin(start_time, latitude, longitude, free, radius, transport):
    tries = 0
    final_itin = []    
    query_size = 500
#    time_split = start_time.split('T')
#    units = time_split[1].split(':')
#    time = 60*int(units[0])+int(units[1])

    hours = int(start_time[0:2]) % 12
    minutes = int(start_time[3:5])
    time_of_day = start_time[6:8]
    if hours == 12:
        hours -= 12
    if time_of_day == 'PM':
        hours +=12
    time = hours*60 + minutes
    
    # check if user inputs make sense
    if time > (20*60) or fabs(latitude - 41.5) > 2 or fabs(longitude + 87.5) > 2:
        print(time)
        return []
    while len(final_itin) < 2 and tries < 10:
        [itin, valid] = create_itinerary(time, latitude, longitude, free, radius, transport, query_size)
        print("We")
        print(valid)
        print(itin)
        print(query_size)
        #print(itin)
        sys.stdout.flush()
        if not valid:
            query_size += 250*int(tries/5)
        if len(itin) < 2 or itin[-1][3] < 240:
            query_size += 1000*int(tries/5)
        elif valid:
            final_itin = itin
        tries+=1
    return final_itin

#itin = generate_itin('09:00 AM', 41.881855, -87.627115, False, 10.0, 'WALK')
#print(itin)
