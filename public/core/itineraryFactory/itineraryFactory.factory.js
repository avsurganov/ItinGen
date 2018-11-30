
angular.module('itineraryFactory')

.factory('itineraryFactory', ['$http', function($http) {
	//TODO: if logged in, make GET request to get users liked itineraries
	// Test itinerary for development 
	var event1 = {
          "venue_id": "5801 South Ellis Avenue Chicago, Illinois 60637",
          "event_name": "University of Chicago",
          "event_id": "yelpAkcZ1fUyB3RocKLYGFu20Q",
          "mon_start": 630,
          "mon_end": 1020,
          "tues_start": 630,
          "tues_end": 1020,
          "wed_start": 630,
          "wed_end": 1020,
          "thurs_start": 630,
          "thurs_end": 1200,
          "fri_start": 630,
          "fri_end": 1020,
          "sat_start": 630,
          "sat_end": 1020,
          "sun_start": 630,
          "sun_end": 1020,
          "tags": [
            "artschools",
            "landmarks",
            "artmuseums"
          ],
          "price": -10
         }

		venue1 = {
		          "venue_id": "yelpAkcZ1fUyB3RocKLYGFu20Q",
		          "venue_name": "Art Institute of Chicago",
		          "latlng": {lat: 41.8796, lng: -87.623713},
		          "address1": "111 S Michigan Ave",
		          "address2": "",
		          "address3": "",
		          "city": "Chicago",
		          "state": "IL",
		          "zip_code": "60603"
		         }

		event2 = {
		          "venue_id": "yelp8sZZM3Dr0G46JYBT9h599A",
		          "event_name": "International Museum of Surgical Science",
		          "event_id": "yelp8sZZM3Dr0G46JYBT9h599A",
		          "mon_start": 570,
		          "mon_end": 1020,
		          "tues_start": 570,
		          "tues_end": 1020,
		          "wed_start": 570,
		          "wed_end": 1020,
		          "thurs_start": 570,
		          "thurs_end": 1020,
		          "fri_start": 570,
		          "fri_end": 1020,
		          "sat_start": 600,
		          "sat_end": 1020,
		          "sun_start": 600,
		          "sun_end": 1020,
		          "tags": [
		            "museums",
		            "venues"
		          ],
		          "price": -10
		         }

		venue2 = {
		          "venue_id": "yelp8sZZM3Dr0G46JYBT9h599A",
		          "venue_name": "International Museum of Surgical Science",
		          "latlng": {lat: 41.9102601910586, lng: -87.6266419992433},
		          "address1": "1524 N Lake Shore Dr",
		          "address2": "",
		          "address3": "",
		          "city": "Chicago",
		          "state": "IL",
		          "zip_code": "60610"
		         }

		event3 = {
		          "event_id": "TMAPIvv1A7ZA8wGkdfoeXP",
		          "event_name": "Elton John: Farewell Yellow Brick Road",
		          "venue_id": "TMAPIKovZpa2MCe",
		          "start": 1200,
		          "end": -10,
		          "date": "02-16-2019",
		          "tags": [
		            "Music",
		            "Rock",
		            "Pop",
		            "Undefined",
		            "Undefined"
		          ],
		          "price": 59.5
		         }

		venue3 = {
		          "venue_id": "TMAPIKovZpa2MCe",
		          "venue_name": "Allstate Arena",
		          "latlng": {lat: 42.00499247, lng: -87.88750024},
		          "address1": "6920 North Mannheim Road",
		          "address2": "",
		          "address3": "",
		          "city": "Rosemont",
		          "state": "IL",
		          "zip_code": "60018"
		}


	var itin1 = [{event: event1, venue: venue1, start: "12:00", end: "3:00"},
        {event: event2, venue: venue2, start: "3:30", end: "5:00"}, 
        {event: event3, venue: venue3, start: "6:00", end: "8:00"}]
    var itin2 = [
        {event: event2, venue: venue2, start: "3:30", end: "5:00"}, 
        {event: event3, venue: venue3, start: "6:00", end: "8:00"},
        {event: event1, venue: venue1, start: "12:00", end: "3:00"}]
	var likedItineraries = [itin1, itin2]
	var itinerary = []
	var service = {}

	//on load or dislike an itinerary: 
	service.getNewItinerary = function() {
		//TODO: make GET request to backend for new itinerary
		return itin1
	}

	service.getCurrentItinerary = function() {
		return itin1
	}
	service.getLikedItineraries = function () {
		$http.get('/api/getliked').then((req) => {
			var success = req.data.success;
			if(success) {
				return req.data.itineraries;
			}
			else {
				var emptyArray = [];
				return emptyArray;
			}
		});
	}

	service.addToLikedItineraries = function (itineraries) {
		$http.post('/api/putliked', {itineraries}).then((req) => {
			return;
		});
	}


	return service
}])
