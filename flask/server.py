from flask import Flask
from flask import request
import json

app = Flask(__name__)

'''
The request to the server is a URL such as this:

http://localhost:5000/?start_time=1430&latitude=44.544&longitude=87.345&free=yes&radius=2.3&transport=walking
'''

@app.route("/")
def run_algorithm():
    start_time = request.args.get("start_time")
    latitude = request.args.get("latitude")
    longitude = request.args.get("longitude")
    free = request.args.get("free")
    radius = request.args.get("radius")
    transport = request.args.get("transport")
    return algorithm(start_time, latitude, longitude, free, radius, transport)

def algorithm(start_time, latitude, longitude, free, radius, transport):
    ret = {
        'start_time': start_time,
        'latitude': latitude,
        'longitude': longitude,
        'free': free,
        'radius': radius,
        'transport': transport
    }
    return json.dumps(ret)

if __name__ == '__main__':
    app.run()

