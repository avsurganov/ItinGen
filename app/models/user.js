var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var bcrypt = require('bcrypt-nodejs');

var UserSchema = new Schema({
	username: {type: String, required: true, unique: true},
	password: {type: String, required: true},
	email: {type: String, required: true, lowercase: true, unique: true},
	tag: String
});

UserSchema.pre('save', (next) => {
	var user = this;
	bcrypt.hash(user.password, null, null, (err, hash) => {
		if (err) return next(err);
		user.password = hash;
		next();
	});
});

module.exports = mongoose.model('User', UserSchema);