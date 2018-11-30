# NOTE: fake credentials file so that code does not give errors if the true
#       credentials file is not present
# NOTE: none of these api keys will return proper results

# API keys
# maxliu@uchicago.edu
key1 = "invalid1"
# max_liu@uchicago.edu
key2 = "invalid2"
# max.liu@uchicago.edu
key3 = "invalid3"
# maxxliu@uchicago.edu
key4 = "invalid4"
# maxx_liu@uchicago.edu
# maxx.liu@uchicago.edu

# all keys
API_KEYS = [key1, key2, key3, key4]

# keep track of what key im using and how to move to next key
CUR_KEY = [-1] # key we are currently using
NO_KEYS = len(API_KEYS) # total number of keys
def switch_key():
    '''
    switches the key that the API is using, will switch if current key reaches
    limit or if rate limiting due to too many calls too quickly

    outputs:
        key (str) - will return the new key to use, if the keys have been
                    rotated through too many times then something is wrong and
                    error value of -1 will be returned
    '''
    CUR_KEY[0] += 1
    switch_to = CUR_KEY[0] % NO_KEYS
    # too many rotations means they are probably all exhausted
    if CUR_KEY[0] > (10 * NO_KEYS):
        print("WARNING: keys have been rotated through too many times")
        return -1

    return API_KEYS[switch_to]
