const chai = require('chai');
const expect = chai.expect;
const Pevent = require('../app/models/pevent');

describe("Pevent Validations", function() {
  const pevent = new Pevent({
    venue_id: "2094752934",
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
  });

  it("Must have venue_id", function() {
    t = pevent
    t.venue_id = undefined;
    t.validate(function(err) {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have event_name", () => {
    t = pevent
    t.event_name = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have event_id", () => {
    t = pevent
    t.event_id = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have mon_start", () => {
    t = pevent
    t.mon_start = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have mon_end", () => {
    t = pevent
    t.mon_end = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have tues_start", () => {
    t = pevent
    t.tues_start = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have tues_end", () => {
    t = pevent
    t.tues_end = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have wed_end", () => {
    t = pevent
    t.wed_end = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have wed_end", () => {
    t = pevent
    t.wed_end = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have thurs_end", () => {
    t = pevent
    t.thurs_end = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have thurs_end", () => {
    t = pevent
    t.thurs_end = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have fri_end", () => {
    t = pevent
    t.fri_end = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have fri_end", () => {
    t = pevent
    t.fri_end = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have sat_end", () => {
    t = pevent
    t.sat_end = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have sat_end", () => {
    t = pevent
    t.sat_end = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have sun_end", () => {
    t = pevent
    t.sun_end = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have sun_end", () => {
    t = pevent
    t.sun_end = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have price", () => {
    t = pevent
    t.price = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });
});
