var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var PEventSchema = new Schema({
    venue_id: String,
    event_name: String,
    event_alias: String,
    event_id: String,
    mon_start: Number,
    mon_end: Number,
    tues_start: Number,
    tues_end: Number,
    wed_start: Number,
    wed_end: Number,
    thurs_start: Number,
    thurs_end: Number,
    fri_start: Number,
    fri_end: Number,
    sat_start: Number,
    sat_end: Number,
    sun_start: Number,
    sun_end: Number,
    tags: [{type: String}],
    price: Number
});


module.exports = mongoose.model('PEvent', PEventSchema);

