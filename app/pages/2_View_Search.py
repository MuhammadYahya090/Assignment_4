import streamlit as st
from db import get_engine
from queries import fetch_all

st.title("🔍 View & Search")
df = fetch_all(get_engine())

search = st.text_input("Search by company or title")
if search:
    df = df[df['company_name'].str.contains(search, case=False) | df['job_title'].str.contains(search, case=False)]

st.dataframe(df, use_container_width=True)