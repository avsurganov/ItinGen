var User = require("../models/user");

module.exports = (router) => {
	router.post('/users', (req, res) => {
		console.log(req.body.username);
		var user = new User();
		user.username = req.body.username;
		user.email = req.body.email;
		user.tag = req.body.tag;
		user.password = req.body.password;
		user.save();
		res.send("user created");
	}); 
	return router;
}