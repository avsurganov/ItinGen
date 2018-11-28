# Ticketmaster API

This directory contains files that utilize the Ticketmaster API to find events
in Chicago for sports and music

## File Information

**tm_api.py** contains functions to execute full Ticketmaster data pipeline and
output to json files so that they can be read into the database

**tm_auth.py** contains API keys that are used to make API requests. This file
should not be in the repository. Instead a fake authentication file is used
and stores invalid keys so that the scripts can still run

**tm_fauth.py** contains invalid API keys

**tm_tests.py** contains testing functions that run both during execution and
after execution of the Ticketmaster data pipeline to ensure that data is valid
