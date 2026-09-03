import streamlit as st
from database.db import get_faqs

st.title("❓ Frequently Asked Questions")
query = st.text_input("Search FAQs:")
faqs = get_faqs(query)

if not faqs:
    st.info("No matching questions found.")
    st.stop()  # 🛠️ Replaced legacy function 'return' with a structural Streamlit execution stop

categories = sorted(list(set(f["category"] for f in faqs)))
for cat in categories:
    st.subheader(cat)
    for item in [f for f in faqs if f["category"] == cat]:
        with st.expander(item["question"]):
            st.write(item["answer"])
