import streamlit as st
from db import get_engine
from queries import fetch_all, execute_query
from auth import is_admin

st.title("🔄 Update Opportunity")
if is_admin():
    df = fetch_all(get_engine())
    if not df.empty:
        op_id = st.selectbox("Select ID to update", df['opportunity_id'].tolist())
        status = st.selectbox("New Status", ["Open", "Closed", "Expired", "Shortlisted"])
        if st.button("Update"):
            execute_query(get_engine(), "UPDATE opportunities SET status = :s WHERE opportunity_id = :id", {"s": status, "id": op_id})
            st.success("Updated!")
else:
    st.error("Admin access required.")