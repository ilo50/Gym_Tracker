import pandas as pd
import streamlit as st
import numpy as np
from numpy.random import default_rng as rng


def training_overview():

    df = pd.DataFrame({
    "date": pd.date_range("2026-10-19", periods=7),  # 4 weeks
    "value": np.random.randint(3, 10, size=7),
    })

    st.scatter_chart(df, x="date", y="value")