var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var TEventSchema = new Schema({
    venue_id: {type: String, required: [true, "can't be blank"]},
    event_name: {type: String, required: [true, "can't be blank"]},
    event_id: {type: String, required: [true, "can't be blank"]},
    start: {type: Number, required: [true, "can't be blank"]},
    end: {type: Number, required: [true, "can't be blank"]},
    date: {type: String, required: [true, "can't be blank"]},
    tags: [{type: String}],
    price: {type: Number, required: [true, "can't be blank"]}
});


module.exports = mongoose.model('TEvent', TEventSchema);
