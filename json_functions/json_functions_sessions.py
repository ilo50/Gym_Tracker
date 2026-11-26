import supabase_utils.file_handling as sb_fh

PATH = "data/training_sessions_live_data.json"
NAME = "workout-data"

def load_training_session():
    '''wrapper for the file download in supabase utils'''
    return sb_fh.download_data_from_supabase_bucket(PATH, NAME)

def write_training_session(data):
    '''wrapper for the file upload in supabase utils'''
    sb_fh.upload_data_to_supabase_bucket(data, PATH, NAME)
    

def add_training_session(sets_data, type, dateinput):

    data = load_training_session()

    sessions = data["training_sessions"]

    new_session = {
            "session_nr" : len(sessions)+1,
            "type" : type,
            "date" : str(dateinput),
            "exercises" : sets_data
    }

    sessions.append(new_session)

    write_training_session(data)


def get_training_sessions(amount, filter): 

    data = load_training_session()
    all_sessions = data["training_sessions"]

    if filter == "all":
        
        return all_sessions[-amount:] if amount > 0 else []

    else:
        
        filtered_sessions = [s for s in all_sessions if s["type"] == filter] 
        
        return filtered_sessions[-amount:] if amount > 0 else []

def get_all_training_sessions(filter="all"): 

    '''return all sessions, with possibility of filtering by type'''

    data = load_training_session()
    all_sessions = data["training_sessions"]

    if filter == "all":
        
        return all_sessions

    else:
        
        filtered_sessions = [s for s in all_sessions if s["type"] == filter] 
        
        return filtered_sessions

def get_session_volume(session):
    # return weight * reps for all exercises in 
    return sum(
        s["weight"] * s["reps"]
        for ex in session["exercises"]
        for s in ex["sets"]
    )

def get_session_by_date(adate : str, filter): 

    data = load_training_session()
    all_sessions = data["training_sessions"]
    
    if filter == "all":
            
        for session in all_sessions:

            if session["date"] == adate:

                return session
    else:
            
        filtered_sessions = [s for s in all_sessions if s["type"] == filter] 
            
        for session in filtered_sessions: 

            if session["date"] == adate:

                return session

def last_performed(name, date, filter): # returns most recent date that {name} exercise occurs prior to {date}

    filtered_sessions_type = get_all_training_sessions(filter)

    # only get the sessions that are before current date
    filtered_sessions_date = [s for s in filtered_sessions_type if s["date"] < date] 

    # reverse to get newest first
    for session in reversed(filtered_sessions_date): 

        for ex in session["exercises"]:

            if ex["exercise_name"] == name:

                return session["date"]

def return_history(session_type, exercise_name):
    '''Takes a name of an exercise and returns a list of the volume of past it in past sessions'''

    sessions = get_all_training_sessions(session_type)

    past_volumes = []

    # reverse to get newest first
    for session in sessions: 

        for ex in session["exercises"]:

            if ex["exercise_name"] == exercise_name:

                volume = sum(s["weight"] * s["reps"] for s in ex["sets"]) 
                past_volumes.append(volume)

    return past_volumes

def return_details_of_exercise(exercise_name, session_type):
    '''Takes a name of an exercise and returns 4 lists: past weights, past reps, past volumes and past dates'''

    sessions = get_all_training_sessions(session_type)
    
    past_volumes = []
    past_reps = []
    past_weights = []
    past_dates = []

    type = ""

    # reverse to get newest first
    for session in sessions: 

        date = session["date"]
        type = session["type"]
    
        for ex in session["exercises"]:
    
            if ex["exercise_name"] == exercise_name:

                reps = sum(s["reps"] for s in ex["sets"])
                weights = sum(s["weight"] for s in ex["sets"])
                volume = sum(s["weight"] * s["reps"] for s in ex["sets"]) 

                past_volumes.append(volume)
                past_reps.append(reps)
                past_weights.append(weights)
                past_dates.append(date)
    
    return past_volumes, past_reps, past_weights, past_dates, type