'use strict';

angular.module('ldButtons')

.component('ldButtons', {
	templateUrl: 'ldButtons/ldButtons.template.html',
	controller: ['$scope', 'itineraryFactory', 'Auth', function ldButtonsController($scope, itineraryFactory, Auth) {
		
		this.addToLikedItinerary = function() {

			if (Auth.isLoggedIn()) {
				// Check if a the token expired
				Auth.getUser().then(function(data) {
					// Check if the returned user is undefined (expired)
					if (data.data.email === undefined) {
					} else {
					  itineraryFactory.addToLikedItineraries()
					}
				});
			}
			this.nextItinerary();
		}

		this.nextItinerary = function() {
			console.log($scope.$parent.settings);
			console.log($scope.$parent.location);
			itineraryFactory.saveSettings($scope.$parent.settings, $scope.$parent.location);
			$scope.$parent.updateMapWithNewItinerary();
		}

		$(document).ready(function() {
   		$('[data-toggle="popover"]').popover({
      		placement: 'top',
      		trigger: 'hover'
   			});
		});
	}]
})