import streamlit as st
from database.db import get_departments

st.title("🏥 Clinical Departments")
search = st.text_input("Search departments by name or symptoms (e.g., 'skin', 'chest', 'bone'):")
depts = get_departments(search)

if not depts:
    st.info("No departments matched your search.")
    st.stop()  # 🛠️ Replaced legacy function 'return' with structural Streamlit stop

for d in depts:
    with st.container(border=True):
        st.subheader(d["name"])
        st.write(d["description"])
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"📍 **Location:** {d['location']}")
        with c2:
            st.markdown(f"📞 **Contact:** {d['contact']}")
        with c3:
            # 🛠️ Sanitized extraction mapping to guarantee safe execution inside join()
            raw_symptoms = d["symptoms"] if isinstance(d["symptoms"], list) else d["symptoms"].split(",")
            symptoms = [str(s).strip() for s in raw_symptoms if s]
            st.markdown(f"🩺 **Indicators:** {', '.join(symptoms)}")
