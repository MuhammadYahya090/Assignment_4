import streamlit as st
from db import get_engine
from queries import execute_query
from auth import is_admin
import datetime

st.title("➕ Add Opportunity")
if is_admin():
    with st.form("add_form"):
        company = st.text_input("Company Name")
        title = st.text_input("Job Title")
        category = st.selectbox("Category", ["Data Science", "Web Development", "Cyber Security", "AI", "Software Engineering"])
        skills = st.text_area("Required Skills")
        deadline = st.date_input("Deadline")
        
        if st.form_submit_button("Add Record"):
            sql = """INSERT INTO opportunities (company_name, job_title, category, required_skills, application_deadline) 
                     VALUES (:c, :t, :cat, :s, :d)"""
            execute_query(get_engine(), sql, {"c": company, "t": title, "cat": category, "s": skills, "d": deadline})
            st.success("Successfully added!")
else:
    st.error("Admin access required.")