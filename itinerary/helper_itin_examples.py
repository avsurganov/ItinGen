eventa = {
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

venuea = {
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

eventb = {
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

eventc = {
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

eventd = {
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

evente = {
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
itina = [(evente,venuea,650,1200)]
# fails meal_overlap check
# free / unspecified price
itinb = [(eventb,venuea,650,790)]
# fails meal_overlap check
# not free
itinc = [(eventc,venuea,650,790)]
# fails meal_overlap check
# not free
itind = [(eventd,venuea,650,790)]
# fails meal_overlap check
# not free
itine = [(eventa,venuea,650,790)]
