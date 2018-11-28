var User = require("../models/user");
var Itinerary = require("../models/itinerary");
var mongoose = require("mongoose");
var app = require("express");
var router = app.Router();

// Route to register new users  
router.post('/users', function(req, res) {
	var user = new User(); // Create new User object
	user.password = user.generateHash(req.body.password); // Save password from request to User object
	user.email = req.body.email; // Save email from request to User object
	// Check if request is valid and not empty or null
	if (req.body.password === null || req.body.password === '' || req.body.email === null || req.body.email === '') {
		res.json({ success: false, message: 'Ensure email, and password were provided' });
	} else {
		// Save new user to database
		user.save(function(err) {
			if (err) {
				// Check if any validation errors exists (from user model)
				if (err.errors !== null) {
					if (err.errors.email) {
						res.json({ success: false, message: err.errors.email.message }); // Display error in validation (email)
					} else if (err.errors.password) {
						res.json({ success: false, message: err.errors.password.message }); // Display error in validation (password)
					} else {
						res.json({ success: false, message: err }); // Display any other errors with validation
					}
				} else if (err) {
					// Check if duplication error exists
					if (err.code == 11000) {
						if (err.errmsg[61] == "u") {
							res.json({ success: false, message: 'That username is already taken' }); // Display error if username already taken
						} else if (err.errmsg[61] == "e") {
							res.json({ success: false, message: 'That e-mail is already taken' }); // Display error if e-mail already taken
						}
					} else {
						res.json({ success: false, message: err }); // Display any other error
					}
				}
			} else {
				res.json({ success: true, message: 'Account registered!' }); // Send success message back to controller/request
			}
		});
	}
});


// Route for user logins
router.post('/authenticate', function(req, res) {
	var loginUser = req.body.email;
	User.findOne({ email: loginUser }).select('email password').exec(function(err, user) {
		if (err) {
			res.json({ success: false, message: 'Something went wrong. This error has been logged and will be addressed by our staff. We apologize for this inconvenience!' });
		} else {
			// Check if user is found in the database (based on email)           
			if (!user) {
				res.json({ success: false, message: 'Username not found' }); // email not found in database
			} else if (user) {
				if (!req.body.password) {
					res.json({ success: false, message: 'No password provided' }); // Password was not provided
				} else {
					var validPassword = user.comparePassword(req.body.password); // Check if password matches password provided by user 
					if (!validPassword) {
						res.json({ success: false, message: 'Could not authenticate password' }); // Password does not match password in database
					} else {
						var token = jwt.sign({ email: user.email}, secret, { expiresIn: '24h' }); // Logged in: Give user token
						res.json({ success: true, message: 'User authenticated!', token: token }); // Return token in JSON object to controller
					}
				}
			}
		}
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
router.post('/getuser', function(req, res) {
	res.send(req.decoded); // Return the token acquired from middleware
});

// Route to get users liked itineraries
router.get('/liked', function(req, res) {
	User.findOne({ email: req.body.email}).exec(function(err, user) {
		if (err) {
			res.json({ success: false, message: 'Something went wrong. This error has been logged and will be addressed by our staff. We apologize for this inconvenience!' });	
		} else {
			if (!user) {
				res.json({ success: false, message: 'No user was found' }); // Return error
			} else {
				if(users.liked.length > 0){
					let liked = user.liked.map(itinerary_id => new mongoose.Types.ObjectId(itinerary_id));
					Itinerary.find({'_id': {$in: liked}}).exec((err, itins) => {
						if (err) {
							res.json({ success: false, message: 'Something went wrong. This error has been logged and will be addressed by our staff. We apologize for this inconvenience!' });	
						} else {
							if (!itins) {
								res.json({success: false, message: 'No itineraries were found'});
							} else {
								res.json({ success: true, message: 'found itineraries', itineraries: itins});
							}
						}
					});
				} else {
					res.json({success: false, message: 'No itineraries were found'});	
					}
			}	
		}
	});
});
	


// Route to provide the user with a new token to renew session
router.get('/renewToken', function(req, res) {
	User.findOne({ email: req.params.email }).select('email').exec(function(err, user) {
		if (err) {
			res.json({ success: false, message: 'Something went wrong. This error has been logged and will be addressed by our staff. We apologize for this inconvenience!' });
		} else {
			if (!user) {
				res.json({ success: false, message: 'No user was found' }); // Return error
			} else {
				var newToken = jwt.sign({email: user.email }, secret, { expiresIn: '24h' }); // Give user a new token
				res.json({ success: true, token: newToken }); // Return newToken in JSON object to controller
			}
		}
	});
});


module.exports = router;