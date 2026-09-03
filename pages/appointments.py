import streamlit as st
import datetime
import re
from database.db import get_departments, get_doctors, insert_appointment

st.title("📅 Book an Appointment")

dept_records = get_departments()
dept_names = [d["name"] for d in dept_records] if dept_records else ["General Medicine"]

# 🛠️ Main Column Splits for basic patient demographics
c1, c2 = st.columns(2)
with c1:
    name = st.text_input("Patient Full Name *")
    age = st.number_input("Patient Age *", min_value=1, max_value=120, value=30)
    phone = st.text_input("Phone Number *")
with c2:
    # 🛠️ Moving interactive dropdown dependencies outside st.form for reactive filtering
    dept = st.selectbox("Department *", dept_names)
    docs = get_doctors(dept_filter=dept)
    doc_names = [d["name"] for d in docs] if docs else ["Any Available Doctor"]
    doctor = st.selectbox("Doctor *", doc_names)
    min_date = datetime.date.today() + datetime.timedelta(days=1)
    pref_date = st.date_input("Date *", min_value=min_date, value=min_date)

c3, c4 = st.columns(2)
with c3:
    slot = st.selectbox("Time Slot *", [
        "09:00 AM - 10:00 AM", "10:00 AM - 11:00 AM",
        "11:00 AM - 12:00 PM", "02:00 PM - 03:00 PM",
        "03:00 PM - 04:00 PM", "04:00 PM - 05:00 PM"
    ])
with c4:
    reason = st.text_area("Reason for Consultation *")

# Form submission event layer
if st.button("Confirm Booking", type="primary", use_container_width=True):
    if not name.strip() or not reason.strip():
        st.error("Name and reason are required.")
    elif not re.match(r"^[0-9+\-\s()]{7,18}$", phone.strip()):
        st.error("Please enter a valid phone number.")
    else:
        try:
            ref_id = insert_appointment(
                name.strip(), 
                int(age), 
                phone.strip(), 
                dept, 
                doctor, 
                str(pref_date), 
                slot, 
                reason.strip()
            )
            st.success(f"🎉 Booking registered successfully! Reference ID: **{ref_id}**")
            st.balloons()
        except Exception as e:
            st.error(f"Error saving appointment: {e}")
