import streamlit as st
import plotly.express as px
from db import get_engine
from queries import fetch_all

st.title("📊 Analytics")
df = fetch_all(get_engine())

if not df.empty:
    st.metric("Total Opportunities", len(df))
    st.plotly_chart(px.pie(df, names='category', title="Category Breakdown"), use_container_width=True)
    st.plotly_chart(px.bar(df['status'].value_counts().reset_index(), x='status', y='count', title="Status Analysis"), use_container_width=True)