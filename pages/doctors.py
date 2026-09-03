import streamlit as st
from database.db import get_doctors, get_departments

st.title("👨‍⚕️ Medical Specialists Directory")
dept_names = [d["name"] for d in get_departments()]

col1, col2 = st.columns([1, 2])
with col1:
    dept_choice = st.selectbox("Department Filter:", ["All Departments"] + dept_names)
with col2:
    doc_search = st.text_input("Search Doctor by Name:")

doctors = get_doctors(dept_choice, doc_search)

if not doctors:
    st.info("No specialists matched your filter.")
    st.stop()  # 🛠️ Replaced function 'return' with native Streamlit execution stop

# 🛠️ Robust grid implementation to prevent flex alignment layout bugs
for i in range(0, len(doctors), 2):
    grid_batch = doctors[i:i+2]
    cols = st.columns(2)
    for idx, doc in enumerate(grid_batch):
        with cols[idx]:
            with st.container(border=True):
                st.subheader(doc["name"])
                st.markdown(f"**Specialization:** {doc['specialization']}")
                st.markdown(f"**Department:** {doc['department']}")
                st.markdown(f"**Experience:** {doc['experience']}")
                st.markdown(f"🗓️ **Days:** {doc['available_days']} | ⏰ **Timing:** {doc['timing']}")
