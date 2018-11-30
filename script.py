from pymongo import MongoClient
import sys

args = sys.argv
print(args)

client = MongoClient('mongodb://localhost:27017/')

## tevents
## pevents
## venues

with client:
    db = client.itingen
    print("DB HAS")
    ## FIND COLLECTIONS COUNT
    print(db.venues.find().count())
    ## FIND  ITEM AT INDEX  2 -> skip(index)
    venue_id = 'yelpm-fake'
    venue = db.venues.find_one({'venue_id': venue_id})
    print(venue)
    venues = db.venues.find().skip(2).limit(1)
    # print(venues[0])
