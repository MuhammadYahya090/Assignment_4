import streamlit as st
import pandas as pd
from db import get_engine
from queries import fetch_all
from auth import is_admin

st.title("📂 Upload & Export CSV")
if is_admin():
    file = st.file_uploader("Upload CSV")
    if file:
        df = pd.read_csv(file)
        df.to_sql('opportunities', get_engine(), if_exists='append', index=False)
        st.success("Data Uploaded!")

csv = fetch_all(get_engine()).to_csv(index=False).encode('utf-8')
st.download_button("Export Database as CSV", csv, "export.csv", "text/csv")