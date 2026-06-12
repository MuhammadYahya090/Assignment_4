import streamlit as st
from db import get_engine
from queries import fetch_all, execute_query
from auth import is_admin

st.title("🗑️ Delete Opportunity")
if is_admin():
    df = fetch_all(get_engine())
    if not df.empty:
        op_id = st.selectbox("Select ID to delete", df['opportunity_id'].tolist())
        if st.button("Delete"):
            execute_query(get_engine(), "DELETE FROM opportunities WHERE opportunity_id = :id", {"id": op_id})
            st.success("Deleted!")
else:
    st.error("Admin access required.")