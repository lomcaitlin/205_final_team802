# 205 Final Project Team 802
This project allows users to view and "like" different breweries from the Open Brewery DB.
#### [Bawar Hotak](https://github.com/HotakBawar), [Chris Webb](https://github.com/WebbontheWeb), [Hunter Smith](https://github.com/Hunterls914), [Keiti Lo](https://github.com/lomcaitlin)
##### CST 205 || December 16, 2021
---
## Table of Contents
- [How to Run](#how-to-run)
- [Future Work](#future-work)
- [Github](https://github.com/lomcaitlin/205_final_team802)
- [Trello](https://trello.com/b/42e385Dy/finalprojteam802)

---
## How to Run
Download required packages from home directory:
```bash
$ pip install -r requirements.txt
```
In home directory, run the following in command line:
```bash
$ export FLASK_APP=app
$ flask run
```
---
## Future Work

It is currently set up to be hosted on [Heroku](https://cst205-final-team802.herokuapp.com/), but because we are keeping track of rankings using a global variable, there are issues with persistence.

One way to make sure the Heroku hosted app works properly would be to store the rankings in a database instead of a global variable. It would also be better/more proper to do it this way.

Also realized after the presentation on Wednesday that we are actually *not* using the full API database. The route which we thought returned a full list of all breweries in the database is actually paginated with a default max rows at 20. Because of this, displaying the rankings and also displaying all the breweries is more difficult. Future work would include updating the routes and templates to allow for paginated data.

The current search route also does not utilize the search endpoint that the API provides, so future work would be to update the search route to use the API's search.

Another aspect of the project that we can expand is having some kind of safety net for users when they give +1 or -1. For example, only allowing a certain number of upvotes or downvotes from a certain IP address or something, in case one user has a grudge against a certain brewery and writes a bot to keep downvoting it.