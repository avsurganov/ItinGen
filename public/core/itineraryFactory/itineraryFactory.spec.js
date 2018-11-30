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

	var testSettings0 = {
      startTime: new Date(Date.now()),
      startLocation: 'test12',
      free: true,
      radius: 10,
      transport: 'DRIVING'
    }

    var testSettings1 = {
      startTime: new Date(Date.now()),
      startLocation: 'test12',
      free: true,
      radius: 10,
      transport: 'DRIVING'
    }

    var testSettings2 = {
      startTime: '',
      startLocation: '',
      free: '',
      radius: '',
      transport: ''
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

	it('should save setting 0', function() {
		expect(factoryService.saveSettings(testSettings0, ' ')).toEqual(factoryService.settings);
	})

	it('should save setting 1', function() {
		expect(factoryService.saveSettings(testSettings1, ' ')).toEqual(factoryService.settings);
	})

	it('should save setting 2', function() {
		expect(factoryService.saveSettings(testSettings2, ' ')).toEqual(factoryService.settings);
	})

	it('should get liked itineraries', function() {
		
		expect(factoryService.getLikedItineraries()).toBeDefined()
	})

	it('should add to liked itineraries', function() {
		var length = factoryService.likedItineraries.length;
		factoryService.addToLikedItineraries()
		expect(length + 1).toEqual(factoryService.likedItineraries.length)
	})
})














