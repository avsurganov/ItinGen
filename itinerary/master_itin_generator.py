from algo_skeleton import *
from pull_events import *
from pymongo import MongoClient

def generate_itin(start_time, latitude, longitude, free, radius, transport):
    tries = 0
    final_itin = []
    while len(final_itin) < 2:
        [itin, valid] = create_itinerary(start_time, latitude, longitude, free, radius, transport, 500 * (tries+1))
        if valid and len(itin) > 1 and  itin[-1][3] - start_time > 120:
            final_itin = itin
        tries+=1
    return final_itin
