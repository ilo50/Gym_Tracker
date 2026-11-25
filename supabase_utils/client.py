from supabase import create_client
import streamlit as st

try:
    supabase_client = create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_PRIVATE_API_KEY"]
    )

except Exception as e:
    st.error(f"Supabase Connection Failed! : {e}")
