from math import sin, cos, sqrt, atan2, radians, acos, fabs, pi

def venue_to_lat_long(venue):
	lat = venue.get('latitude')
	long = venue.get('longitude')
	return [lat, long]

def find_distance(coords1, coords2):
	earth_radius = 3957.25
	lat1 = radians(coords1[0])
	lat2 = radians(coords2[0])
	long1 = radians(coords1[1])
	long2 = radians(coords2[1])
	a = sin((lat2-lat1)/2)**2 + cos(lat1)*cos(lat2)*sin((long2-long1)/2)**2
	return fabs(earth_radius*2*atan2(sqrt(a), sqrt(1-a)))

def find_angle(coords1, center, coords2):
	earth_radius = 3957.25
	a = find_distance(coords1, center)/(2*pi*earth_radius)
	b = find_distance(center, coords2)/(2*pi*earth_radius)
	c = find_distance(coords1, coords2)/(2*pi*earth_radius)
	num = cos(c)-cos(a)*cos(b)
	den = sin(a)*sin(b)
	print(num)
	print(den)
	if (den == 0):
		return 0
	return acos(num/den)

def validate_angle(coords1, center, coords2, limit):
	angle = find_angle(coords1, center, coords2)
	rad_lim = limit*pi
	if (angle <= rad_lim):
		return True
	else:
		return False

def decrement_radius(prev_rad, dA):
	new_rad = sqrt((pi*prev_rad**2-dA)/pi)
	if new_rad < 0:
		return prev_rad
	else:
		return new_rad

def increment_radius(prev_rad, dA):
	new_rad = sqrt((dA/5+pi*prev_rad**2)/pi)
	return new_rad

print(find_angle([0,1], [0,0], [0, -1]))
