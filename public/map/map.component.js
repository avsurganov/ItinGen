'use strict';

angular.module('googleMap')

// .config(['$routeProvider', function($routeProvider) {
//   $routeProvider.when('/home', {
//     templateUrl: 'map/map.html',
//     controller: 'View1Ctrl'
//   });
// }])

.component('googleMap', {
	templateUrl: 'map/map.template.html',
	controller: [function mapController() {
		// Instantiate google map immediately on load
		
	}]
});