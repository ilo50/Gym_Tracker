import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng



def exercise_overview():

    '''displays detailed information about a specific exercise'''

    

    df = pd.DataFrame({
        "dates": pd.to_datetime(dates),
        "volume": volumes,
        "session_type": session_types,
        })

    st.line_chart(df)