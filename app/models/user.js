var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var bcrypt = require('bcrypt-nodejs');

var UserSchema = new Schema({
	password: {type: String, required: true},
	email: {type: String, required: true, unique: true},
	liked: [{type: String}]
});

UserSchema.methods.generateHash = function(password) {
    return bcrypt.hashSync(password, bcrypt.genSaltSync(8), null);
};

UserSchema.methods.comparePassword = function(password) {
    return bcrypt.compareSync(password, this.password); // Returns true if password matches, false if doesn't
};

module.exports = mongoose.model('User', UserSchema);