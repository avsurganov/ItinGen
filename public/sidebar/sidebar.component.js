'use strict';

angular.module('sideBar')

.component('sideBar', {
	templateUrl: 'sidebar/sidebar.template.html',
	controller: ['$scope', '$http', 'itineraryFactory', '$window', 'Auth', '$route', function sideBarController($scope, $http,itineraryFactory, $window, Auth, $route) {
		
    $scope.itinerary = []
    $scope.likedItineraries = []
    $scope.settings = itineraryFactory.getSettings();
    $scope.isLoggedIn = false;
    var state = "IL"

    console.log($scope.settings)
    $http.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=' + $scope.settings.startLocation.lat + ',' + $scope.settings.startLocation.lng + '&key=AIzaSyArSWwjXq_NL9lBNgYfwPtFInt4hM4Iia0').then((res) => {
      console.log(res.data.results[0].formatted_address)
      $scope.settings.startLocationDisplay = res.data.results[0].formatted_address
    })
    

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
  


    this.generate = function() {
      $scope.$parent.updateMapWithNewItinerary();
      var hide = document.getElementById("intro_message");
      hide.style.display = "none";
      var like_b = document.getElementById("like");
      like_b.style.display = "inline";
      var dislike_b = document.getElementById("dislike");
      dislike_b.style.display = "inline";
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
      itineraryFactory.setLikedItineraries([]);
      $scope.isLoggedIn = false;
      $window.location.reload();
    }
  
    this.facebook = function() {
      $window.location = $window.location.protocol + '//' + $window.location.host + '/auth/facebook';
      };

    this.home = function() {
      if (itineraryFactory.getCurrentItinerary().length == 0){
        var hide = document.getElementById("intro_message");
        hide.style.display = "inline";
      };
       this.sidebarTemplate = sidebarTemplates[0]
      //  this.itinerary = itineraryFactory.getNewItinerary()
    }

    this.getLikedItineraries = function() {
      var hide = document.getElementById("intro_message");
      hide.style.display = "none";
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

      // check for undefined fields
      

      console.log($scope.settings.startLocationDisplay)
      // convert string address to latlng object for backend processing
      if ($scope.settings.startLocationSelect == "givenLocation") {
        $http.get('https://maps.googleapis.com/maps/api/geocode/json?address='+$scope.settings.startLocationDisplay +'&key=AIzaSyArSWwjXq_NL9lBNgYfwPtFInt4hM4Iia0').then((res) => {
         var boundLocation = res.data.results[0].formatted_address.search(state)
         if (boundLocation == -1) {
            alert("You're start location must be within the state of Illinois")
            return;
         }
          $scope.settings.startLocation = res.data.results[0].geometry.location
          console.log(settings)
          itineraryFactory.saveSettings(settings);
          alert("Settings successfully saved!")
        })
      } else {
          console.log(settings)
          itineraryFactory.saveSettings(settings);
          alert("Settings successfully saved!")
      }
      
    }

    // this.assignTransport = function(transport) {
    //   $scope.settings.transport = transport;
    // }

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


