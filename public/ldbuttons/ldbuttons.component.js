'use strict';

angular.module('ldButtons')

.component('ldButtons', {
	templateUrl: 'ldButtons/ldButtons.template.html',
	controller: ['$scope', 'itineraryFactory', 'Auth', function ldButtonsController($scope, itineraryFactory, Auth) {
		
		this.addToLikedItinerary = async function() {
			console.log("SHOULD NOT GET HERE")
			if (Auth.isLoggedIn()) {
				// Check if the token expired
				Auth.getUser().then(function(data) {
					// Check if the returned user is undefined (expired)
					if (data.data.success == true) {
					  itineraryFactory.addToLikedItineraries().then((res) => {
						  console.log(res);
					  })
					}
				});
			}
			await this.nextItinerary();
		}

		this.nextItinerary = async function() {
			console.log("SHOUDLGET HERE")
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