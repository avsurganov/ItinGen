from __future__ import print_function

import argparse
import json
import pprint
import requests
import sys
import urllib
import datetime

from validation import *

# This client code can run on Python 2.x or 3.x.  Your imports can be
# simpler if you only need one of those.
try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode

# just a simple date function
def get_date():
    '''
    get the current date
    ex. for November 13, 2018 the output will be 20181113

    inputs:
        None
    outputs:
        date (str) - current date
    '''
    date = datetime.datetime.now().strftime("%Y%m%d")

    return date

# Uses private keys to authenticate requests (API Key)
# You can find it on https://www.yelp.com/developers/v3/manage_app
API_KEY = "PcUO1w3mcD-nRwv_CH6Sg06x07INlXcQkIZNBVGMSKDM2W8R-56Y0OCntQUSogMpqSPEkaZzwahHyvyjdXlP__TXeTbq880ftMxlPpJd6zsuc0J4wlGU1uhvS1rjW3Yx"

keys = ["txsgyNE9-odnCQBXF4IeAQcy9JjdWtCSdvJLpln0AhSkmX5B4q57QiLM-1T9jZTI5p3csIEg5aOUSzJHHggKDT53tQ-Frtd-sZoTlXscG3U_IVAwJ_p6fqeCJlvqW3Yx",
        "Xnp-xCH_EyHt_QCgvcBCqJklS-AvMSvqcfBZFOdeElGxaMUNrvQV7h9bt2MuaOr5T-5kjcJsm22uCyOxgtaXR4Vm5fbxGe9BuSqRWSppi8TIedkoX23kQ9e77CjiW3Yx",
        "M9S8kSyLzLf3y8jtO1f2G9YwCUsYZ0jhONdGYkaaV-MbvmjkoTKmJ2ujHeBNwqYLx8nO4N1Ui6lLhl4UftOuL7n0NaNgRIAS3R5v9P-x2wOspOz6BRrNfHhEJhn-W3Yx",
        "9_5vnCP7kfYbVwsIPW29k6u-XcMC0aY0XA92dDOaRPJeJIrJwBudLTIfqWsBRsKZngFdnen9FiG7J2E6RH0V73WOIaEt3BWj0okyaM4vToY9urtHb11ZyE0rshn-W3Yx",
        "sp3v1oG59W3WrviOCMpj6X38FhYOpZKB7VIpkFqQT9Q63vxLOo78XsNrUNTWtM6xgSDNWN5FVzonizPlTEZFoUegCrmyOXpftdPw4sj06aIuWz_bOJTR0JUEqhv-W3Yx",
        "LfDN02IOr4ATEedypFAxyOx9ux0VabEv2mmlizqWpms1LshQidkyZUg0Sl_cFoPRf7W1AfLPuZXgUKHTv5mP306p-Fv9A-h6vKbZOMnvjqDFd6aaDDxImNR8UTrrW3Yx",
        "PcUO1w3mcD-nRwv_CH6Sg06x07INlXcQkIZNBVGMSKDM2W8R-56Y0OCntQUSogMpqSPEkaZzwahHyvyjdXlP__TXeTbq880ftMxlPpJd6zsuc0J4wlGU1uhvS1rjW3Yx"
]

def switch_api(API_KEY):
    i = 0
    for x, val in enumerate(keys):
        if val == API_KEY:
            i = x
            break
    new_i = (i + 1) % len(keys)
    API_KEY = keys[new_i]


# API constants
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.

# Defaults
DEFAULT_CATEGORIES = 'museums'
DEFAULT_LOCATION = 'Chicago, IL'
SEARCH_LIMIT = 50
DEFAULT_OFFSET = 0

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--cat', dest='categories', default=DEFAULT_CATEGORIES,
                    type=str, help='Search categories (default: %(default)s)')
parser.add_argument('-l', '--location', dest='location',
                    default=DEFAULT_LOCATION, type=str,
                    help='Search location (default: %(default)s)')
parser.add_argument('-o', '--offset', dest='offset',
                     default=DEFAULT_OFFSET, type=str,
                     help='Result page offset (default: %(default)s)')
input_values = parser.parse_args()

VEN = "../app/activities_data/venues/"
EVN = "../app/activities_data/events/"
venuefname = VEN + input_values.categories + '_venues_' + get_date() + '.json'
eventfname = EVN + input_values.categories + '_events_' + get_date() + '.json'

venuelist = []
eventlist = []




# "component" query functions

# Given API key, sends get request to the API
# host (str) is domain host, path (str) is path of API after domain
# url_params (dict) is an optional set of query parameters
# returns JSON response from the request
# raises HTTP error if an error occurs from the request
def request(host, path, api_key, url_params=None):
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }
    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)
    if "error" in response:
        switch_api(API_KEY)
        headers['Authorization'] = 'Bearer %s' % API_KEY
        response = requests.request('GET', url, headers=headers, params=url_params)
    return response.json()


