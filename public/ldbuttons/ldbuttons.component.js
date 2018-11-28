'use strict';

angular.module('ldButtons')

.component('ldButtons', {
	templateUrl: 'ldButtons/ldButtons.template.html',
	controller: ['$scope', 'itineraryFactory', function ldButtonsController($scope, itineraryFactory) {
		this.nextItinerary = function() {
			console.log($scope.$parent.test)
		}
		
	}]
})