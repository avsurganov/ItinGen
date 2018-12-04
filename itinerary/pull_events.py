import json
import pprint
import sys
import urllib
import datetime
import random
import numpy
import math
from pymongo import MongoClient
#from algo_skeleton import *

client = MongoClient("mongodb://localhost:27017/")
with client:
    db = client.itingen

    # just a simple date function
    def get_date():
        '''
        get the current date
        ex. for November 13, 2018 the output will be 11-13-2018

        inputs:
            None
        outputs:
            date (str) - current date
        '''
        date = datetime.datetime.now().strftime("%m-%d-%Y")

        return date

    # gets categories from which to get events
    def pick_categories(user_weight=0):
        ordered_categories = shuffle(categories)
        return ordered_categories

    # get str version of a day
    def day_to_str(dayint):
        if dayint == 0:
            return "mon"
        if dayint == 1:
            return "tues"
        if dayint == 2:
            return "wed"
        if dayint == 3:
            return "thurs"
        if dayint == 4:
            return "fri"
        if dayint == 5:
            return "sat"
        if dayint == 6:
            return "sun"

    # for permanent events - check that time and date are right
    def time_date_check_perm(event,user_start_time):
        daynum = datetime.datetime.today().weekday()
        daystr = day_to_str(daynum)
        startname = daystr + "_start"
        endname = daystr + "_end"
        starttime = event[startname]
        endtime = event[endname]
        if endtime < user_start_time:
            return False
        if endtime - user_start_time < 15: #event should be open for more than 15 min after start time
            return False
        if starttime == 0 and endtime == 0:
            return False
        return True

    # check that time is compatible with user time
    def time_check_temp(event,user_start_time):
        starttime = event.get('start')
        endtime = event.get('end')
        if endtime == -10:
            return True
        if endtime < user_start_time:
            return False
        if endtime - user_start_time < 15:
            return False
        # do we want to throw out if the event starts before the user start time?
        if starttime == 0 and endtime == 0:
            return False
        return True

    # check that date of event is actually today
    def date_check_temp(event):
        today = get_date()
        if event.get('date') != today:
            return False
        return True

    # check that events dont overlap with meal times
    def check_meal_overlap_temp(event):
        starttime = event.get('start')
        endtime = event.get('end')
        if starttime >= 660 and endtime <= 780:
            return False #throws out if entire event is within lunch period 11-1
        if starttime >= 660 and starttime <= 690 and endtime >= 780:
            return False #throws out if event covers all but 1st half hour of lunch
        if starttime <= 660 and endtime >= 750 and endtime <= 780:
            return False #throws out if event covers all but last half hour of lunch
        if starttime <= 660 and endtime >= 780:
            return False #throws out if event covers entire lunch period
                            # may want to make this optional depending on how we think
                            # of one time events - do you go to whole thing or no?
        return True

    # checks that events are free
    def check_free(event):
        if event["price"] == 0:
            return True
        if event["price"] == -10:
            return True
        return False

    # gets the pool of temporary events
    def get_t_events(user_inputs,numev):
        evindexes = []
        tpool = []
        total_tevents = db.tevents.find().count()
        evindexes.append(random.sample(range(total_tevents),numev))
        for index in evindexes[0]:
            event = db.tevents.find().skip(index).limit(1)[0]
            f = True
            t = True
            d = True
            if user_inputs.get('only_free') == True:
                f = check_free(event)
            t = time_check_temp(event,user_inputs.get('start_time'))
            d = date_check_temp(event)
            if t and d and f:
                venid = event.get("venue_id")
                venue = db.venues.find_one({'venue_id': venid})
                if venue:
                    del(event['_id'])
                    del(venue['_id'])
                    del(event['__v'])
                    del(venue['__v'])
                    tpool.append((event,venue))
        print(len(tpool))            
        return tpool

    # gets the pool of permanent events
    def get_p_events(user_inputs,numev):
        evindexes = []
        ppool = []
        total_pevents = db.pevents.find().count()
        evindexes.append(random.sample(range(total_pevents),numev))
        for index in evindexes[0]:
            event = db.pevents.find().skip(index).limit(1)[0]
            f = True
            if user_inputs.get('only_free') == True:
                f = check_free(event)
            td = time_date_check_perm(event,user_inputs.get('start_time'))
            if td and f:
                venid = event.get("venue_id")
                venue = db.venues.find_one({'venue_id': venid})
                if venue:
                    del(event['_id'])
                    del(venue['_id'])
                    del(event['__v'])
                    del(venue['__v'])
                    ppool.append((event,venue))
        return ppool

    # gets the complete pool of events with proper temp/perm ratio
    def get_pool(user_inputs, total):
        total_p = db.pevents.find().count()
        total_t = db.tevents.find().count()
        total_all = total_p + total_t
        ntemp = int((total_t / total_all) * total)
        nperm = int((total_p / total_all) * total)
        tpool = get_t_events(user_inputs,ntemp)
        ppool = get_p_events(user_inputs,nperm)
        pool = tpool + ppool
        return pool
