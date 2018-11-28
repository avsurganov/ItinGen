'use strict';

// Declare app level module which depends on views, and core components
angular.module('ItinGen', [
	'ldButtons',
	'itineraryFactory',
	'sideBar',
	'introduction'
])



.controller('itinGenController', ['$scope', 'itineraryFactory', function($scope, itineraryFactory) {
  
  $scope.test = "We got it!"


}])




