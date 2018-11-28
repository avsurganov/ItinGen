'use strict';

// Declare app level module which depends on views, and core components
angular.module('ItinGen', [
	'ldButtons',
	'itineraryFactory',
	'sideBar',
	'introduction'
])



.controller('itinGenController', ['$scope', '$http', 'itineraryFactory', function($scope, $http, itineraryFactory) {
  
  var test_params = {"username" : "test_username", "password" : "test_password", "tag" : "test_tag", "email" : "test_email"};
  $scope.test = "We got it!"
  $http({url: '/api/users', method: 'POST', params: test_params}).then((res) => {
	  console.log(res);
  });

}])




