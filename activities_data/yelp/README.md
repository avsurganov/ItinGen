# This folder contains the implementation for calls to the Yelp API

## How to Use
Calls to the Yelp API can be made from the command line by typing “python get_yelpdata.py”. Additional optional parameters include:

- Location: specify with -l or --location. Default is Chicago, IL
- Category: specify with -c or —categories. Default is museums, though the way most data is collected is by using this flag to construct JSON files with events and venues from a variety of Yelp categories. Relevant categories for the Yelp API are specified below.
- Offset: specify with -o or —offset. Indicates which “page” of results you want returned from the API request, where each “page” includes 50 businesses. Default is 50, and the program automatically accesses subsequent pages for categories with more than 50 businesses.


## Files in this Folder
- get_yelpdata.py: the main program. Queries the API by location, category, offset, etc. When run with a specified category, creates two JSON files, one with the venues for businesses in that category, and one with the events for businesses in that category.
- validation.py: includes various validation tests for venue and event dictionaries
- unittests.py: unit tests for various functions in get_yelpdata.py and validation.py


## Relevant Categories
The database is populated with business data from the Yelp API for businesses that fall within the following categories (as defined by Yelp), plus numerous food, nightlife, and restaurant categories that have been omitted for brevity’s sake:
	-aquariums
	-culturalcenter
	-farms
	-fleamarkets
	-galleries
	-gardens
	-landmarks
	-localflavor
	-museums
	-observatories
	-paintandsip
	-planetarium
	-publicmarkets
	-trampoline
	-zoos








