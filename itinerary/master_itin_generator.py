from algo_skeleton import *
from pull_events import *
from pymongo import MongoClient

def generate_itin(start_time, latitude, longitude, free, radius, transport):
    tries = 0
    final_itin = []
    time_split = start_time.split('T')
    units = time_split[1].split(':')
    time = 60*int(units[0])+int(units[1])
    while len(final_itin) < 2:
        [itin, valid] = create_itinerary(60*int(units[0])+int(units[1]), latitude, longitude, free, radius, transport, 500 * (tries+1))
        if valid and len(itin) > 1 and  itin[-1][3] - time > 120:
            final_itin = itin
        tries+=1
    return final_itin

#itin = generate_itin('2018-11-30T08:21:50.182Z', 41.881855, -87.627115, False, 10.0, 'driving')
#print(itin)
