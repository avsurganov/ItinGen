'use strict';

// Declare app level module which depends on views, and core components
angular.module('ItinGen', [
	'ldButtons',
	'itineraryFactory',
	'sideBar',
	'introduction'
])



.controller('itinGenController', ['$scope', '$http', 'itineraryFactory', function($scope, $http, itineraryFactory) {
  
  var currentItinerary = {}
  var directionsService 
  var directionsDisplay
  var test_params = {"username" : "test_username", "password" : "test_password", "tag" : "test_tag", "email" : "test_email"};
  $scope.test = "We got it!"
  $http({url: '/api/users', method: 'POST', params: test_params}).then((res) => {
	  console.log(res);
  });

  
     var map;
     function initMap(x, y) {
     	directionsService = new google.maps.DirectionsService();
     	directionsDisplay = new google.maps.DirectionsRenderer();
        map = new google.maps.Map(document.getElementById('map'), {
	        center: {lat: x, lng: y},
	        zoom: 13
        });
        directionsDisplay.setMap(map);
    }
    function onPositionRecieved(position){
      var coords = position.coords;
      initMap(coords.latitude, coords.longitude);
    }
    // error if initial position not recieved
    function locationNotRecieved(positionError){
      console.log(positionError);
    }

    // set position on map when position tracking coords received
    function watchCoordinatesRecieved(pos) {
      var coords = pos.coords
      marker.setPosition({lat: coords.latitude, lng: coords.longitude})
    }

    // begin watch position for movement tracking
    function beginPositionWatch() {
      navigator.geolocation.watchPosition(watchCoordinatesRecieved, locationTrackNotRecieved, options)
    }

    // Check if DOM navigator object exists
    (function init() {
      if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(onPositionRecieved, locationNotRecieved);
      }
    })()


  function drawNewItinerary() {
  	var waypoints = []
  	for (event in currentItinerary) {
  		var index = parseInt(event) + 1
  		if (index != currentItinerary.length)
  			waypoints.push({location: currentItinerary[index].venue.latlng}) 
  	}

  	var directionRequest = {
		origin: currentItinerary[0].venue.latlng,
		destination: currentItinerary[currentItinerary.length - 1].venue.latlng,
		travelMode: 'DRIVING',
		waypoints: waypoints
  	}
  	directionsService.route(directionRequest, function(result, status) {
  		if (status == 'OK') {
  			directionsDisplay.setDirections(result)
  		}
  	})
  	
  }

  $scope.updateMapWithNewItinerary = function() {
  	currentItinerary = itineraryFactory.getNewItinerary()
  	drawNewItinerary()
  }




}])




