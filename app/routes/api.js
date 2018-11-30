var User = require("../models/user");
var Itinerary = require("../models/itinerary");
var mongoose = require("mongoose");
var spawn = require("child_process").spawn;
var app = require("express");
var jwt = require('jsonwebtoken'); // Import JWT Package
var router = app.Router();
var secret = 'itingen'; // Create custom secret to use with JWT

router.post('/getitinerary', function(req, res) {
	var userSettings = req.body.userSettings;
	var startTime = userSettings.startTime;
	var startLocation = userSettings.startLocation;
	var lat = startLocation.lat;
	var lon = startLocation.lon;
	var free = userSettings.free;
	var radius = userSettings.radius;
	var transport = userSettings.transport;
	console.log(userSettings);
	var pythonProcess = spawn('py',["algorithm.py", "startTime", startTime, 
										"lat", lat, "lon", lon, "free", 
										free, "radius", radius, "transport", transport]);
	pythonProcess.stdout.on('data', (data) => {
		// Do something with the data returned from python script
		console.log("GOT DATA");
	});
});


// Middleware for Routes that checks for token - Place all routes after this route that require the user to already be logged in
router.use(function(req, res, next) {
	var token = req.body.token || req.body.query || req.headers['x-access-token']; // Check for token in body, URL, or headers

	// Check if token is valid and not expired  
	if (token) {
		// Function to verify token
		jwt.verify(token, secret, function(err, decoded) {
			if (err) {
				res.json({ success: false, message: 'Token invalid' }); // Token has expired or is invalid
			} else {
				req.decoded = decoded; 
				next(); // Required to leave middleware
			}
		});
	} else {
		res.json({ success: false, message: 'No token provided' }); // Return error if no token was provided in the request
	}
});

// Route to get the currently logged in user    
router.post('/me', function(req, res) {
	console.log("in /me");
	console.log(req.decoded);
	res.send(req.decoded); // Return the token acquired from middleware
});

// Route to get users liked itineraries
router.get('/getliked', function(req, res) {
	console.log("GOT HERE");
	User.findOne({ email: req.decoded.email}).exec(function(err, user) {
		if (err) {
			res.json({ success: false, message: 'Something went wrong. This error has been logged and will be addressed by our staff. We apologize for this inconvenience!' });	
		} else {
			if (!user) {
				console.log("IN HEREz");
				res.json({ success: false, message: 'No user was found' }); // Return error
			} else {
				if(user.liked.length > 0){
					res.json({ success: true, message: 'found itineraries', itineraries: user.liked});
				} else {
					console.log("IN HEREz");
					res.json({success: false, message: 'No itineraries were found'});	
				}
			}	
		}
	});
});

// Route to append to a users like itineraries
router.post('/putliked', (req, res) => {
	var itins = req.body.itineraries;
	var userEmail = req.decoded.email;
	let user = new User();
	user.liked = itins;
	user.userEmail = userEmail;
	User.findOneAndUpdate({email : userEmail}, user, function(err) {
		if (err) { 
			res.json({success : false});
			return; 
		}
		res.json({success : true});
	});
});

module.exports = router;