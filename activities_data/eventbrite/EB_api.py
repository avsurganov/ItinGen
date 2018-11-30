import requests
import json
import datetime
from EB_tokens import *
from EB_tests import *

class Utility:
	def get_token():
		return EB_tokens.next_token()

	def split_date_and_time(dt):
		return dt.split('T')

	def time_to_mins(time):
		split = time.split(':')
		return 60*int(split[0]) + int(split[1])

	def format_date(date):
		return date[5:] + '-' + date[:4]

	def compare_dates(date1, date2):
		d1 = datetime.datetime.strptime(date1, '%Y-%m-%d').date()
		d2 = datetime.datetime.strptime(date2, '%Y-%m-%d').date()
		return (d2-d1).days

	def check_null (attribute, value):
		if attribute is None:
			return value
		else:
			return attribute

#parent class for all types of queries

class Query:
	def __init__(self, query):
		self.URI = 'https://www.eventbriteapi.com/v3/'
		invalid_query = True
		while (invalid_query):
			search = requests.get(self.URI + query + Utility.get_token())
			if (search.status_code == 200):
				invalid_query = False
				self.query = query
				self.page = 0
				self.json = {}
				self.all_data = search.json()

	#advances to the next page of results
	def next_page(self):
		self.page += 1
		search = requests.get(self.URI+self.query+Utility.get_token()+'&page='+str(self.page))
		self.all_data = search.json()
		if (search.status_code != 200 or int(self.all_data.get('pagination').get('page_count')) < self.page):
			return False
		else:
			return True

#class responsible for searching for events

class Search(Query):
	#creates json object for all events in search and compiles list of venues
	def get_events(self):
		self.events_json = {}
		self.events_json['events'] = []
		self.venue_set = set()
		for e in self.all_data.get('events'):
			self.venue_set.add(e.get('venue_id'))
			self.events_json['events'].append(self.event_json(e))
		return self.events_json

	#creates json object for single event
	def event_json(self, event):
			event_id = event.get('id')
			price = float(0)
			if (not event.get('is_free')):
				ticket = Ticket('events/' + event_id + '/ticket_classes/?token=')
				price = ticket.get_price()
			e = Event(event, price)
			return e.make_json()

	#creates json object for all venues in search
	def get_venues(self):
		self.venues_json = {}
		self.venues_json['venues'] = []
		for v in self.venue_set:
			venue = Venue('venues/' + v + '?token=')
			self.venues_json['venues'].append(venue.make_json())
		return self.venues_json

	#returns event and venue json objects
	def make_jsons(self):
		return [self.get_events(), self.get_venues()]


#class for getting price for event
class Ticket(Query):
	def get_price(self):
		min_price = float('inf')
		for t in self.all_data.get('ticket_classes'):
			if (not t.get('free') and (not t.get('donation'))):
				price = float(t.get('cost').get('major_value'))
				if (price<min_price):
					min_price = price
		if (min_price == float('inf')):
			min_price = float(-10)
		return min_price

#class for creating json object for single venue
class Venue(Query):
	#creates json object for venue
	def make_json(self):
		address = self.all_data.get('address')
		self.json['venue_id'] = 'EB_' + Utility.check_null(str(self.all_data.get('id')), '')
		self.json['venue_name'] = Utility.check_null(self.all_data.get('name'), '')
		self.json['latitude'] = Utility.check_null(float(address.get('latitude')), float(999))
		self.json['longitude'] = Utility.check_null(float(address.get('longitude')), float(999))
		self.json['address1'] = Utility.check_null(address.get('address_1'), '')
		self.json['address2'] = Utility.check_null(address.get('address_2'), '')
		self.json['address3'] = ''
		self.json['city'] = Utility.check_null(address.get('city'), '')
		self.json['state'] = Utility.check_null(address.get('region'), '')
		self.json['zip_code'] = Utility.check_null(address.get('postal_code'), '')
		EB_tests.venue_valid(self.json)
		return self.json


#class for creating json object for single event
class Event:
	def __init__(self, event, price):
		self.event = event
		self.price = price
	#creates json object for event
	def make_json(self):
		self.json = {}
		self.json['event_id'] = 'EB_' + Utility.check_null(str(self.event.get('id')), '')
		self.json['event_name'] = Utility.check_null(self.event.get('name').get('text'), '')
		self.json['venue_id'] = 'EB_' + Utility.check_null(str(self.event.get('venue_id')), '')
		start = self.event.get('start').get('local')
		end = self.event.get('end').get('local')
		s_split = Utility.split_date_and_time(start)
		e_split = Utility.split_date_and_time(end)
		self.json['start'] = Utility.check_null(Utility.time_to_mins(s_split[1]), -10)
		self.json['end'] = Utility.check_null(Utility.time_to_mins(e_split[1])+1440*Utility.compare_dates(s_split[0], e_split[0]), -10)
		self.json['date'] = Utility.check_null(Utility.format_date(s_split[0]), '')
		self.json['tags'] = ''
		self.json['price'] = self.price
		EB_tests.event_valid(self.json)
		return self.json

#class that houses all functions to be called by main database update function
class EB:

	#main function to create all json objects and write them to files
	def query_EB_api(self, query):
		event_json = {}
		venue_json = {}
		search = Search(query)
		jsons = search.make_jsons()
		event_json = jsons[0].get('events')
		venue_json = jsons[1].get('venues')
		while search.next_page():
			jsons = search.make_jsons()
			event_json = event_json + jsons[0].get('events')
			venue_json = venue_json + jsons[1].get('venues')
		EB_tests.time_valid(event_json)
		EB_tests.lat_long_valid(venue_json)
		EB_tests.venue_id_valid(event_json, venue_json)
		EB_tests.display_test_results()
		return[venue_json, event_json]

	#gets all events from the current day
	def query_EB_api_today(self):
		return self.query_EB_api('events/search/?location.address=chicago&start_date.keyword=today&token=')

	#gets all listed events
	def query_EB_api_all(self):
		return self.query_EB_api('events/search/?location.address=chicago&token=')
