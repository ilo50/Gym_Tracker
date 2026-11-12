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