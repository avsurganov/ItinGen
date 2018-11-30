'use strict';

// describe('itineraryFactory module', function() {
//   var itineraryFactory = {};
//   beforeEach(module('itineraryFactory'));
//   beforeEach(inject(function(itineraryFactory) {
//   	itineraryFactory = itineraryFactory 
//   }))
//   describe('itineraryFactory factory', function(){

//     it('should ....', function () {
//       //spec body
      
//       expect(itineraryFactory).toBeDefined();
//     });

//   });
// });

describe('itinerary factory module', function() {
	var factoryService;
	var http;

	beforeEach(function() {
		module('itineraryFactory');
		inject(function($injector) {
			factoryService = $injector.get('itineraryFactory');
			http = $injector.get('$http')
		});
	});

	it('should exist', function() {
		expect(factoryService).toBeDefined();
	})

	it('get new itinerary', function() {
		expect(factoryService.getNewItinerary).toBeDefined();
	})
})