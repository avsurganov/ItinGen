console.log('testintingtes')
angular.module('appRoutes', ['ngRoute'])

// Configure Routes; 'authenticated = true' means the user must be logged in to access the route
.config(function($routeProvider, $locationProvider) {

    console.log("HEREEE");
    // AngularJS Route Handler
    $routeProvider

    // Route: Home             
    .when('/', {
        template: ''
    })

    // Route: Facebook Callback Result            
    .when('/facebook/:token', {
        template: '',
        controller: 'facebookCtrl',
        controllerAs: 'facebook'
    })

    .otherwise({ redirectTo: '/' }); // If user tries to access any other route, redirect to home page

    $locationProvider.html5Mode({ enabled: true, requireBase: false }); // Required to remove AngularJS hash from URL (no base is required in index file)
});

