import pandas as pd
import streamlit as st
import json_functions.json_functions_sessions as jf_se

def training_overview():

    # get the training sessions by selected amount
    selected_sessions = jf_se.get_training_sessions(st.session_state.day_interval, st.session_state.session_filter)

    dates = [session["date"] for session in selected_sessions] 
    session_types = [session["type"] for session in selected_sessions] 
    volumes = [jf_se.get_session_volume(session) for session in selected_sessions]

    df = pd.DataFrame({
    "dates": pd.to_datetime(dates),
    "volume": volumes,
    "session_type": session_types,
    })

    spec = {
        "mark": {"type": "circle", "size": 200, "tooltip": True},
        "params": [{"name": "interval_selection", "select": "interval"},
            {
            "name": "point_selection",
            "select": {
                    "type": "point",
                    "fields": ["dates"],
                    "toggle": False,
                    "clear": "dblclick"
                    }
            },
        ],
        "encoding": {
            "x": {"field": "dates", "type": "temporal"},
            "y": {"field": "volume", "type": "quantitative"},
            "color": {"field": "session_type", "type": "nominal", "legend":None}, "fillOpacity": {
                "condition": {"param": "point_selection", "value": 1},
                "value": 1,
            },
        },
    }

    event = st.vega_lite_chart(df, spec, key="vega_chart", on_select="rerun")

    event

    selection = event.selection

    points = selection.get("point_selection", [])

    interval = selection.get("interval_selection", {})

    if points: # when point is selected on graph 
        
        point = points[0]

        if "most_recent_point" not in st.session_state: 
            st.session_state.most_recent_point = point 

            date = point["dates"]
            date_str = pd.to_datetime(date, unit="ms", utc=True).tz_convert("Europe/Stockholm").strftime("%Y-%m-%d")

            st.write(f"initial point pressed with date: {date_str}")
            st.session_state.show_details_of_session = date_str



        if st.session_state.most_recent_point != point:
            
            date = point["dates"]
            date_str = pd.to_datetime(date, unit="ms", utc=True).tz_convert("Europe/Stockholm").strftime("%Y-%m-%d")
            st.session_state.show_details_of_session = date_str

            st.write(f"new point pressed, with date: {date_str}")

            st.session_state.most_recent_point = point
        

    st.write(st.session_state.show_details_of_session)
    st.write(st.session_state.session_filter)

    selected_session = jf_se.get_session_by_date(st.session_state.show_details_of_session, st.session_state.session_filter)

    exercise_names = [exercises["exercise_name"] for exercises in selected_session["exercises"]]

    
    st.write("Last session details")
    df = pd.DataFrame(
            {
                "name": exercise_names,
                
            }
    )
    
    st.dataframe(
            df,
            column_config={
                "name": "Exercise name",
                
            },
            hide_index=True,
    )

    