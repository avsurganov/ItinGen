from algo_skeleton import *
from pull_events import *
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
with client:
    db = client.itingen
def generate_itin(user_inputs):
    tries = 0
    final_itin = []
    while len(final_itin) < 2:
        [itin, valid] = create_itinerary('test', 500 * (tries+1))
        if valid and len(itin) > 1 and  itin[-1][3] - user_inputs.get('start_time') > 120:
            final_itin = itin
        tries+=1
    newitin = {"activities" : final_itin}
    db.itineraries.insert_one(newitin)
    return final_itin

itin = generate_itin({'start_time':120})
print(itin)
