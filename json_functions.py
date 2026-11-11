import json

class json_handler:

    '''
    contains handy json functions
    '''

    # return all exercises in json file, by specified type of exercise
    def get_exercises_by_type(workout_type : str) -> list:
        result = ""
        with open("data/exercises.json", "r", encoding="utf-8") as file:
            data = json.load(file)

            for exercises in data["exercises"]:

                if exercises["type"] == workout_type:

                    return exercises["names"]

        

    get_exercises_by_type("push")