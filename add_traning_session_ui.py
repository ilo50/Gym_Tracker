import streamlit as st

import json_functions.json_functions_exercises as jf_exercises
import json_functions.json_functions_sessions as jf_session

import navigation as nav

from datetime import date

def select_exercise_type():
    
    result = jf_exercises.get_exercises_by_type(st.session_state.workout_type)
    exercises = st.multiselect(
    "Select exercises",
    [*result], 
    accept_new_options=True
    )
    new_exercises = [name for name in exercises if name not in result] # if new exercise is added, put in exercises.json

    with st.container(horizontal=True):
            st.button("Done", on_click=nav.go_to_select_weight_and_reps, args=(exercises,new_exercises), disabled=not exercises)
            st.button("Cancel", on_click=nav.go_to_home)

def add_new_session_form():

    st.session_state.results = []
    workout_type = st.selectbox(
    "Select workout type",
    ("push", "pull", "legs"), 
    )

    selected_date = st.date_input("Select date", date.today().isoformat())
    
    with st.container(horizontal=True):
        st.button(key="session_form_button", label="Done", on_click=nav.go_to_select_exercises, args=(workout_type,selected_date))
        st.button("Cancel", on_click=nav.go_to_home)

def next_exercise(exercise, sets_data):

    st.session_state.results.append(
        {
            "exercise_name" : exercise,
            "sets" : sets_data
        }
    )
    st.session_state.exercise_index += 1

    if len(st.session_state.exercises) == st.session_state.exercise_index:
        jf_session.add_training_session(st.session_state.results, st.session_state.workout_type, st.session_state.selected_date)

        # after session is added update which session to show details of
        # since it will most likely be this new one
        most_recent_session = jf_session.get_training_sessions(1, st.session_state.session_filter)
        if len(most_recent_session)!=0:
            most_recent_session_date = most_recent_session[0]["date"]
            st.session_state.show_details_of_session = most_recent_session_date
        else:
            st.session_state.show_details_of_session = None

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
    
    set_data = [] #store weight and reps across iterations

    for n in range(nr_of_sets):

        st.write(f"Set {n+1}")
        col1, col2 = st.columns(2, gap="small")

        with col1:
            st.markdown("**Weight**")
            weight = st.number_input(
                "Weight",
                min_value=1.0,
                max_value=200.0,
                value=20.0,
                step=0.5,
                format="%.1f",
                key=f"weight_{exercise}_{n}",
                label_visibility="collapsed",
            )

        with col2:
            st.markdown("**Repetitions**")
            reps = st.number_input(
                "Reps",
                min_value=1,
                max_value=30,
                value=10,
                key=f"reps_{exercise}_{n}",
                label_visibility="collapsed",
            )

        set_data.append({"weight": weight, "reps": reps})

    with st.container(horizontal=True):
        st.button(key="session_form_button", label="Done", on_click=next_exercise, args=(exercise, set_data))
        st.button("Cancel", on_click=nav.go_to_home)