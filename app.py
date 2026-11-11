import streamlit as st
from json_functions import json_handler

def go_to_select_weight_and_reps(exercises):
    st.session_state.exercises = exercises
    st.session_state.page = "select_weight_and_reps"

def go_to_add_new_session():
    st.session_state.page = "add_new_session_form"

def go_to_select_exercises(workout_type):
    st.session_state.workout_type = workout_type
    st.session_state.page = "select_exercise_type"

def go_to_home():
    st.session_state.page = "home"

def home():

    st.button("Add session", on_click=go_to_add_new_session)

def select_exercise_type():
    
    result = json_handler.get_exercises_by_type(st.session_state.workout_type)
    
    exercises = st.multiselect(
    "Select exercises",
    [*result], 
    )

    st.button("Done", on_click=go_to_select_weight_and_reps, args=(exercises,))

def add_new_session_form():

    workout_type = st.selectbox(
    "Select workout type",
    ("push", "pull", "legs"), 
    )
    st.button(key="session_form_button", label="Done", on_click=go_to_select_exercises, args=(workout_type,))

def select_weight_and_reps():



    for exercise in st.session_state.exercises:
        st.subheader(exercise)

        nr_of_sets = st.number_input(
            "", 
            value=3, 
            placeholder="Select number of sets", 
            key=f"sets_{exercise}"
        )

        for n in range(nr_of_sets):

            weight = st.slider(
                label="",
                min_value=0,
                max_value=200,
                value=20,
                key=f"weight_{exercise}_{n}"
            )

        
    
# init
if "page" not in st.session_state:
    st.session_state.page = "home"

# flow
if st.session_state.page == "home":
    home()

elif st.session_state.page == "add_new_session_form":
    add_new_session_form()

elif st.session_state.page == "select_exercise_type":
    select_exercise_type()

elif st.session_state.page == "select_weight_and_reps":
    select_weight_and_reps()




    
