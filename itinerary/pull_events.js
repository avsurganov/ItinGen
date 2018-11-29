

categories = ["misc","museums","music","nightlife","publicattractions","sports"]
numcat = 6
//user_weight_default = [1 for x in range(numcat)]
numev = 50 // number of events you want to pull from each category
          // maybe make bigger if only free? bc you'll throw out a lot

function day_to_str(dayint){
  switch(dayint) {
    case 1:
      return "mon";
    case 2:
      return "tues";
    case 3:
      return "wed";
    case 4:
      return "thurs";
    case 5:
      return "fri";
    case 6:
      return "sat";
    case 0:
      return "sun" //dates indexed by zero starting sunday
  }
}

function get_date(){
  var today = new Date();
  var dd = today.getDate();
  var mm = today.getMonth()+1; //January is 0!
  var yyyy = today.getFullYear();

  if(dd<10) {
    dd = '0'+dd;
  }

  if(mm<10) {
    mm = '0'+mm;
  }
  today = mm + '-' + dd + '-' + yyyy;
  return today;
}

function time_date_check_perm(event, user_start_time){
  var daynum = Date.getDay();
  var daystr = day_to_str(daynum);
  var startname = daystr + "_start";
  var endname = daystr + "_end";
  var starttime = event[startname];
  var endtime = event[endname];
  if (endtime < user_start_time) {
    return false;
  }
  if (endtime - user_start_time < 15) { //event should be open for more than 15 min after start time
    return false;
  }
  if (starttime == 0 && endtime == 0) {
    return false;
  }
  return true;
}

function time_check_temp(event,user_start_time) {
  var starttime = event[start];
  var endtime = event[end];
  if (endtime < user_start_time) {
    return false;
  }
  if (endtime - user_start_time < 15) {
    return false;

  }
  // do we want to throw out if the event starts before the user start time?
  if (starttime == 0 && entime == 0) {
    return false;
  }
  return true
}

function date_check_temp(event) {
    var today = get_date();
    if (event[date] != today) {
      return false;
    }
    return true;
}

function check_meal_overlap_temp(event) {
    var starttime = event[start];
    var endtime = event[end];
    if (starttime >= 660 && endtime <= 780) {
        return false;     //throws out if entire event is within lunch period 11-1
    }
    if (starttime >= 660 && starttime <= 690 && endtime >= 780) {
        return false; //throws out if event covers all but 1st half hour of lunch
    }
    if (starttime <= 660 && endtime >= 750 && endtime <= 780) {
        return false; //throws out if event covers all but last half hour of lunch
    }
    if (starttime <= 660 && endtime >= 780) {
        return false; //throws out if event covers entire lunch period
    }                    // may want to make this optional depending on how we think
                        // of one time events - do you go to whole thing or no?
}

function check_free(event) {
    if (event[price] != -10) {
        return false;
    }
    return true;
}

function shuffle(array) {
  var currentIndex = array.length, temporaryValue, randomIndex;

  // While there remain elements to shuffle...
  while (0 !== currentIndex) {

    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}

function pick_categories() {
    var ordered_categories = shuffle(categories);
    return ordered_categories;
}

/*
assuming user_inputs = formatted like:

user_inputs = { "user_start_time" : 1200
                "user_start_location" : {"lat" : whatever, "long" = whatever}
                "user_transport" : "car"
                "user_radius" : 10
                "user_cost" : 0         #0 or 1, 0 = free, 1 = not free
}

*/

function get_events(ordered_categories, user_inputs){ //user inputs formatted as a dict?
    var i = 0;
    var evindexes = []  //indexes of events to pull from the database, randomly generated
    var pool = {}  //the entire pool from which events will be pulled to generate itin
    for (i = 0; i < numcat; i++) {
        var category = ordered_categories[i];
        var catname = str(category);
        pool[catname] = [];
        var cattotalevents = 1000   //number of events in the category overall - will need to calculate
        // gotta find way in js to generate a list of length x with random numbers between y and z
        evindexes.push(random.sample(range(ntotalevents),numev)) //generate the random indexes
        for (var j = 0; j < evindexes.length(); j++) {
            //GET the event at that index from the database
            //checks that event makes sense depending on type
            var f = true;
            if (user_inputs[user_cost] == 0) {
                f = check_free(event);
            }
            if (event == temp) {
                var t = time_check_temp(event);
                var d = date_check_temp(event);
                var m = check_meal_overlap_temp(event);
                if (t && d && m && f) {
                    //GET venue, put in tuple
                    pool[catname].push(tuple);
                }
            }
            if (event == perm) {
                var td = time_date_check_perm(event);
                if (td && f) {
                    //get venue, put in tuple
                    pool[catname].push(tuple);
                }
            }
        }
    }
    return pool;
}
