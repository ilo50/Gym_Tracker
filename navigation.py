import streamlit as st
import json_functions.json_functions_exercises as jf_exercises

def go_to_select_weight_and_reps(exercises, new_exercises):
    st.session_state.exercises = exercises
    st.session_state.exercise_index = 0
    st.session_state.page = "select_weight_and_reps"

    if len(new_exercises) != 0:
         
        jf_exercises.add_exercises(new_exercises, st.session_state.workout_type)

def go_to_add_new_session():
    st.session_state.page = "add_new_session_form"

def go_to_select_exercises(workout_type):
    st.session_state.workout_type = workout_type
    st.session_state.page = "select_exercise_type"

def go_to_home():
    st.session_state.page = "home"