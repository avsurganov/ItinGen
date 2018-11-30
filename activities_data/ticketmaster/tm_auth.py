# file to contain API keys to use for ticketmaster API

# public API rate limit for normal account
# 5000 requests every 1 day

# we can use the public APIs which are:
# Discovery API
# Commerce API

# Partner APIs are:
# Partner API
# Publish API
# International Discovery API

# API keys
# maxliu@uchicago.edu
key1 = "hDzVBIQUgOvWcpgizjEuhvuM5TI0qxG1"
# max_liu@uchicago.edu
key2 = "gUkTRWqOR2vXMqirOvU9pZ1eRVpRJBqA"
# max.liu@uchicago.edu
key3 = "8FYGosHlo8zMPBC5COOdl5IduPs7zazC"
# maxxliu@uchicago.edu
key4 = "5Ac8YTsJHkWwwcctUTqOrm0Dq1Ya59CL"
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
