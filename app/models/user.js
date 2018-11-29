var mongoose = require('mongoose');
var Schema = mongoose.Schema;
// var bcrypt = require('bcrypt-nodejs');

var Activity = new Schema({ event_id: String, venue_id: String, start: Number, end: Number}, { noId: true });
var ItinerarySchema = new Schema({
    activities : [Activity]
});

var UserSchema = new Schema({
	email: {type: String, required: true, unique: true},
	liked: [ItinerarySchema]
});

// UserSchema.methods.generateHash = function(password) {
//     return bcrypt.hashSync(password, bcrypt.genSaltSync(8), null);
// };

// UserSchema.methods.comparePassword = function(password) {
//     return bcrypt.compareSync(password, this.password); // Returns true if password matches, false if doesn't
// };

module.exports = mongoose.model('User', UserSchema);