var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var PEventSchema = new Schema({
    venue_id: {type: String, required: [true, "can't be blank"]},
    event_name: {type: String, required: [true, "can't be blank"]},
    event_alias: String,
    event_id: {type: String, required: [true, "can't be blank"]},
    mon_start: {type: Number, required: [true, "can't be blank"]},
    mon_end: {type: Number, required: [true, "can't be blank"]},
    tues_start: {type: Number, required: [true, "can't be blank"]},
    tues_end: {type: Number, required: [true, "can't be blank"]},
    wed_start: {type: Number, required: [true, "can't be blank"]},
    wed_end: {type: Number, required: [true, "can't be blank"]},
    thurs_start: {type: Number, required: [true, "can't be blank"]},
    thurs_end: {type: Number, required: [true, "can't be blank"]},
    fri_start: {type: Number, required: [true, "can't be blank"]},
    fri_end: {type: Number, required: [true, "can't be blank"]},
    sat_start: {type: Number, required: [true, "can't be blank"]},
    sat_end: {type: Number, required: [true, "can't be blank"]},
    sun_start: {type: Number, required: [true, "can't be blank"]},
    sun_end: {type: Number, required: [true, "can't be blank"]},
    tags: [{type: String}],
    price: {type: Number, required: [true, "can't be blank"]}
});


module.exports = mongoose.model('PEvent', PEventSchema);

