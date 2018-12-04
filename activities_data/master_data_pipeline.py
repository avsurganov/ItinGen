# this is the master data pipeline file, all of the different api calls will
# be made from here and distributed to the correct data folder
import datetime
import sys
import os
# api functions
sys.path.insert(0, "eventbrite")
from EB_api import *
sys.path.insert(0, "ticketmaster")
from tm_api import *
# we do not actually need to import the yelp file for now
# can be run from the command line
# sys.path.insert(0, "yelp")
# from get_yelpdata import *


# museums = ["aquariums", "culturalcenter", "galleries", "museums",
#             "observatories", "planetarium", "zoos",
#             ]
# publicattractions = ["gardens", "landmarks", "localflavor"]
# nightlife = ["adultentertainment", "barcrawl", "beerbar", "champagnebars",
#                 "cigarbars", "cocktailbars", "divebars", "drivethrubars",
#                 "gaybars", "hookah_bars", "irish_pubs", "lounges",
#                 "pubs", "speakeasies", "sportsbars", "tikibars",
#                 "vermouthbars", "whiskeybars", "wine_bars", "beergardens",
#                 "clubcrawl", "comedyclubs", "countrydancehalls", "danceclubs",
#                 "jazzandblues", "karaoke", "pianobars", "poolhalls",
#                 "cabaret", "casinos", "wineries", "breweries",
#                 "distilleries"
#                 ]
# misc = ["farms", "fleamarkets", "paintandsip", "publicmarkets",
#         "trampoline", "bowling", "escapegames", "golf",
#         "minigolf", "paintball", "lasertag", "scavengerhunts",
#         "waterparks", "arcades", "hauntedhouses", "saunas",
#         "amusementparks", "psychic_astrology", "virtualrealitycenters"
#         ]
# food = ["acaibowls",
#            "bagels",
#            "bakeries",
#            "bento",
#            "bubbletea",
#            "chimneycakes",
#            "churros",
#            "cideries",
#            "coffee",
#            "cupcakes",
#            "delicatessen",
#            "desserts",
#            "diyfood",
#            "donuts",
#            "empanadas",
#            "farmersmarket",
#            "foodtrucks",
#            "gelato",
#            "icecream",
#            "jpsweets",
#            "juicebars",
#            "cakeshop",
#            "poke",
#            "pretzels",
#            "streetvendors",
#            "tea",
#            "afghan",
#             "african",
#             "newamerican",
#             "tradamerican",
#             "arabian",
#             "argentine",
#             "armenian",
#             "asianfusion",
#             "australian",
#             "austrian",
#             "bangladeshi",
#             "bbq",
#             "basque",
#             "belgian",
#             "brasseries",
#             "brazilian",
food = [            "breakfast_brunch",
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

categories = []
# categories.extend(museums)
# categories.extend(publicattractions)
# categories.extend(nightlife)
# categories.extend(misc)
categories.extend(food)


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


def master_data():
    '''
    master data function that will run all of the individual api calls and
    dump the json files into the correct place

    inputs:
        None
    outputs:
        success (int) - 0 for success and 1 for failure
    '''
    # header file paths
    VEN = "../app/activities_data/venues/"
    TMP = "../app/activities_data/tmp_events/"
    EVN = "../app/activities_data/events/"

#data
    print("\n###################")
    print("# EVENTBRITE DATA #")
    print("###################\n")
    # keeping the same demo call that was provided
    EB_demo = EB()
    eb_v, eb_e = EB_demo.query_EB_api_today() # return venue json, events json
    # write to file
    eb_venue_of = VEN + "eb_venues_" + get_date() + ".json"
    eb_event_of = TMP + "eb_events_" + get_date() + ".json"
    with open(eb_venue_of, "w") as fp:
        json.dump(eb_v, fp, indent=2)
    with open(eb_event_of, "w") as fp:
        json.dump(eb_e, fp, indent=2)


    print("\n#####################")
    print("# TICKETMASTER DATA #")
    print("#####################\n")
    # run the main tm function
    tm_v, tm_s, tm_m = run_tm_pipeline() # venue, sport events, music events
    # write to file
    tm_venue_of = VEN + "tm_venues_" + get_date() + ".json"
    tm_s_event_of = TMP + "tm_sports_events_" + get_date() + ".json"
    tm_m_event_of = TMP + "tm_music_events" + get_date() + ".json"
    with open(tm_venue_of, "w") as fp:
        json.dump(tm_v, fp, indent=2)
    with open(tm_s_event_of, "w") as fp:
        json.dump(tm_s, fp, indent=2)
    with open(tm_m_event_of, "w") as fp:
        json.dump(tm_m, fp, indent=2)


    print("\n#############")
    print("# YELP DATA #")
    print("#############\n")
    # yelp script already does the correct writing into the folders
    # just need to call the script
    # this runs on UNIX
    # eventually will switch this out for a better way to do all of the
    # category calls but for now we do not have enough API keys
    # this call should automatically place into correct folder
    for c in categories:
        os.system("python3 yelp/get_yelpdata.py -c " + c)

master_data()
