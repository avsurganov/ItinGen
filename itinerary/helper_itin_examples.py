event3 = {
          "event_id": "TMAPIvv1A7ZA8wGkdfoeXP",
          "event_name": "Elton John: Farewell Yellow Brick Road",
          "venue_id": "TMAPIKovZpa2MCe",
          "start": 665,
          "end": 775,
          "date": "02-16-2019",
          "tags": [
            "Music",
            "Rock",
            "Pop",
            "Undefined",
            "Undefined"
          ],
          "price": 59.5
         }

venue3 = {
          "venue_id": "TMAPIKovZpa2MCe",
          "venue_name": "Allstate Arena",
          "latitude": 42.00499247,
          "longitude": -87.88750024,
          "address1": "6920 North Mannheim Road",
          "address2": "",
          "address3": "",
          "city": "Rosemont",
          "state": "IL",
          "zip_code": "60018"
}

event4 = {
          "event_id": "TMAPIvv1A7ZA8wGkdfoeXP",
          "event_name": "Elton John: Farewell Yellow Brick Road",
          "venue_id": "TMAPIKovZpa2MCe",
          "start": 665,
          "end": 790,
          "date": "02-16-2019",
          "tags": [
            "Music",
            "Rock",
            "Pop",
            "Undefined",
            "Undefined"
          ],
          "price": -10
         }

event5 = {
          "event_id": "TMAPIvv1A7ZA8wGkdfoeXP",
          "event_name": "Elton John: Farewell Yellow Brick Road",
          "venue_id": "TMAPIKovZpa2MCe",
          "start": 655,
          "end": 775,
          "date": "02-16-2019",
          "tags": [
            "Music",
            "Rock",
            "Pop",
            "Undefined",
            "Undefined"
          ],
          "price": 59.5
         }

event6 = {
          "event_id": "TMAPIvv1A7ZA8wGkdfoeXP",
          "event_name": "Elton John: Farewell Yellow Brick Road",
          "venue_id": "TMAPIKovZpa2MCe",
          "start": 655,
          "end": 790,
          "date": "02-16-2019",
          "tags": [
            "Music",
            "Rock",
            "Pop",
            "Undefined",
            "Undefined"
          ],
          "price": -3
         }

event7 = {
          "event_id": "TMAPIvv1A7ZA8wGkdfoeXP",
          "event_name": "Elton John: Farewell Yellow Brick Road",
          "venue_id": "TMAPIKovZpa2MCe",
          "start": 790,
          "end": 900,
          "date": "02-16-2019",
          "tags": [
            "Music",
            "Rock",
            "Pop",
            "Undefined",
            "Undefined"
          ],
          "price": 0
         }
# passes meal_overlap check
# free
itina = [(event7,venue3,650,1200)]
# fails meal_overlap check
# free / unspecified price
itinb = [(event4,venue3,650,790)]
# fails meal_overlap check
# not free
itinc = [(event5,venue3,650,790)]
# fails meal_overlap check
# not free
itind = [(event6,venue3,650,790)]
# fails meal_overlap check
# not free
itine = [(event3,venue3,650,790)]
