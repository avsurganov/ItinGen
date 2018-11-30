import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["itingen"]


"""
    This returns an array of venues / pevents / tevents. Iterate over them simply like so:

    for venue in venues:
        print(venue)
"""
venues = mydb["venues"].find()
pevents = mydb["pevents"].find()
tevents = mydb["tevents"].find()


