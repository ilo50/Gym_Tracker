import streamlit as st

import add_traning_session_ui as add_session
import home_ui as home
import exercise_details_ui as ex_det

# init
if "page" not in st.session_state:
    st.session_state.page = "home"

# dictionary that maps a page name to a function
PAGES = {
    "home": home.home,
    "add_new_session_form": add_session.add_new_session_form,
    "select_exercise_type": add_session.select_exercise_type,
    "select_weight_and_reps": add_session.select_weight_and_reps,
    "exercise_details": ex_det.exercise_details,
}

PAGES[st.session_state.page]()

    
