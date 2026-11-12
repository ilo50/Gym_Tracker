import streamlit as st

import json_functions.json_functions_exercises as jf_exercises
import json_functions.json_functions_sessions as jf_session

import navigation as nav

def home():

    st.button("Add session", on_click=nav.go_to_add_new_session)

def select_exercise_type():
    
    result = jf_exercises.get_exercises_by_type(st.session_state.workout_type)
    exercises = st.multiselect(
    "Select exercises",
    [*result], 
    accept_new_options=True
    )
    new_exercises = [name for name in exercises if name not in result] # if new exercise is added, put in exercises.json
    st.button("Done", on_click=nav.go_to_select_weight_and_reps, args=(exercises,new_exercises), disabled=not exercises)

def add_new_session_form():

    st.session_state.results = []
    workout_type = st.selectbox(
    "Select workout type",
    ("push", "pull", "legs"), 
    )
    st.button(key="session_form_button", label="Done", on_click=nav.go_to_select_exercises, args=(workout_type,))

def next_exercise(exercise, sets_data):

    st.session_state.results.append(
        {
            "exercise_name" : exercise,
            "sets" : sets_data
        }
    )
    st.session_state.exercise_index += 1

    if len(st.session_state.exercises) == st.session_state.exercise_index:
        jf_session.add_training_session(st.session_state.results, st.session_state.workout_type)
        nav.go_to_home()
        
def select_weight_and_reps():

    exercises = st.session_state.exercises
    index = st.session_state.exercise_index 
    exercise = exercises[index]
    st.subheader(exercise)

    nr_of_sets = st.number_input(
                "Select the amount of sets for the exercise", 
                value=3, 
                min_value=1,
                max_value=5,
                placeholder="amount of sets", 
                key=f"sets_{exercise}"
                )

    st.caption("Select the weight and reps for each set, top to bottom")
    col1, col2 = st.columns(2)

    with col1:
        st.write("Weight")
    with col2:
        st.write("Repetitions")

    set_data = [] #store weight and reps across iterations

    for n in range(nr_of_sets):

        col1, col2 = st.columns(2)

        with col1:
            weight = st.slider(
                        label="",
                        min_value=0,
                        max_value=300,
                        value=20,
                        key=f"weight_{exercise}_{n}"
                        )

        with col2:
            reps = st.slider(
                        label="",
                        min_value=0,
                        max_value=30,
                        value=10,
                        key=f"reps_{exercise}_{n}"
                        )

        set_data.append({"weight": weight, "reps": reps})

    st.button(key="session_form_button", label="Done", on_click=next_exercise, args=(exercise, set_data))