# query the API by given category, location, and offset
# returns JSON response from the request with all businesses of given category and location
def search_categories(api_key, categories, location, offset):
    url_params = {
        'categories': categories,
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'offset': int(offset)
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


# query the business API by a business ID to get more specifics about a business
# returns JSON response from the request
def get_business(api_key, business_id):
    business_path = BUSINESS_PATH + business_id
    return request(API_HOST, business_path, api_key)

def get_ids(businesses):
    biz_ids = []
    for biz in businesses:
        biz_ids.append(biz['id'])
    return biz_ids




# "helper" functions for dictionary construction

def converttime_yelp(time):
    if len(time) < 4:
        raise Exception("time string is too short. string was: {}".format(time))
    hours = int(time[0:2])
    minutes = int(time[2:4])
    inttime = hours*60 +minutes
    if inttime == 1440:
        return 0
    if inttime > 1440:
        raise Exception("time exceeds 24hr frame. time was: {}".format(inttime))
    return inttime

def construct_venue(business_details):
    venue = {}
    venue['venue_id'] = "yelp" + business_details['id']
    venue['venue_name'] = business_details['name']
    venue['latitude'] = float(business_details['coordinates']['latitude'])
    venue['longitude'] = float(business_details['coordinates']['longitude'])
    venue['address1'] = business_details['location']['address1']
    venue['address2'] = business_details['location']['address2']
    venue['address3'] = business_details['location']['address3']
    venue['city'] = business_details['location']['city']
    venue['state'] = business_details['location']['state']
    venue['zip_code'] = business_details['location']['zip_code']
    return venue

def tag_as_category(input_category):
    # (food,) nightlife, museums, publicattractions, misc
    # sports and music i think are all ticketmaster and eventbrite
    museums = ["aquariums", "culturalcenter", "galleries", "museums",
                "observatories", "planetarium", "zoos",
                ]
    publicattractions = ["gardens", "landmarks", "localflavor"]
    nightlife = ["adultentertainment", "barcrawl", "beerbar", "champagnebars",
                    "cigarbars", "cocktailbars", "divebars", "drivethrubars",
                    "gaybars", "hookah_bars", "irish_pubs", "lounges",
                    "pubs", "speakeasies", "sportsbars", "tikibars",
                    "vermouthbars", "whiskeybars", "wine_bars", "beergardens",
                    "clubcrawl", "comedyclubs", "countrydancehalls", "danceclubs",
                    "jazzandblues", "karaoke", "pianobars", "poolhalls",
                    "cabaret", "casinos", "wineries", "breweries",
                    "distilleries"
                    ]
    misc = ["farms", "fleamarkets", "paintandsip", "publicmarkets",
            "trampoline", "bowling", "escapegames", "golf",
            "minigolf", "paintball", "lasertag", "scavengerhunts",
            "waterparks", "arcades", "hauntedhouses", "saunas",
            "amusementparks", "psychic_astrology", "virtualrealitycenters"
            ]
    food = ["acaibowls",
	           "bagels",
               "bakeries",
               "bento",
               "bubbletea",
               "chimneycakes",
               "churros",
               "cideries",
               "coffee",
               "cupcakes",
               "delicatessen",
               "desserts",
               "diyfood",
               "donuts",
               "empanadas",
               "farmersmarket",
               "foodtrucks",
               "gelato",
               "icecream",
               "jpsweets",
               "juicebars",
               "cakeshop",
               "poke",
               "pretzels",
               "streetvendors",
               "tea",
               "afghan",
                "african",
                "newamerican",
                "tradamerican",
                "arabian",
                "argentine",
                "armenian",
                "asianfusion",
                "australian",
                "austrian",
                "bangladeshi",
                "bbq",
                "basque",
                "belgian",
                "brasseries",
                "brazilian",
                "breakfast_brunch",
                "british",
                "buffets",
                "bulgarian",
                "burgers",
                "burmese",
                "cafes",
                "cafeteria",
                "cajun",
                "cambodian",
                "newcanadian",
                "carribean",
                "cheesesteaks",
                "chickenshop",
                "chicken_wings",
                "chinese",
                "comfortfood",
                "creperies",
                "cuban",
                "czech",
                "delis",
                "diners",
                "ethiopian",
                "hotdogs",
                "filipino",
                "fishnchips",
                "fondue",
                "food_court",
                "french",
                "gastropubs",
                "georgian",
                "german",
                "gluten_free",
                "greek",
                "guamanian",
                "halal",
                "hawaiian",
                "himalayan",
                "honduran",
                "hkcafe",
                "hotdog",
                "hotpot",
                "hungarian",
                "iberian",
                "indpak",
                "indonesian",
                "italian",
                "calabrian",
                "sardinian",
                "sicilian",
                "tuscan",
                "venetian",
                "japanese",
                "conveyorsushi",
                "japacurry",
                "ramen",
                "kebab",
                "korean",
                "kosher",
                "laotian",
                "latin",
                "colombian",
                "salvadoran",
                "venezuelan",
                "raw_food",
                "malaysian",
                "mediterranean",
                "falafel",
                "mexican",
                "tacos",
                "mideastern",
                "egyptian",
                "lebanese",
                "modern_european",
                "mongolian",
                "moroccan",
                "newmexican",
                "nicaraguan",
                "noodles",
                "pakistani",
                "panasian",
                "persian",
                "peruvian",
                "pizza",
                "polish",
                "polynesian",
                "popuprestaurants",
                "portuguese",
                "poutineries",
                "russian",
                "salad",
                "sandwiches",
                "scandinavian",
                "scottish",
                "seafood",
                "singaporean",
                "slovakian",
                "soulfood",
                "soup",
                "southern",
                "spanish",
                "srilankan",
                "steak",
                "supperclubs",
                "sushi",
                "syrian",
                "taiwanese",
                "tapas",
                "tapasmallplates",
                "tex-mex",
                "thai",
                "turkish",
                "ukrainian",
                "uzbek",
                "vegan",
                "vegetarian",
                "vietnamese",
                "waffles",
                "wraps"
                ]
    if input_category in museums:
        return "museums"
    if input_category in publicattractions:
        return "publicattractions"
    if input_category in nightlife:
        return "nightlife"
    if input_category in misc:
        return "misc"
    if input_category in food:
        return "food"


def construct_event(business_details):
    event = {}
    event['venue_id'] =  "yelp" + business_details['id']
    event['event_name'] = business_details['name']
    event['event_id'] =  "yelp" + business_details['id']
    event['mon_start'] = extract_hours(business_details,0,0)
    event['mon_end'] = extract_hours(business_details,0,1)
    event['tues_start'] = extract_hours(business_details,1,0)
    event['tues_end'] = extract_hours(business_details,1,1)
    event['wed_start'] = extract_hours(business_details,2,0)
    event['wed_end'] = extract_hours(business_details,2,1)
    event['thurs_start'] = extract_hours(business_details,3,0)
    event['thurs_end'] = extract_hours(business_details,3,1)
    event['fri_start'] = extract_hours(business_details,4,0)
    event['fri_end'] = extract_hours(business_details,4,1)
    event['sat_start'] = extract_hours(business_details,5,0)
    event['sat_end'] = extract_hours(business_details,5,1)
    event['sun_start'] = extract_hours(business_details,6,0)
    event['sun_end'] = extract_hours(business_details,6,1)
    event['tags'] = []
    for item in business_details['categories']:
        event['tags'].append(item['alias'])
    category_tag = tag_as_category(input_values.categories)
    event['tags'].append(category_tag)
    if 'price' in business_details:
        event['price'] = 0 - len(business_details['price'])
    else:
        event['price'] = -10
    return event

def extract_hours(business_details, day, startorend):
    if 'hours' not in business_details:
        return 0
    daysopen = len(business_details['hours'][0]['open'])
    if day < daysopen:
        hours = business_details['hours'][0]['open'][day]
        start = converttime_yelp(hours['start'])
        end = converttime_yelp(hours['end'])
        if startorend == 0:
            return start
        else:
            return end
    else:
        return 0




# main API query and dictionary construction function

# query the API by the input values (categories, location offset)
# for each business, gets more specific details
# creates a venue and event dictionary for each business and adds this dictionary to a list
def query_api(categories, location, offset):
    nevents = 0
    nvenues = 0

    response = search_categories(API_KEY, categories, location, offset)
    businesses = response.get('businesses')
    nbiz = response.get('total')
    print('# businesses = {}'.format(nbiz))

    if not businesses:
        print(u'No businesses for {0} in {1} found.'.format(categories, location))
        return

    while businesses:
        biz_ids = get_ids(businesses)
        for id in biz_ids:
            biz_detail = get_business(API_KEY,id)
            venue = construct_venue(biz_detail)
            event = construct_event(biz_detail)
            if validate_venue(venue):
                venuelist.append(venue) # adds the constructed venue to the list
                nvenues += 1
            if validate_event(event):
                eventlist.append(event) # adds the constructed event to the list
                nevents += 1
        if nbiz < 51:
            print("# of events added: {}".format(nevents))
            print("# of venues added: {}".format(nvenues))
            return
        offset += 50
        print('offset = {}'.format(offset))
        response = search_categories(API_KEY, categories, location, offset)
        nbiz = response.get('total')
        businesses = response.get('businesses')

    print("# of events added: {}".format(nevents))
    print("# of venues added: {}".format(nvenues))
    return




def main():

    try:
        query_api(input_values.categories, input_values.location, input_values.offset)

        venuesfile = open(venuefname,"w")
        eventsfile = open(eventfname, "w")

        json.dump(venuelist,venuesfile,indent="\t")
        json.dump(eventlist,eventsfile,indent='\t')

    except HTTPError as error:
            sys.exit(
                'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                    error.code,
                    error.url,
                    error.read(),
                )
            )


if __name__ == '__main__':
    main()
