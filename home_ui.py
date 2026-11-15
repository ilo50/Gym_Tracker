import streamlit as st
import navigation as nav
import gym_session_overview_ui as gso

def home():

    st.button("Add session", on_click=nav.go_to_add_new_session)

    gso.training_overview()