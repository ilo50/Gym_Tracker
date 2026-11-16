import json
from datetime import date
from pathlib import Path

def write_training_session(data):
    with open("data/training_sessions.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def add_training_session(sets_data, type):

    data = load_training_session()

    sessions = data["training_sessions"]

    new_session = {
            "session_nr" : len(sessions)+1,
            "type" : type,
            "date" : date.today().isoformat(),
            "exercises" : sets_data
    }

    sessions.append(new_session)

    write_training_session(data)

def load_training_session():

    default = {"training_sessions": []}

    # if manually emptying the training sessions, recreate the root
    if Path("data/training_sessions.json").stat().st_size == 0:
        return default

    with open("data/training_sessions.json", "r", encoding="utf-8") as file:
        return json.load(file)

def get_training_sessions(amount, filter):

    data = load_training_session()
    all_sessions = data["training_sessions"]

    if filter == "all":
        
        return all_sessions[-amount:] if amount > 0 else []

    else:
        
        filtered_sessions = [s for s in all_sessions if s["type"] == filter] 
        
        return filtered_sessions[-amount:] if amount > 0 else []

def get_session_volume(session):
    # return weight * reps for all exercises in 
    return sum(
        s["weight"] * s["reps"]
        for ex in session["exercises"]
        for s in ex["sets"]
    )

def get_session_by_date(date : str, filter): 

    data = load_training_session()
    all_sessions = data["training_sessions"]
    
    if filter == "all":
            
        for session in all_sessions:

            if session["date"] == date:

                return session
    else:
            
        filtered_sessions = [s for s in all_sessions if s["type"] == filter] 
            
        for session in filtered_sessions: 

            if session["date"] == date:

                return session


