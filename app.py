import streamlit as st
import page_ui as ui

# init
if "page" not in st.session_state:
    st.session_state.page = "home"

# dictionary that maps a page name to a function
PAGES = {
    "home": ui.home,
    "add_new_session_form": ui.add_new_session_form,
    "select_exercise_type": ui.select_exercise_type,
    "select_weight_and_reps": ui.select_weight_and_reps,
}

PAGES[st.session_state.page]()

    
