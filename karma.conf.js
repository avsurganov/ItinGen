//jshint strict: false
module.exports = function(config) {
  config.set({

    basePath: './public',
// removed factory b/c of failure to load
    files: [
      'lib/angular/angular.js',
      'lib/angular-route/angular-route.js',
      '../node_modules/angular-mocks/angular-mocks.js',
      'view*/**/*.js',
      'core/itineraryFactory/itineraryFactory.module.js',
      'core/itineraryFactory/itineraryFactory.factory.js',
      'core/itineraryFactory/itineraryFactory.spec.js',
      'app.js',
      'app.spec.js'
    ],

    autoWatch: true,

    frameworks: ['jasmine'],

    browsers: ['Chrome'],

    plugins: [
      'karma-chrome-launcher',
      'karma-firefox-launcher',
      'karma-jasmine'
    ]

  });
};
