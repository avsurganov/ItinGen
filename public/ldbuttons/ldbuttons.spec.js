'use strict';

describe('button tester', function(){ 
	var $factoryService, ctrl;



	beforeEach(inject(function($componentController, _$factoryService_){
		$factoryService = _$factoryService_;
		ctrl = $componentController.get('ldButtonsController');
	}));




	// beforeEach(inject(function(_$factoryService_){
	// 	inject(function($injector) {
	// 	factoryService = $injector.get('itineraryFactory');
	// 	control = $injector.get('ldButtonsController')};
	// 	$controller = _$controller_;
	// ));

		// function() {
		// module('ldButtons');
		// inject(function($injector) {
		// 	factoryService = $injector.get('itineraryFactory');

		// control = $injector.get('ldButtonsController')
		// })
	// })

	describe('controller exist', function(){
		it("controller should exist", function(){
			expect(control).toBeDefined();
		})
	})
})
	

// describe('itinerary factory module', function() {
// 	var factoryService;
// 	let http;

// 	beforeEach(function() {
// 		module('itineraryFactory');
// 		inject(function($injector) {
// 			factoryService = $injector.get('itineraryFactory');
// 			http = $injector.get('$http')
// 		});
// 	});