
angular.module('itineraryFactory')

.factory('itineraryFactory', ['$http', function($http) {

	var likedItineraries = []
	var currentItinerary = []
	var userLocationCoords;
	// default location is center of chicago
	var chicagoCenterCoords = {lat: 41.881855, lng: -87.627115};
	var now = new Date(Date.now())

	var defaultHour = appendZero(convertFromMilitary(now.getHours()))
	var defaultMin = appendZero(snapToNearest15(now.getMinutes()))
	var defaultSection = amOrPm(now.getHours())
	var settings = {
		startTimeHours: defaultHour,
		startTimeMinute: defaultMin,
		startTimeSection: defaultSection,
		startTime: defaultHour + ':' + defaultMin + ' ' + defaultSection,
		startLocation: chicagoCenterCoords,
		startLocationSelect: "chicagoCenter",
		free: "true",
		radius: 5,
		transport: 'DRIVING'
	};

	var service = {}

	console.log(new Date(Date.now()))

	function amOrPm (hours) {
		if (hours < 12)
			return 'AM'
		else
			return 'PM'
	}

	function convertFromMilitary(hours) {
		var hour = hours % 12;
		if (hour == 0)
			return 12
		else 
			return hour
	}

	function snapToNearest15(minutes) {
		console.log(minutes)
		if (minutes < 15)
			return 15
		else if (minutes < 30)
			return 30
		else if (minutes < 45)
			return 45
		else 
			return 0
	}

	function appendZero (num) {
		if (num < 10)
			return '0' + num
		else 
			return num.toString()
	}


	//on load or dislike an itinerary: 
	service.getNewItinerary = function() {
	
		return $http.post('/api/getitinerary', {settings});
	}



	service.saveSettings = function(userSettings) {
		userSettings.startTime = userSettings.startTimeHours + ':' + userSettings.startTimeMinute 
		+ ' ' + userSettings.startTimeSection
		if (userSettings.startLocationSelect == "chicagoCenter")
			userSettings.startLocation = chicagoCenterCoords
		else if (userSettings.startLocationSelect == "currentLocation" && userLocationCoords != undefined)
			userSettings.startLocation = userLocationCoords
		settings = userSettings 
		

		console.log('new settings');
		console.log(settings);
	}

	service.setTransport = function(transport) {
		setts.transport = transport;
	}


	service.getCurrentItinerary = function() {
		return currentItinerary
	}


	service.getSettings = function() {
		return settings;
	}

	service.setCurrentItinerary = function(current) {
		currentItinerary = current;
	}

	service.setLikedItineraries = function(likedItins) {
		likedItineraries = likedItins;
	}

	service.getcurrentLikedItineraries = function () {
		return likedItineraries;
	}


	service.getLikedItineraries = function () {
		return $http.get('/api/getliked');
	}

	service.setUserLocation = function (location) {
		userLocationCoords = location
	}

	service.addToLikedItineraries = function () {
		console.log("got to add to liked itinfactory here");
		if(currentItinerary.length > 0){
			likedItineraries.push(currentItinerary);
			console.log("Adding itinerary...")
			console.log(currentItinerary);
			$http.post('/api/putliked', {likedItineraries}).then((data) => {
				console.log("Adding itineraries is a " + data.data.success);
			});
		} else {
			console.log("current itinerary is empty");
		}
	}


	return service
}])
