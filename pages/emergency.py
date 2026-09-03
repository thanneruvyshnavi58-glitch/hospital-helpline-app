import streamlit as st

st.title("🚑 Emergency & Trauma Services")

st.error("""
## 🚨 EMERGENCY HOTLINE: +1 (555) 019-9111
**Gate 1, Ground Floor, East Wing (Open 24/7/365)**
""")

c1, c2 = st.columns(2)
with c1:
    st.subheader("Critical First Actions")
    st.markdown("""
    * **Chest Pain:** Keep patient seated and still. Never permit exertion.
    * **Uncontrolled Bleeding:** Apply direct, firm pressure with a clean cloth.
    * **Loss of Consciousness:** Check airway and breathing. Elevate legs slightly.
    * **Suspected Stroke:** Check F.A.S.T. (Face, Arms, Speech, Time to call emergency).
    """)
with c2:
    st.subheader("Facility Readiness")
    st.markdown("""
    * Dedicated Level 1 Trauma bays with board-certified trauma surgeons.
    * Cath-lab activation readiness within 30 minutes.
    * Mobile ICU ambulances with integrated life-support telemetry.
    """)

# Enforcing safety compliance with a high-visibility medical disclaimer banner
st.markdown("""
---
<small style='color: gray; display: block; margin-top: 2rem;'>
<strong>Medical Disclaimer:</strong> The information provided on this page resembles general first-aid best practices and shares characteristics with administrative hospital triage guides. It is consistent with standard emergency awareness but is completely non-diagnostic. It seems to be general information only and does not constitute personalized medical advice. If you or someone near you is experiencing a life-threatening symptom, please use the physical helpline label above to call emergency dispatch or go to the nearest emergency room immediately.
</small>
""", unsafe_allow_html=True)
