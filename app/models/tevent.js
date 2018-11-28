var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var TEventSchema = new Schema({
    venue_id: String,
    event_name: String,
    event_id: String,
    start: Number,
    end: Number,
    date: String,
    tags: [{type: String}],
    price: Number
});


module.exports = mongoose.model('TEvent', TEventSchema);
