import streamlit as st
from auth import setup_auth

st.set_page_config(page_title="Dashboard Home", layout="wide")
setup_auth()

st.title("💼 Internship & Job Tracking Dashboard")
st.markdown("Welcome to the University Opportunities Hub. Use the sidebar to navigate.")

st.markdown("---")
st.subheader("Access Control")

# Display the current active role
st.info(f"Current Session Role: **{st.session_state.role}**")

# Simple toggle to switch roles
role = st.radio("Select Session Role:", ["Viewer", "Admin"], index=0 if st.session_state.role == "Viewer" else 1)

if st.button("Apply Role"):
    st.session_state.role = role
    st.success(f"Access granted as: {role}")
    st.rerun()