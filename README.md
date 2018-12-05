# plan.it

plan.it is a web based application that allows users to randomly generate optimized itineraries for their schedules to explore a new city or rediscover a city they have been living in for years.

# Table of Contents

- [Setup](#setup)
    * [Install Prerequisites](#install-prerequisites)
    * [Initializing the App](#initializing-the-app)
- [Known Bugs and Other Instructions](#known-bugs-and-other-instructions)    
- [Running Unit Tests](#running-unit-tests)
- [Suggested Acceptance Tests](#suggested-acceptance-tests)
- [Who Did What](#who-did-what)
    * [Back End](#back-end)
    * [Front End](#front-end)
    * [Data Aggregation](#data-aggregation)
- [Changes](#changes)

## Setup
### Install Prerequisites 
(NPM/Node.js/MongoDB/Flask)
#### Ubuntu
You will need to add the Node.js PPA by running this command:
```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -
```
Finally, install Node.js:
```bash
sudo apt-get install -y nodejs
```

Check to see if NPM and Node.js were install correctly by running:
```bash
node -v
npm -v
```

Now you will need to install MongoDB:
```bash
sudo apt-get install -y mongodb
```

You will also need to install Flask
```bash
pip3 install Flask
```

#### macOS
Install node by visiting the website (https://nodejs.org) and installing.

Install npm ...

Check to see if NPM and Node.js were installed correctly by running:
```bash
node -v
npm -v
```

Install MongoDB by running: 

If you have problems with Mongo, do this:

Install Flask by running: 
```bash
pip3 install Flask
```



### Initializing the App
#### Ubuntu

```bash
git clone -b master https://github.com/maxxliu/ItinGen.git
cd ItinGen
```
For all terminals and for all commands, you should be in the ItinGen directory of the master branch of our repository.

In one terminal window, run this command:
```bash
npm run flask
```
If npm run flask doesn't work due to missing pymongo module then type the following
```bash
pip3 install pymongo --user
```

If pip3 is a command thats not found, then you don't have python, so run the following:
```bash
sudo apt update
sudo apt install python3-pip
pip3 --version
```

Then in another terminal window, run these commands:
```bash
npm install
npm run seed
npm start
```

If you don't get a message saying successfully connected to the database, you will need a third window. 
In the second window, in ItinGen, run the following:
```bash
sudo mkdir -p /data/db/
sudo chown id /data/db
mongod
```
where id is your user id

Then in the third window, run npm install then npm start.

So im summary, one window should be continuously running after typing "npm run flask", one window should be continuously running after typing "mongod", and a third window should be continuously running after typing "npm start". Then, in the Chrome browser, go to localhost:3000 and click refresh.

#### macOS
In one terminal window in ItinGen/itinerary run this command:
```bash
python server.py
```

In another terminal window, run these commands:
```bash
npm install
npm run seed
npm start
```

Then, in Chrome, go to localhost:3000.


## Known Bugs and Other Instructions

### Tips for Using
- Use the app in Chrome. This is the most reliable browser, and some UI features may not work properly in Safari or Firefox.
- Do not spam the like or dislike buttons. Itinerary generation is not instantaneous. If you don't have an itinerary after 10-20 seconds, then try again.
- Itineraries will only be generated for start times between 6am and 8pm. This means that if you try to generate an itinerary with the default settings outside that range, you will not see any itinerary generated. 
- User-inputted start locations outside of Chicago are not supported.
- If something loads incorrectly and there is no generate button and no like buttons, you can click home to make the generate button re-appear
- If you generate an itinerary with invavlid values, such as the time being between 8pm and 6am, then click home, then generate an itinerary using the dislike or like button, the generate button will appear below the generated itinerary. We are aware of this bug, but decided it did not interfere with the user experience and was not worth fixing.



## Running Unit Tests
### Front End
- Front end tests are in `public/core/itinerary/factory`. To run front end tests, do:
  ```
  npm run e2e
  ```
### Back End
- To run database validation tests (back end) for the application, simply run:
  ```bash
  npm test
  ```

### Data & Algorithm
- Unit Tests for the data aggregation scripts and the generation algorithm and the respective instructions on how to use them will be found in the `itinerary` directory.  
  


## Suggested Acceptance Tests
- Opening and closing the hamburger menu. 
- Opening the menu and selecting different settings and generating different itinereraries. 
- Logging in and out.
- For acceptance tests of the map, feel free to manipulate the map as you see fit (zoom in and out, travel to other parts of the world, etc.).

## Who Did What

The entire team collaborated to integrate and test each piece of the system. 

### Back End
Omar and Anthony wrote the back-end together. They redeveloped the application to utilize MongoDB. They registered our app on Facebook and connected our database to Facebook so that the user could sign up for our app strictly through Facebook. 

### Front End
Leslie and Tyler make tweaks to the sidebar. They implemented the feature that allows users to save itineraries and view their saved itineraries. They added various "help" modals to give more information to the user about the functionality of various buttons. 

### Data Aggregation
Clare wrote the logic to create a pool of viable itinerary events. Eli wrote the logic to choose events within a certain distance and angle of the previous event. Masha wrote the logic to check that the times and distances between events were logical. Max wrote the logic to slot events into a final itinerary and account for meal times in the itinerary. Each team member wrote validation functions for their generation logic and tested their validation functions. 

## Changes
- Back End:
   * We rewrote the app with a node.js back end. We decided to switch to an node.js because it's easier to integrate with an Angular.js front end. 
   * We switched back to an MongoDB to better support our unstructured data.
- Front End:
   * We rewrote the app with an Angular.js front end.
   * We made a number of small changes to various user preference features:
      * The user can specify start time, but not end time. We removed end time because it resulted in too many evening events being rejected.
      * The user can specify which method of transportation they want to use to get between events.
      * The user can specify that they want an itinerary with only free events. 
      * We did not implement the ability to select an itinerary to follow. We decided that this feature didn't add anything to the app experience and wasn't important to the main functionality.
      * We decided not to implement the ability for a user to un-like an itinerary.
   * We decided to change the format of the "Liked Itineraries" visual so that the user doesn't see overlapping itineraries.
   * We implemented a Facebook login functionality. 
   * We updated the color scheme. 
   * We added a fire logo.
- Data Team:
   * Our final version of the algorithm does not include generating itineraries based on the other itineraries that a user has saved. This is because accounting for liked itineraries required a large volume of database queries for information about their liked itineraries each time a new itinerary was generated. This proved costly and we decided that it wasn't important enough to the core features of the software to be worth the computational and performance cost.      
