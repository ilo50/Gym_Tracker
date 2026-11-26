import streamlit as st
# Hide the toolbar on all streamlit plots

st.markdown("""
    <style>
        [data-testid="stElementToolbar"] {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)