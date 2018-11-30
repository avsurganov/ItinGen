const chai = require('chai');
const expect = chai.expect;
const Venue = require('../app/models/venue');

describe("Pevent Validations", function() {
  const venue = new Venue({
    venue_id: "2094752934",
    venue_name: "Best Event Ever",
    latitude: 34.30,
    longitude: 56.22
  });

  it("Must have venue_id", function() {
    t = venue
    t.venue_id = undefined;
    t.validate(function(err) {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have venue_name", () => {
    t = venue
    t.venue_name = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have latitude", () => {
    t = venue
    t.latitude = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });

  it("Must have longitude", () => {
    t = venue
    t.longitude = undefined;
    t.validate((err) => {
      expect(err.errors.name).to.be.undefined;
    });
  });
});
