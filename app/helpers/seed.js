const mongoose = require('mongoose');
const fs = require('fs');

mongoose.connect('mongodb://localhost:27017/itingen', (err) => {
	if (err){
		console.log("Not connected to database" + err);
	}
	else {
		console.log("Successfully connected to database");
	}
});

const User = require('../models/user');
const Itinerary = require('../models/itinerary');
const Pevent = require('../models/pevent');
const Tevent = require('../models/tevent');
const Venue = require('../models/venue');

Itinerary.collection.drop();
Pevent.collection.drop();
Tevent.collection.drop();
Venue.collection.drop();

const pevents_array = [];
const tevents_array = [];
const venues_array  = [];

const peventsFolder = './app/activities_data/events/';
const teventsFolder = './app/activities_data/tmp_events/';
const venuesFolder = './app/activities_data/venues/';


function seedEvents(data, type, events) {
  if (type == 'pevents') {
    data.map(d => {
      const event = {
        venue_id: d.venue_id,
        event_name: d.event_name,
        event_alias: d.event_alias,
        event_id: d.event_id,
        mon_start: d.mon_start,
        mon_end: d.mon_end,
        tues_start: d.tues_start,
        tues_end: d.tues_end,
        wed_start: d.wed_start,
        wed_end: d.wed_end,
        thurs_start: d.thurs_start,
        thurs_end: d.thurs_end,
        fri_start: d.fri_start,
        fri_end: d.fri_end,
        sat_start: d.sat_start,
        sat_end: d.sat_end,
        sun_start: d.sun_start,
        sun_end: d.sun_end,
        tags: d.tags,
        price: d.price
      };
      events.push(event);
    });
  } else {
    data.map(d => {
      const event = {
        venue_id: d.venue_id,
        event_name: d.event_name,
        event_id: d.event_id,
        start: d.start,
        end: d.end,
        date: d.date,
        tags: d.tags,
        price: d.price
      };
      events.push(event);
    });
  }
}

function seedVenues(data, venues) {
  data.map(d => {
    const venue = {
      venue_id: d.venue_id,
      venue_name: d.venue_name,
      venue_alias: d.venue_alias,
      latitude: d.latitude,
      longitude: d.longitude,
      address1: d.address1,
      address2: d.address2,
      address3: d.address3,
      city: d.city,
      state: d.state,
      zip_code: d.zip_code
    };
    venues.push(venue);
  });
}

fs.readdirSync(peventsFolder).map(file => {
  const pevents = require('../activities_data/events/' + file);
  seedEvents(pevents, 'pevents', pevents_array);
});

fs.readdirSync(teventsFolder).map(file => {
  const tevents = require('../activities_data/tmp_events/' + file);
  seedEvents(tevents, 'tevents', tevents_array);
});

fs.readdirSync(venuesFolder).map(file => {
  const venues = require('../activities_data/venues/' + file);
  seedVenues(venues, venues_array);
});

Pevent.create(pevents_array)
  .then(pevent => {
    console.log(`${pevent.length} pevents created`);
  })
  .catch((err) => {
    console.log(err);
  })

Tevent.create(tevents_array)
  .then(tevent => {
    console.log(`${tevent.length} tevents created`);
  })
  .catch((err) => {
    console.log(err);
  })

venues_array.map(v => {
  Venue.create(v)
    .catch((err) => {
      console.log(err);
    });
});

//Venue.create(venues_array)
  //.then(venue => {
    //console.log(`${venue.length} venues created`);
  //})
  //.catch((err) => {
    //console.log(err);
  //})

User.create(
  [
    {
      email: 'example@example.com',
      password: 'Example@123'
    }, {
      email: 'example2@example.com',
      password: 'Example@321'
    }
  ])

  .then(user => {
    console.log(`${user.length} users created`);
    mongoose.connection.close();
  })

  .catch((err) => {
    console.log(err);
    mongoose.connection.close();

  })


  var itin = new Itinerary();
  itin.activities = [];
  itin.save();

