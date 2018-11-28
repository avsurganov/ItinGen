'use strict';

angular.module('sideBar')

.component('sideBar', {
	templateUrl: 'sidebar/sidebar.template.html',
	controller: ['$scope', 'itineraryFactory', function sideBarController($scope, itineraryFactory) {
		
		this.drawLikedItineraries = function() {
			console.log($scope.$parent.test)
		}
	}]
})