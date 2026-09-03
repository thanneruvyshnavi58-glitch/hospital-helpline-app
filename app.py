import streamlit as st
from database.db import init_db

# Configure the browser tab titles and dimensions
st.set_page_config(
    page_title="MetroHealth Central Hospital Helpline",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Run database setup and collection seeding on startup
init_db()

# Main landing routing logic 
st.title("Hospital Helpline Management System")
st.markdown("---")

# Navigation Setup
pages = {
    "Hospital Overview": [
        st.Page("pages/home.py", title="Home Dashboard", icon="🏥"),
        st.Page("pages/departments.py", title="Medical Departments", icon="🏢"),
        st.Page("pages/doctors.py", title="Find Our Doctors", icon="👨‍⚕️"),
    ],
    "Patient Services": [
        st.Page("pages/appointments.py", title="Book an Appointment", icon="📅"),
        st.Page("pages/chatbot.py", title="AI Medical Assistant", icon="💬"),
    ],
    "Support & Contact": [
        st.Page("pages/emergency.py", title="Emergency Contacts", icon="🚨"),
        st.Page("pages/faq.py", title="Help & FAQs", icon="🙋"),
        st.Page("pages/contact.py", title="Reach Us", icon="📍"),
    ]
}

pg = st.navigation(pages)
pg.run()
