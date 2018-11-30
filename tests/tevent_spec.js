const chai = require('chai');
const expect = chai.expect;
const Tevent = require('../app/models/tevent');

describe("Pevent Validations", function() {
  const tevent = new Tevent({
    venue_id: "2094752934",
    event_name: "Best Event Ever",
    event_id: "1823421",
    start: 23847,
    end: 4592345,
    date: 2893476,
    tags: ['nightlife'],
    price: 4000
  });

  it("Must have venue_id", function() {
    t = tevent
    t.venue_id = undefined;
    t.validate(function(err) {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have event_name", function() {
    t = tevent
    t.event_name = undefined;
    t.validate(function(err) {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have event_id", function() {
    t = tevent
    t.event_id = undefined;
    t.validate(function(err) {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have start", function() {
    t = tevent
    t.start = undefined;
    t.validate(function(err) {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have end", function() {
    t = tevent
    t.end = undefined;
    t.validate(function(err) {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have price", function() {
    t = tevent
    t.price = undefined;
    t.validate(function(err) {
      expect(err.errors.name).to.be.undefined;
    });
  });

});

