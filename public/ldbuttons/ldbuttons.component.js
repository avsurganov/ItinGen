'use strict';

angular.module('ldButtons')

.component('ldButtons', {
	templateUrl: 'ldButtons/ldButtons.template.html',
	controller: ['$scope', 'itineraryFactory', 'Auth', function ldButtonsController($scope, itineraryFactory, Auth) {
		
		this.addToLikedItinerary = function() {

			if (Auth.isLoggedIn()) {
				// Check if the token expired
				Auth.getUser().then(function(data) {
					// Check if the returned user is undefined (expired)
					if (data.data.success == true) {
					  itineraryFactory.addToLikedItineraries()
					}
				});
			}
			this.nextItinerary();
		}

		this.nextItinerary = async function() {
			// itineraryFactory.saveSettings($scope.$parent.settings, $scope.$parent.location);
			await $scope.$parent.updateMapWithNewItinerary();
		}

		$(document).ready(function() {
   		$('[data-toggle="popover"]').popover({
      		placement: 'top',
      		trigger: 'hover'
   			});
		});
	}]
})