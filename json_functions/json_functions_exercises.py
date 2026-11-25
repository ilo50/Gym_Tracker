import json
from pathlib import Path
import supabase_utils.file_handling as sb_fh

PATH = "data/exercises.json"
NAME = "exercise_data"

def load_exercises():
    '''wrapper for the file download in supabase utils'''
    return sb_fh.download_data_from_supabase_bucket(PATH, NAME)

def write_exercise(data):
    '''wrapper for the file upload in supabase utils'''
    sb_fh.upload_data_to_supabase_bucket(data, PATH, NAME)

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




