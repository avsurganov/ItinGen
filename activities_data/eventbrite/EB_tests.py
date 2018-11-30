#Class for testing eventbrite API calls
#tests are run both during data collection process and before passing data to next step
class Tests:

	def __init__(self):
		self.num_tests = 0
		self.success_tests = 0

	#check venue for valid field types
	def venue_valid(self, venue):
		is_valid = True
		if not isinstance(venue.get('venue_id'), str):
			print('\tTYPE ERROR: venue_id should be string')
			is_valid = False
		if not isinstance(venue.get('venue_name'), str):
			print('\tTYPE ERROR: venue_name should be string')
			is_valid = False
		if not isinstance(venue.get('latitude'), float):
			print('\tTYPE ERROR: latitude should be float')
			is_valid = False
		if not isinstance(venue.get('longitude'), float):
			print('\tTYPE ERROR: longitude should be float')
			is_valid = False
		if not isinstance(venue.get('address1'), str):
			print('\tTYPE ERROR: address1 should be string')
			is_valid = False
		if not isinstance(venue.get('address2'), str):
			print('\tTYPE ERROR: address2 should be string')
			is_valid = False
		if not isinstance(venue.get('address3'), str):
			print('\tTYPE ERROR: address3 should be string')
			is_valid = False
		if not isinstance(venue.get('city'), str):
			print('\tTYPE ERROR: city should be string')
			is_valid = False
		if not isinstance(venue.get('state'), str):
			print('\tTYPE ERROR: state should be string')
			is_valid = False
		if not isinstance(venue.get('zip_code'), str):
			print('\tTYPE ERROR: zip_code should be string')
			is_valid = False
		if (is_valid):
			self.success_tests += 1
		self.num_tests+=1
		assert is_valid, 'Invalid venue ' + venue.get('venue_id')

	#check event for valid field types
	def event_valid(self, event):
		is_valid = True
		if not isinstance(event.get('event_id'), str):
			print('\tTYPE ERROR: event_id should be string')
			is_valid = False
		if not isinstance(event.get('event_name'), str):
			print('\tTYPE ERROR: event_name should be string')
			is_valid = False
		if not isinstance(event.get('venue_id'), str):
			print('\tTYPE ERROR: venue_id should be string')
			is_valid = False
		if not isinstance(event.get('start'), int):
			print('\tTYPE ERROR: start should be int')
			is_valid = False
		if not isinstance(event.get('end'), int):
			print('\tTYPE ERROR: end should be int')
			is_valid = False
		if not isinstance(event.get('date'), str):
			print('\tTYPE ERROR: event_date should be string')
			is_valid = False
		if not isinstance(event.get('price'), float):
			print('\tTYPE ERROR: price should be float')
			is_valid = False
		if (is_valid):
			self.success_tests += 1
		self.num_tests+=1
		assert is_valid, 'Invalid event ' + event.get('event_id')

	#check that end times are after start times
	def time_valid(self, events):
		for event in events:
			self.num_tests+=1
			start = event.get('start')
			end = event.get('end')
			if (end <= start):
				print('\tEVENT ERROR: event %s has end time before start time' % event.get('event_id'))
				assert False, 'Invalid time from event ' + event.get('event_id')
			else:
				self.success_tests += 1
	#check that all latitude and longitude values are in the acceptable range
	def lat_long_valid(self, venues):
		for venue in venues:
			lat = venue.get('latitude')
			long = venue.get('longitude')
			id = venue.get('venue_id')
			self.num_tests+=1
			if (lat > 90.0 or lat < -90.0):
				print('\tVENUE ERROR: venue %s has invalid latitude' % id)
				assert False, 'Invalid latitude from venue ' + id
			else:
				self.success_tests += 1
			self.num_tests+=1
			if (long > 180.0 or long < -180.0):
				print('\tVENUE ERROR: venue %s has invalid longitude' % id)
				assert False, 'Invalid longitude from venue ' + id
			else:
				self.success_tests+=1



	# check that all events have a valid venue id
	def venue_id_valid(self, events, venues):
		venue_ids = []
		for venue in venues:
			venue_ids.append(venue.get('venue_id'))
		for event in events:
			venue_id = event.get('venue_id')
			if not venue_id in venue_ids:
				print('\tEVENT ERROR: event %s has invalid venue_id' % event.get('event_id'))
				assert False, 'Invalid venue_id ' + venue_id + ' from event_id ' + event.get('event_id')
			else:
				self.success_tests += 1
			self.num_tests+=1

	#print number of tests and successes
	def display_test_results(self):
		print('\tTESTS: %d tests run, %d tests passed' % (self.num_tests, self.success_tests))

EB_tests = Tests()
