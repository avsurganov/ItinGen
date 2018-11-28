# Eventbrite API


## EB_api.py
	- Main class EB to be used by master database update function
		- Methods that get specified events and associated venues and returns json objects
	- Parent class Query with methods to make API calls
		- Subclass Search to do initial search for events
			- Main method make_jsons that returns jsons for each page of search results
			- Helper methods for venues and events
		- Subclass Ticket to get event pricing
			- Method to determine best price
		- Subclass Venue to create json object for a single venue
	- Class Event to create json object for a single event
	- Class Utility with some useful methods for other classes
		- Gets OAuth tokens
		- Formats dates and times properly
		- Checks for null values


## EB_tokens.py
	- Main class Tokens to store list of OAuth tokens
		- Method to add token
		- Method to get a valid token
	- Creates an instance of Tokens class for use in API calls

## EB_tests.py
	- Main class Tests to conduct testing
		- Tests event and venue json objects for type safety
		- Tests times for consistency
		- Tests latitude and longitude values for validity
		- Tests events and venues to ensure that the venue for every event is listed
	- Creates an instance of Tests class for testing data collection
		
	


