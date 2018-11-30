'use strict';

angular.module('ldButtons')

.component('ldButtons', {
	templateUrl: 'ldButtons/ldButtons.template.html',
	controller: ['$scope', 'itineraryFactory', function ldButtonsController($scope, itineraryFactory) {
		
		this.addToLikedItinerary = function() {
			itineraryFactory.addToLikedItineraries()
			this.nextItinerary();
		}

		this.nextItinerary = function() {
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