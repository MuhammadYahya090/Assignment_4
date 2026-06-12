import streamlit as st
from db import get_engine
from queries import fetch_all
from utils import find_dupes

st.title("🛡️ Duplicate Detection")
df = fetch_all(get_engine())
dupes = find_dupes(df)

if dupes.empty:
    st.success("No duplicates found.")
else:
    st.warning("Potential duplicates detected:")
    st.dataframe(dupes)