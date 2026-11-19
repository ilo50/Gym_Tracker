import pandas as pd
import streamlit as st
import json_functions.json_functions_sessions as jf_se


def exercise_details():

    '''displays detailed information about a specific exercise'''

    st.subheader(f"Showing details of {st.session_state.show_details_of_exercise_name} exercise")

    volumes, reps, weights, dates = jf_se.return_details_of_exercise(
        st.session_state.show_details_of_exercise_name, 
        st.session_state.session_filter)

    
    df_volume = pd.DataFrame({
        "dates": pd.to_datetime(dates),
        "volumes": volumes,
        })

    
    df_weights = pd.DataFrame({
        "dates": pd.to_datetime(dates),
        "weights": weights,
        })

    df_reps = pd.DataFrame({
            "dates": pd.to_datetime(dates),
            "reps": reps,
            })

    st.write("Volumes")
    st.line_chart(df_volume, x="dates", y="volumes", height=150)

    st.write("Weights")
    st.line_chart(df_weights, x="dates", y="weights", height=150)

    st.write("Reps")
    st.line_chart(df_reps, x="dates", y="reps", height=150)

    # todo  add a button to go backwards