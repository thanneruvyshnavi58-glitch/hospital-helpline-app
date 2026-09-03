import streamlit as st
from database.db import get_hospital_info

st.title("📞 Contact & Directory")
h = get_hospital_info()

c1, c2 = st.columns(2)
with c1:
    st.subheader("Main Hospital Campus")
    st.write(h["address"])
    st.write(f"Central Phone: **{h['phone']}**")
    st.write(f"Emergency: **{h['emergency_phone']}**")
with c2:
    st.subheader("Timings")
    st.write(f"OPD Hours: {h['working_hours']}")
    st.write(f"Visiting: {h['visiting_hours']}")

st.markdown("---")
st.subheader("Administrative Feedback")
with st.form("contact_form", clear_on_submit=True):
    st.text_input("Name")
    st.text_input("Email")
    st.text_area("Message")
    if st.form_submit_button("Submit"):
        st.success("Message submitted to the administration desk.")
