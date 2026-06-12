import os
from sqlalchemy import create_engine
import streamlit as st

@st.cache_resource
def get_engine():
    db_host = os.getenv("DB_HOST", "localhost")
    db_password = os.getenv("DB_PASSWORD", "app_password")
    return create_engine(f"postgresql://app_user:{db_password}@{db_host}:5432/student_opportunities_db")