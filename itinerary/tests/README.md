# Testing

Updates:
	* Added type testing for the elements of an itinerary (validate_type)
	* Subsumed validate_within_username function into validate_no_overlap
	* Removed validate_event_price and added validate_free instead to reflect that the only price-related user input is free/not free rather than specific price
	* Incorporated validate_free and validate_type testing into validate_itin tests

Run the following command to run unit tests
```
python validation_tests.py
```
