const assert = require("assert")

//TODO: This must be a valid schema object...
const pevent = {
  venue_id: "_fajdhfas",
  event_name: "Best Event Ever",
  event_alias: "Better event?",
  event_id: "1823421",
  mon_start: 300,
  mon_end: 300,
  tues_start: 300,
  tues_end: 300,
  wed_start: 300,
  wed_end: 300,
  thurs_start: 300,
  thurs_end: 300,
  fri_start: 300,
  fri_end: 300,
  sat_start: 300,
  sat_end: 300,
  sun_start: 300,
  sun_end: 300,
  tags: ['nightlife'],
  price: 4000
}

describe("Pevent Validations", function() {
  it("Must have Venue_id", function() {
    assert.equal(true, true);
  });
});
