import streamlit as st

def setup_auth():
    if "role" not in st.session_state:
        st.session_state.role = "Viewer"

def is_admin():
    return st.session_state.role == "Admin"