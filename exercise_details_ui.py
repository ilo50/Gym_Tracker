import pandas as pd
import streamlit as st
import json_functions.json_functions_sessions as jf_se
import navigation as nav


def exercise_details():

    '''displays detailed information about a specific exercise'''

    st.subheader(f"Details of {st.session_state.show_details_of_exercise_name} exercise")

    row1_col1, row1_col2, row1_col3 = st.columns(3)

    volumes, reps, weights, dates, type = jf_se.return_details_of_exercise(
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

    with row1_col1:
        st.write("Volumes")
        st.line_chart(df_volume, x="dates", y="volumes", height=200, on_select="ignore")
    
    with row1_col2:
        st.write("Weights")
        st.line_chart(df_weights, x="dates", y="weights", height=200, on_select="ignore")
    
    with row1_col3:
        st.write("Reps")
        st.line_chart(df_reps, x="dates", y="reps", height=200, on_select="ignore")

    df_exercise_details = pd.DataFrame(
                {
                    "Session type": [type],
                    "Amount of times performed":[str(len(dates))],
                    "First performed": [dates[-1]],
                    "Most previously performed": [dates[0]],
                },
                
        )
        
    st.dataframe(df_exercise_details, hide_index=True)

    st.button("Go Back", on_click=nav.go_to_home) 