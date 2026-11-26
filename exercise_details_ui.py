import pandas as pd
import streamlit as st
import json_functions.json_functions_sessions as jf_se
import navigation as nav
import matplotlib.pyplot as plt


def exercise_details():

    '''displays detailed information about a specific exercise'''

    st.subheader(f"Details of {st.session_state.show_details_of_exercise_name} exercise")

    row1_col1, row1_col2, row1_col3 = st.columns(3)

    volumes, reps, weights, dates, type = jf_se.return_details_of_exercise(
        st.session_state.show_details_of_exercise_name, 
        st.session_state.session_filter)
    
    df = pd.DataFrame({
        "dates": pd.to_datetime(dates),
        "Volumes": volumes,
        "Weights": weights,
        "Reps": reps
    }).sort_values("dates")

    # Create compact static charts
    fig, axes = plt.subplots(3, 1, figsize=(7, 5), sharex=True)

    chart_data = [
        ("Volumes", "#3498db"),
        ("Weights", "#2ecc71"),
        ("Reps", "#e67e22")
    ]

    for ax, (column, color) in zip(axes, chart_data):

        ax.plot(
            df["dates"],
            df[column],
            color=color,
            linewidth=1.8,
            marker="o",
            markersize=3
        )

        ax.set_title(column, fontsize=10, loc="left", pad=5)
        ax.grid(axis="y", alpha=0.2)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_alpha(0.2)
        ax.tick_params(axis="both", labelsize=8, length=0)

    fig.autofmt_xdate(rotation=30)
    fig.tight_layout(pad=1.5)

    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    # Exercise information
    df_exercise_details = pd.DataFrame({
        "Session type": [type],
        "Amount of times performed": [str(len(dates))],
        "First performed": [dates[-1]],
        "Most previously performed": [dates[0]],
    })

    st.dataframe(df_exercise_details, hide_index=True)

    st.button("Go Back", on_click=nav.go_to_home)