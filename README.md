ATTENTION ALL TESTERS: USE THESE FACEBOOK CREDENTIALS TO USE OUR APP. YOU HAVE TO LOGIN AS THIS ACCOUNT ON FACEBOOK. THE USERNAME: userplanit@gmail.com. THE PASSWORD: planITtest1. USE THESE FACEBOOK CREDENTIALS TO LOGIN TO OUR APP AND THEN YOU CAN LIKE AND SAVE ITINERARIES.

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
Install node by visiting the website (https://nodejs.org) and installing. Follow the instructions on the website

Node.js and npm are packaged together. So getting Node.js means you will also npm.

Check to see if NPM and Node.js were installed correctly by running:
```bash
node -v
npm -v
```

Install MongoDB by running: 

```
npm i mongodb
mkdir <insert directory name>
mongod --dbpath <path to directory made in previous command>
```
If you have problems with Mongo, do this:

View the mongodb installation documentation (https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)

Install Flask by running: 
```bash
pip3 install Flask
```
### Windows

Unfortunately, the process for getting the appropriate software is extremely involved with windows. If you are using windows and wish to utilize our app, contact the developers using this github repo 


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
## Brief Functionality Description and Brief Tutorial
1) An installation guide
   See Above
2) A brief functionality description
   Plan.it is an itinerary generator that will generate itineraries to help you explore. You can specify parameters for generating itineraries, and like itineraries to save them for future reference.
3) A brief tutorial about how to use your software
   Once you are on the webpace, you can hover over all the buttons and setting options for helpful descriptions. You can click generate, given that it is between 6am and 8pm (as that is the best time for optimal itineraries). You can click on the hamburger menu and click settings to set parameters. The modals will help tell you what each parameter is for. In the hamburger menu, if you are logged in, you can switch between viewing liked itineraries with the liked itineraries button and viewing one itinerary with the home button. The green thumb will add an itinerary to your liked itineraries and generate a new itinerary. The red thumb will just generate a new itinerary and will not add the current one to your liked itineraries. 

## Known Bugs and Other Instructions

### Tips for Using // Known Bugs
- Use the app in Chrome. This is the most reliable browser, and some UI features may not work properly in Safari or Firefox.
- Do not spam the like or dislike buttons. Itinerary generation is not necessarily instantaneous.
- Itineraries will only be generated for start times between 6am and 8pm. This means that if you try to generate an itinerary with the default settings outside that range, you will not see any itinerary generated. 
- User-inputted start locations outside of Chicago are not supported.
- If something loads incorrectly and there is no generate button and no like buttons, you can click home to make the generate button re-appear
- If you generate an itinerary with invalid values, such as the time being between 8pm and 6am, then click home, then generate an itinerary using the dislike or like button, the generate button will appear below the generated itinerary. We are aware of this bug, but decided it did not interfere with the user experience and was not worth fixing.
- A few select custom locations will not generate an intinerary because our algorithim does not recognize them
- The first time you login, facebook will ask you to approve the app. This means you technically have to click the login button twice, once before facebook asks you, once after
- The first time you login with facebook, the liked itineraries may not show up. All you have to do is refresh the page and then click liked itineraries, and they should show up.
- Very rarely, our algorithim will pull an event with a title that contiains a non-ASCII character which causes the itinerary to not generate, making the user have to re-generate an itinerary



## Running Unit Tests

### Back End
- To run database validation tests (back end) for the application, simply run:
  ```bash
  npm test
  ```

### Data & Algorithm
- To run tests for data aggregation, run:
   ```
   npm run data_tests
   ```
- To run test for the algorithm, run:
   ```
   npm run algo_tests
   ```
  


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
   
### Milestone 5 Part 2
2. A final design review document for the TA
1) refer to your first and second milestone document, and discuss:
1.a what proposed functionality is implemented
   User can click generate button to view new itinerary. Itinerary contains information pulled from Yelp, EventBrite, and Ticketmaster. Users can login with a facebook account, once we have added them to the list of test users. Once logged in, users can like itineraries and save them. They can then view liked itineraries and examined the details. Users can click home to return to looking at a single itinerary. Users can click the dislike button to generate a new itinerary, without adding it to their liked itineraries. Users can specify search paramters to search for itineraries including: Start Time (between 6am and 8pm as that is the best window for events), Start Location, Radius they are willing to travel, Method of transportation, and whether they want their itinerary to only include free events.
   
1.b what proposed functionality is not implemented and why
   We didn't implement the ability to dislike or "unlike" itineraries because we didnt think it was important to the user experience. We didnt implement the overlapping view of itineraries because we were unable to. Therefore, Users are also unable to show or hide various itineraries to focus on. Once users like an itinerary and then generate a new one, they can no longer view the liked itinerary on the map as we had originally planned. We did not allow users to specify a type of event or a prearranged event that they would prefer to see in their itinerary because it was too slow to include in our algorithm. We also did not allow users to specify cost because Yelp didn't give us cost specific information other than dollar sign measures. The itinerary generator does not learn from user inputs because it was too expensive to continue making database calls for that implementation. 
1.c what functionality is implemented but not proposed and why
   That ability to use facebook login was not proposed. We added a cute logo and changed the name to plan.it. We added a parameter to chose between driving, public transit, walking, and biking which was not proposed. We added several help modals that appear on hover to help the user that were not proposed.

2) describe what each team member has contributed to the project
   See Above

3. A checkpoint of your source code implementation (Just take a checkpoint, and tell us where it is)
   master branch commit 5329e1de9a96739485d3f8b2f13bd26225d9f178 (does not include final readme edits)

