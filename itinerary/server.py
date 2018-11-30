from flask import Flask
from flask import request
import json
import sys
# sys.path.insert(0, '../itinerary')
from master_itin_generator import *

app = Flask(__name__)

'''
The request to the server is a URL such as this:

http://localhost:5000/?start_time=1430&latitude=44.544&longitude=87.345&free=yes&radius=2.3&transport=walking
'''

@app.route("/")
def run_algorithm():
    start_time = request.args.get("startTime")
    latitude = request.args.get("lat")
    longitude = request.args.get("lon")
    free = request.args.get("free")
    radius = request.args.get("radius")
    transport = request.args.get("transport")
    free = False
    print(start_time, latitude, longitude, free, radius, transport, free)
    itin = generate_itin(start_time, float(latitude), float(longitude), free, float(radius), transport)
    print("OMAR")
    print(itin)
    sys.stdout.flush()
    return json.dumps(itin)

if __name__ == '__main__':
    app.run()

