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
### Install Prerequisites (NPM/Node.js/MongoDB)
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

## Suggested acceptance tests

Opening and closing the hamburger menu, clicking the register link so that a modal window appears with a form for user information, and closing this window.

For acceptance tests of the map, feel free to manipulate the map as you see fit (zoom in and out, travel to other parts of the world, etc.).

User disliking an itinerary triggers the generation of a new itinerary. The TA can test this functionality by clicking the dislike button (red thumb down).


## Who Did What:
### Back-end
Omar and Anthony wrote the back-end together. They implemented a seeds
file to make sure that the JSON data that the Data Aggregation Team
extracted was populating the database. They also redeveloped the
application to utilize PosgreSQL instead of MongoDB. Additionally,
established the route and testing suite, wrote DB migrations, model
validations, and implemented controller logic. Lastly, they tracked down
bugs in the app and data aggregation scripts.

### Front-end
Leslie and Tyler constructed the sidebar with information related to events/activities in a given itinerary and buttons allowing one to access more information about the event when fully implemented. Additionally, they implemented a menu with links to home, liked itineraries, log in window, and register window. Register link triggers a modal view of a the sign on form. Finally, they built and positioned like and dislike buttons on top of the map.

Anthony implemented the Google map with drawn itineraries and paths and
injected Ruby code into the front-end to display itineraries in the
sidebar.

### Data Aggregation
Max wrote the Ticketmaster API data collection, Clare and Masha wrote the Yelp API data collection and Eli wrote the Eventbrite API data collection. Each team member wrote validation tests for their API. The main database pipeline was written primarily by Max with assistance from the other members of the Data Aggregation Team. The collected data was all stored as JSON files for use by the Back-end team.

## Changes:
We decided to switch the application from using MongoDB to Postgresql.
We were having issues with MongoDB working properly with the Rails
application and so we switched it out for Postgres.

No longer using Vue.js frontend framework. Instead only working with pure javascript, html, and CSS. This decision allowed for quicker development time as the Vue.js presented a learning curve for all members of our team

We switched from collecting data by type of event to collecting data by API to reduce data overlap and the number of API calls needed. This also allowed each member of the data aggregation team to focus on a single API.

## Addressing Specific Questions for Milestone 4A:

1. A brief description about what you plan to implement in the 2nd iteration.

For our iteration two, we plan to boost our application to production level by implementing user accounts, automatic itinerary generation, user defined settings, and a liked itineraries page. These features build upon the first in that they add to the core functionality of the application, or, the true value add to users of ItinGen. As before, we leave the development of the user interface to the frontend team, the development of the data model to the backend team, and the implementation of the itinerary generation algorithm to the algorithm and data team. We elaborate on what each subteam will do specifically below.

Due to time constraints and unforseen complications, we are decreasing the amount of inputs we will accept from the user. We will no longer allow users to specify their budget, but we will allow them to specify whether they only want to attend free or not free events. We will no longer allow them to specify an ending location as we will assume the ending location is the same as the starting location. We will allow them to specify a maximum radius for the itinerary instead of a distance they are willing to travel. We will also not allow them to specify types of activities they are interested in. Therefore, our settings window will only accept start location, time frame, amd travel radius as possible inputs from a user.

2. A brief description about how the work will be divided among all pairs of people in your team.

  Front End [Leslie, Tyler]
  Integrate Angular.js frontend framework (previously decided against) to handle increase frontend complexity
  Build setting window where user can define parameters that affect the result itineraries
  Build liked itineraries page where users can view all of their previously liked itineraries at once with the ability to focus on a particular itinerary
  Insert login button and functionality

  Back End [Anthony, Omar]
  Populate Database with models
  Create associations between models
  Integrate OAuth and User Accounts
  Integrate itinerary generation algorithm
  Convert Rails MVC to Rails API and add Angular.js integration

  Algorithms [Clare, Eli, Masha, Max]
  a) We will implement an algorithm to randomly generate an itinerary, which will contain events from our database and will be constrained by (optional) parameters set by the user. Prior to itinerary generation, the user will be able to:
  specify starting and ending time
  specify starting location
  specify the distance radius they are willing to travel
  Specify if itinerary should only be free events
  Additionally, users will be able to like or dislike each itinerary and future itineraries will be optimized to take into account the user’s history of likes and dislikes. The user inputs have changed from the design document in order to simplify the itinerary generation algorithm.

  b) The algorithm and data team will work together to implement an itinerary generation algorithm based on user inputs. The team will work with the backend and frontend teams to ensure smooth transition from user input, database querying, generation, to displaying.



