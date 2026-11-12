import json
from pathlib import Path

def load_exercises():
    default = {"exercises":[{"type": "pull","names": []},
                            {"type": "push","names": []},
                            {"type": "legs","names": []}]}
        
    # if manually emptying the exercises, recreate the root
    if Path("data/exercises.json").stat().st_size == 0:
        return default
        
    with open("data/exercises.json", "r", encoding="utf-8") as file:
        return json.load(file)

def write_exercise(data):
    with open("data/exercises.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

# return all exercises in json file, by specified type of exercise
def get_exercises_by_type(workout_type : str) -> list:
    
    data = load_exercises()

    for exercises in data["exercises"]:

        if exercises["type"] == workout_type:

            return exercises["names"]

def add_exercises(new_exercises, type):

    data = load_exercises()

    for exercises in data["exercises"]:
    
        if exercises["type"] == type:

            exercises["names"].extend(new_exercises)

    write_exercise(data)




