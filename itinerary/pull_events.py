import json
import pprint
import sys
import urllib
import datetime
import random
import numpy

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

categories = ["misc","museums","music","nightlife","publicattractions","sports"]
numcat = 6
user_weight_default = [1 for x in range(numcat)]
numev = 50 # number of events you want to pull from each category
            # maybe make bigger if only free? bc you'll throw out a lot


# what is format of user weight gonna be? a dict? each category has a value?
# assumes format = array w probabilities ordered by alphabetical categories
def pick_categories(user_weight=0):
    ordered_categories = []
    if user_weight:
        ordered_categories.append(numpy.random.choice(categories,replace=False,p=user_weight))
    else:
        ordered_categories = shuffle(categories)
    return ordered_categories

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

# for permanent events
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

def time_check_temp(event,user_start_time):
    starttime = event[start]
    endtime = event[end]
    if endtime < user_start_time:
        return False
    if endtime - user_start_time < 15:
        return False
    # do we want to throw out if the event starts before the user start time?
    if starttime == 0 and endtime == 0:
        return False
    return True

def date_check_temp(event):
    today = get_date()
    if event[date] != today:
        return False
    return True

def check_meal_overlap_temp(event):
    starttime = event[start]
    endtime = event[end]
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

def check_free(event):
    if event[price] != -10:
        return False
    return True
 
