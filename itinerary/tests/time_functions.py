
# checks that the times given for itin items don't overlap
def validate_nooverlap(itin, user_times=0):
    return False

# checks that itin items are in chronological order
def validate_chrono(itin):
    return False

# checks that times given for itin items are within event's open hours
def validate_isopen(itin, day):
    return False

# checks that itin items fall within specified user times
def validate_within_usertime(itin, user_times=0):
    return False
