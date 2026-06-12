import streamlit as st
import pandas as pd
from db import get_engine
from queries import fetch_all
import datetime

st.title("⏰ Deadline Alerts")
df = fetch_all(get_engine())
df['deadline'] = pd.to_datetime(df['application_deadline']).dt.date

today = datetime.date.today()
soon = df[(df['deadline'] >= today) & (df['deadline'] <= today + datetime.timedelta(days=7))]

st.subheader("Closing in 7 Days")
st.dataframe(soon)