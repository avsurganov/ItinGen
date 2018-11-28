var mongoose = require('mongoose');
var Schema = mongoose.Schema;


var Activity = new Schema({ event_id: String, venue_id: String, start: Number, end: Number}, { noId: true });
var ItinerarySchema = new Schema({
    activities : [Activity]
});

module.exports = mongoose.model('Itinerary', ItinerarySchema);

