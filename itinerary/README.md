# What the Files Are

- The Algorithm
  * `pull_events`: logic to create the pool of events from which the itinerary is created
  * `algo_skeleton`: basic logic of the algorithm after the pool of events is created
  * `algo_helpers`: helper functions called by the skeleton to implement itinerary creation logic
  * `validation`: helper functions called by the skeleton to validate various pieces of the itinerary
  * `master_itin_generator`: overall function that combines all other logic and validation to create an itinerary
- Testing
  * `helper_tests`: tests the helper functions. Instructions for use are below
    * `helper_itin_examples`: example events, itins, etc for the helper tests
    * `user_input_examples`: example user inputs for the helper tests
  * `validation_tests`: tests the validation functions. Instructions for use are below
    * `validation_itin_examples`: example events, itins, etc for the validation tests
    * `itin_examples`: same as above
- Server
  * `server`: algorithm API server
    


# Testing
## Updates since 4A
- Added type testing for the elements of an itinerary (```validate_type```)
- Subsumed ```validate_within_username``` function into ```validate_no_overlap```
- Removed ```validate_event_price``` and added ```validate_free``` instead to reflect that the only price-related user input is free/not free rather than specific price
- Incorporated ```validate_free``` and ```validate_type``` testing into validate_itin tests

Run the following commands to run unit tests
```
python validation_tests.py
python helper_tests.py
```
