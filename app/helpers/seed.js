const mongoose = require('mongoose');
const { port, db, secret }    = require('../config/env');
//mongoose.Promise = require('bluebird');
mongoose.connect(db);

const User = require('../models/user');
const Pevent = require('../models/pevent');
const Tevent = require('../models/tevent');
const Venue = require('../models/venue');

User.collection.drop();
Pevent.collection.drop();
Tevent.collection.drop();
Venue.collection.drop();

const pevents_array = [];
const tevents_array = [];
const venues_array  = [];

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
      longitutde: d.longitude,
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

// PEVENTS JSON
fetch('JSON PATH')
  .then(response => response.json)
  .then(data => seedEvents(data, 'pevents', pevents_array));

// TEVENTS JSON
fetch('JSON PATH')
  .then(response => response.json)
  .then(data => seedEvents(data, 'tevents', tevents_array));

// VENUES JSON
fetch('JSON PATH')
  .then(response => response.json)
  .then(data => seedVenues(data, venues_array));

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

Venue.create(venuess_array)
  .then(venue => {
    console.log(`${venue.length} venues created`);
  })
  .catch((err) => {
    console.log(err);
  })

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
  })

  .catch((err) => {
    console.log(err);
  })

  .finally(() => {
    mongoose.connection.close();
  });

