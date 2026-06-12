import streamlit as st
from db import get_engine
from sqlalchemy import text

st.title("🩺 Database Health")
try:
    with get_engine().connect() as conn:
        version = conn.execute(text("SELECT version();")).scalar()
        count = conn.execute(text("SELECT COUNT(*) FROM opportunities;")).scalar()
    st.success("PostgreSQL is connected and healthy.")
    st.write(f"**Version:** {version}")
    st.write(f"**Total Records:** {count}")
except Exception as e:
    st.error(f"Connection Failed: {e}")