# Activities Data

## Structure

Activities data is divided by API. Each of the API's will gather data for a
group of activities. Activity groups include:
- City events
- Food
- Museums
- Nightlife
- Public attractions
- Sports
- Music

**Ticketmaster API:** Sports, Music

**Yelp API:** Food, Museums, Nightlife

**Eventbrite API:** City events

*requirements.txt contains packages necessary for running the scripts*
*requirements.txt may not have every single package at the moment*

## Tests

Tests are no longer contained in a separate testing file. Each API will have
its own individual tests located in their respective api directory. This makes
the most sense as each API will have its own nuances and placing tests in an
outside directory is both difficult to import and vague as to which test
corresponds to which API.

Please look into each API directory to see how their respective tests run. Most
of these tests are not run as separate scripts but are rather run both during
execution and after execution to make sure that data is valid and requests
are returning correctly

*structure subject to change*

## Main Database Pipeline
Run master_data_pipeline.py to generate json files for all APIs to their respective folders.
This should also be run for all validation tests. 
