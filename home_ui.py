import streamlit as st
import navigation as nav
import gym_session_overview_ui as gso
import json_functions.json_functions_sessions as jfs

# import css to apply the stylings
import streamlit_css

def home():
    
    # keep track of how many days to show in sessions overview 
    # day_interval used in gym session to filter number of days to display
    if "day_interval" not in st.session_state: 
        st.session_state.day_interval = 7 # default is seven

    if "session_filter" not in st.session_state: 
            st.session_state.session_filter = "all" 

    if "show_details_of_session" not in st.session_state: # default session is most recent
            most_recent_session = jfs.get_training_sessions(1, st.session_state.session_filter)
            if len(most_recent_session)!=0:
                most_recent_session_date = most_recent_session[0]["date"]
                st.session_state.show_details_of_session = most_recent_session_date
            else:
                st.session_state.show_details_of_session = None

    
    st.subheader(f"Past {st.session_state.day_interval} Days Of Training")

    with st.container(horizontal=True, vertical_alignment="center"):
            st.menu_button("Filter", options=["all", "pull", "push", "legs"], on_click=update_session_filter, key="session_filter_input") 
            st.write(f"Filtered by {st.session_state.session_filter}")
            st.space("stretch")
            st.button("Add new session", on_click=nav.go_to_add_new_session) 
        
    # plots the graph of past sessions
    gso.training_overview()

    st.slider("Change interval", min_value=7, max_value=365, value=st.session_state.day_interval, on_change=update_day_interval, key="interval_input")
    
    gso.specific_session_overview()

def update_day_interval():
    st.session_state.day_interval = st.session_state.interval_input

def update_session_filter():
    st.session_state.session_filter = st.session_state.session_filter_input

    # when changing filter, get a new most recent session date for that filter
    most_recent_session = jfs.get_training_sessions(1, st.session_state.session_filter)
    if len(most_recent_session)!=0:
        most_recent_session_date = most_recent_session[0]["date"]
        st.session_state.show_details_of_session = most_recent_session_date
    else:
        st.session_state.show_details_of_session = None