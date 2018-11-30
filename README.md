# ItinGen

ItinGen is a web based application that allows users to randomly
generate optimized itineraries for their schedules to explore a new city
or rediscover a city they have been living in for years

# Table of Contents

- [Setup](#setup)
    * [Install Prerequisites](#install-prerequisites)
    * [Initializing the App](#initializing-the-app)
- [Running Unit Tests](#running-unit-tests)
- [Suggested Acceptance Tests](#suggested-acceptance-tests)
- [Who Did What](#who-did-what)
    * [Back End](#back-end)
    * [Front End](#front-end)
    * [Data Aggregation](#data-aggregation)
- [Changes](#changes)
- [Specific Information for 4B](#specific-information-for-4b)

## Setup
### Install Prerequisites 
(NPM/Node.js/MongoDB)
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
```
sudo apt-get install -y mongodb
```


### Initializing the App
```bash
npm install
npm run seed
npm start
```

## Running Unit Tests
Unit Tests for the Data Aggregation scripts and instructions on how to use them will be found in the `app/activities_data` directory.

To run tests for the application, simply run:
```bash
npm test
```
These tests will test to make sure that all of the front-end objects are
displaying on the home page properly and as are intended.:w

## Suggested Acceptance Tests

Opening and closing the hamburger menu, clicking the register link so that a modal window appears with a form for user information, and closing this window.

For acceptance tests of the map, feel free to manipulate the map as you see fit (zoom in and out, travel to other parts of the world, etc.).

User disliking an itinerary triggers the generation of a new itinerary. The TA can test this functionality by clicking the dislike button (red thumb down).


## Who Did What

The entire team collaborated to integrate and test each piece of the system. 

### Back End
Omar and Anthony wrote the back-end together. They redeveloped the application to utilize MongoDB. They registered our app on Facebook and connected our database to Facebook so that the user could sign up for our app strictly through Facebook. 

### Front End
Leslie and Tyler make tweaks to the sidebar. They implemented the feature that allows users to save itineraries and view their saved itineraries. They added various "help" modals to give more information to the user about the functionality of various buttons. 

### Data Aggregation
Clare wrote the logic to create a pool of viable itinerary events. Masha wrote the logic to check that the times and distances between itineraries were logical. Eli wrote the logic to choose events within a certain distance and angle of the previous event. Max wrote the logic to slot events into a final itinerary and account for meal times in the itinerary. Each team member wrote validation functions for their generation logic and tested their validation functions. 

## Changes
- Back End:
   * We rewrote the app with a node.js back end. We decided to switch to an node.js because it's easier to integrate with an Angular.js front end. 
   * We switched back to an MongoDB to better support our unstructured data.
- Front End:
   * We rewrote the app with an Angular.js front end.
   * We decided to change the format of the "Liked Itineraries" visual so that the user doesn't see overlapping itineraries.
   * We did not implement the ability to select an itinerary to follow. We decided that this feature didn't add anything to the app experience and wasn't important to the main functionality.
   * We implemented a Facebook login functionality. 
   * We updated the color scheme. 
- Data Team:
   * We made a number of small changes to various user preference features:
      * The user can specify start time, but not end time. We removed end time because it resulted in too many evening events being rejected.
      * The user can specify which method of transportation they want to use to get between events.
      * The user can specify that they want an itinerary with only free events. 

## Specific Information for 4B

Question answers go here


