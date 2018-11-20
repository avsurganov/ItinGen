# ItinGen

ItinGen is a web based application that allows users to randomly
generate optimized itineraries for their schedules to explore a new city
or rediscover a city they have been living in for years

Table of Contents

[TOC]

## Setup

https://gorails.com/setup/osx/10.14-mojave
Currently setup with Postgres as the DataBase.

### Initializing the app
```bash
bundle install
rake db:setup
rails s
```

## Running Unit Tests
Unit Tests for the Data Aggregation scripts and instructions on how to use them will be found in the `activities_data` directory.

To run tests for the application, simply run:
```bash
rspec
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
