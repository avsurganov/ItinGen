var User = require("../models/user");
var app = require("express");
var router = app.Router();

router.post('/users', (req, res) => {
	console.log(req.query);
	var user = new User();
	user.username = req.query.username;
	user.email = req.query.email;
	user.tag = req.query.tag;
	user.password = user.generateHash(req.query.password);
	user.save();
	res.send("user created");
}); 

module.exports = router;