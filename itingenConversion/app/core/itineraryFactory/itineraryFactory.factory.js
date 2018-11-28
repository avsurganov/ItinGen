
angular.module('itineraryFactory')

.factory('itineraryFactory', function() {
	//TODO: if logged in, make GET request to get users liked itineraries
	var likedItineraries = []
	var itinerary = []
	var service = {}

	//on load or dislike an itinerary: 
	service.getNewItinerary = function() {
		//TODO: make GET request to backend
		var newItin = [{lat: 1, lng: 2}]
		return newItin
	}

	service.getLikedItineraries = function () {
		return likeItineraries
	}

	service.addToLikedItineraries = function (itineraryObj) {
		likedItineraries.push(itineraryObj)
		// TODO: add POST request to add new liked itinerary
		return likeItineraries
	}


	return service
})
