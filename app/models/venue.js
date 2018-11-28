var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var VenueSchema = new Schema({
    venue_id: String,
    venue_name: String,
    venue_alias: String,
    latitude: Number,
    longitude: Number,
    address1: String,
    address2: String,
    address3: String,
    city: String,
    state: String,
    zip_code: String
});


module.exports = mongoose.model('Venue', VenueSchema);
