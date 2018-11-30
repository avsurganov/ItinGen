'use strict';

angular.module('sideBar')

.component('sideBar', {
	templateUrl: 'sidebar/sidebar.template.html',
	controller: ['$scope', '$http', 'itineraryFactory', '$window', function sideBarController($scope, $http,itineraryFactory, $window) {
		
    this.itinerary = []
    this.likedItineraries = []
    // Default settings
    console.log($scope.$parent.$displayLocation)
    this.settings = {
      startTime: new Date(Date.now()),
      startLocation: $scope.$parent.$displayLocation,
      free: true,
      radius: 10,
      transport: 'DRIVING'
    }

    this.generate = function() {
      itineraryFactory.addToLikedItineraries()
      $scope.$parent.updateMapWithNewItinerary();
    }

    this.startLocation
    $scope.$on('update', function(e) {
       this.itinerary = itineraryFactory.getCurrentItinerary();
       console.log(this.itinerary)
       $scope.$apply()
    }.bind(this))

    this.intToChar = function($index) {
      return String.fromCharCode(65 + $index)
    }

  
    this.facebook = function() {
      $window.location = $window.location.protocol + '//' + $window.location.host + '/auth/facebook';
      };

    this.home = function() {
       this.sidebarTemplate = sidebarTemplates[0]
       this.itinerary = itineraryFactory.getNewItinerary()
    }

    this.getLikedItineraries = function() {
      console.log("switching!")
      this.sidebarTemplate = sidebarTemplates[1]
      this.likedItineraries = itineraryFactory.getLikedItineraries()
      console.log(this.likedItineraries)

    }

    this.showElements = function(index) {
      var numEventsInItinerary = this.likedItineraries[index].length;
      let i;
      for (i = 0; i < numEventsInItinerary; i++) {
        var elementClasses = document.getElementById('collapseDetail' + index + i).classList
        console.log(elementClasses.length)
        if (elementClasses.length == 1)
          $('#collapseDetail' + index + i).collapse('show')
        else
          $('#collapseDetail' + index + i).collapse('hide')
      }
    }

    this.saveSettings = function() {
      console.log(this.settings)
      itineraryFactory.saveSettings(this.settings)
    }

    this.assignTransport = function(transport) {
      this.settings.transport = transport
    }

    var sidebarTemplates = ['sidebar/itineraries.htm', 'sidebar/likeditineraries.htm']
    this.sidebarTemplate = sidebarTemplates[0]
	}]
})

// DOM Ready
$(function() {
 var el, newPoint, newPlace, offset;
 
 // Select all range inputs, watch for change
 $("input[type='range']").change(function() {
 
   // Cache this for efficiency
   el = $(this);
   
   // Measure width of range input
   width = el.width();
   
   // Figure out placement percentage between left and right of input
   newPoint = (el.val() - el.attr("min")) / (el.attr("max") - el.attr("min"));
   
   // Janky value to get pointer to line up better
   offset = -1.3;
   
   // Prevent bubble from going beyond left or right (unsupported browsers)
   if (newPoint < 0) { newPlace = 0; }
   else if (newPoint > 1) { newPlace = width; }
   else { newPlace = width * newPoint + offset; offset -= newPoint; }
   
   // Move bubble
   el
     .next("output")
     .css({
       left: newPlace,
       marginLeft: offset + "%"
     })
     .text(el.val());
 })
 // Fake a change to position bubble at page load
 .trigger('change');
});


