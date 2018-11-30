
angular.module('itineraryFactory')

.factory('itineraryFactory', ['$http', function($http) {
	//TODO: if logged in, make GET request to get users liked itineraries
	// Test itinerary for development 

	var likedItineraries = []
	var currentItinerary = []
	var settings = {}
	var service = {}


	//on load or dislike an itinerary: 
	service.getNewItinerary = function() {
		console.log("SETTINGS ARE");
		console.log(settings);
		return $http.post('/api/getitinerary', {settings});
	}



	service.saveSettings = function(userSettings, defaultLocation) {
		console.log("in save settings");
		console.log(defaultLocation)
		console.log(userSettings)
		settings = userSettings;
		if(settings['startLocation'] == '' || settings['startLocation'] == undefined) {
			settings['startLocation'] = defaultLocation;
		}
		console.log(settings)
	}


	service.getCurrentItinerary = function() {
		return currentItinerary
	}

	service.setCurrentItinerary = function(current) {
		currentItinerary = current;
	}

	service.getLikedItineraries = function () {
		return $http.get('/api/getliked');
	}

	service.addToLikedItineraries = function () {
		if(currentItinerary.length > 0)
			likedItineraries.push(currentItinerary)
		console.log("got here");
		console.log(likedItineraries);
		$http.post('/api/putliked', {likedItineraries}).then((data) => {
			console.log('putlike');
			console.log(data.data);
		});
	}


	return service
}])
