var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var VenueSchema = new Schema({
  venue_id: {type: String, required: [true, "can't be blank"]},
  venue_name: {type: String, required: [true, "can't be blank"]},
  venue_alias: String,
  latitude: {type: Number, required: [true, "can't be blank"]},
  longitude: {type: Number, required: [true, "can't be blank"]},
  address1: String,
  address2: String,
  address3: String,
  city: String,
  state: String,
  zip_code: String
});


module.exports = mongoose.model('Venue', VenueSchema);
