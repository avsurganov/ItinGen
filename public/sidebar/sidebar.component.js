'use strict';

angular.module('sideBar')

.component('sideBar', {
	templateUrl: 'sidebar/sidebar.template.html',
	controller: ['$scope', '$http', 'itineraryFactory', '$window', 'Auth', function sideBarController($scope, $http,itineraryFactory, $window, Auth) {
		
    $scope.itinerary = []
    $scope.likedItineraries = []
    $scope.settings = itineraryFactory.getSettings();
    $scope.isLoggedIn = false;

    if (Auth.isLoggedIn()) {
      // Check if a the token expired
      Auth.getUser().then(function(data) {
          // Check if the returned user is undefined (expired)

          if (data.data.success) {
            $scope.isLoggedIn = true;
            itineraryFactory.getLikedItineraries().then((req) => {
              var success = req.data.success;
              console.log(success)
              if(success) {
                console.log("got here")
                var likedItinerariesString = req.data.itineraries;
                if(likedItinerariesString != undefined){
                  $scope.likedItineraries = JSON.parse(likedItinerariesString);
                  itineraryFactory.setLikedItineraries($scope.likedItineraries);
                  console.log("On load, found users liked Itins");
                  console.log($scope.likedItineraries);
                }
              }
            });
          }
          else {
            console.log("User not in DB or token is expired");
          }
      });
  }
  else {
    console.log("No token saved in browser");
  }
    // Default settings
    // this.settings = {
    //   startTime: new Date(Date.now()),
    //   startLocation: '',
    //   free: true,
    //   radius: 10,
    //   transport: 'DRIVING'
    // }

    // itineraryFactory.saveSettings($scope.$parent.settings, $scope.$parent.location);



    this.generate = function() {
      $scope.$parent.updateMapWithNewItinerary();
    }

    $scope.$on('update', function(e) {
       $scope.itinerary = itineraryFactory.getCurrentItinerary();
      //  $scope.$apply()
    }.bind(this))

    this.intToChar = function($index) {
      return String.fromCharCode(65 + $index)
    }

    this.logout = function(){
      Auth.logout();
      $scope.isLoggedIn = false;
    }
  
    this.facebook = function() {
      $window.location = $window.location.protocol + '//' + $window.location.host + '/auth/facebook';
      };

    this.home = function() {
       this.sidebarTemplate = sidebarTemplates[0]
      //  this.itinerary = itineraryFactory.getNewItinerary()
    }

    this.getLikedItineraries = function() {
      if($scope.isLoggedIn){
        this.sidebarTemplate = sidebarTemplates[1]
        this.likedItineraries = itineraryFactory.getcurrentLikedItineraries();
      } 
    }

    this.showElements = function(index) {
      var numEventsInItinerary = this.likedItineraries[index].length;
      let i;
      for (i = 0; i < numEventsInItinerary; i++) {
        var elementClasses = document.getElementById('collapseDetail' + index + i).classList
        if (elementClasses.length == 1)
          $('#collapseDetail' + index + i).collapse('show')
        else
          $('#collapseDetail' + index + i).collapse('hide')
      }
    }

    this.saveSettings = function(settings) {
      console.log(settings);
      itineraryFactory.saveSettings(settings);
    }

    this.assignTransport = function(transport) {
      $scope.settings.transport = transport;
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


