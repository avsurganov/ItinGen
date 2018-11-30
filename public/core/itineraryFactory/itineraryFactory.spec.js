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
	let http;

	beforeEach(function() {
		module('itineraryFactory');
		inject(function($injector) {
			factoryService = $injector.get('itineraryFactory');
			http = $injector.get('$http')
		});
	});

	var testSettings = {
      startTime: new Date(Date.now()),
      startLocation: '',
      free: true,
      radius: 10,
      transport: 'DRIVING'
    }
	
	it('should exist', function() {
		expect(factoryService).toBeDefined();
	})

	it('should get new itinerary', function() {
		expect(factoryService.getNewItinerary()).toBeDefined();
	})

	it('should make post request to get new itinerary', function() {
		expect(http).toBeDefined();
	})

	it('should make post request to get new itinerary', function() {
		expect(factoryService.getCurrentItinerary()).toBeDefined();
	})

	it('should save setting', function() {
		expect(factoryService.saveSettings()).toBeDefined();
	})
})