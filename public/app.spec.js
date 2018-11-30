describe('itinGenController', function() {
	beforeEach(module('ItinGen'));

	it('should create a `map` model with a map', inject(function($controller) {
		var scope = {};
		var ctrl = $controller('itinGenController', {$scope: scope});

		expect(scope.map).toBeDefined();
	}))
})