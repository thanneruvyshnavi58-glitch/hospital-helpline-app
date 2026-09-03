import streamlit as st
from database.db import get_hospital_info

# Targeted CSS styling for the main container
st.markdown("""
<style>
/* Scope styling to main area only */
.main .block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1100px;
}

/* Hero Banner */
.hero-banner {
    background: linear-gradient(135deg, #0f172a 0%, #0369a1 60%, #0d9488 100%);
    padding: 2.2rem 2.5rem;
    border-radius: 16px;
    color: #ffffff;
    margin-bottom: 1.5rem;
    box-shadow: 0 10px 25px -5px rgba(3, 105, 161, 0.2);
}
.hero-banner h1 {
    margin: 0;
    font-size: 2.1rem;
    font-weight: 700;
    letter-spacing: -0.5px;
    color: #ffffff !important;
}
.hero-banner p {
    margin-top: 0.4rem;
    font-size: 1.05rem;
    color: #e0f2fe;
    opacity: 0.95;
}

/* Emergency Alert Strip */
.emergency-strip {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #fef2f2;
    border: 1px solid #fecaca;
    border-left: 5px solid #ef4444;
    border-radius: 10px;
    padding: 0.9rem 1.4rem;
    margin-bottom: 1.8rem;
}
.emergency-text {
    font-size: 0.98rem;
    color: #991b1b;
    font-weight: 500;
}
.emergency-phone {
    font-weight: 700;
    color: #b91c1c;
    font-size: 1.1rem;
}

/* Metric Stat Card */
.stat-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    border-top: 3px solid #0284c7;
    height: 100%;
}
.stat-card-title {
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #64748b;
    font-weight: 600;
    margin-bottom: 0.3rem;
}
.stat-card-val {
    font-size: 1.35rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 0.2rem;
}
.stat-card-sub {
    font-size: 0.85rem;
    color: #0d9488;
    font-weight: 500;
}

/* Content Cards */
.content-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 1.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    margin-top: 1.5rem;
}
.content-card h3 {
    margin-top: 0;
    font-size: 1.15rem;
    font-weight: 600;
    color: #0f172a;
    border-bottom: 1px solid #f1f5f9;
    padding-bottom: 0.6rem;
    margin-bottom: 1rem;
}
.facility-badge {
    display: inline-block;
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    color: #166534;
    font-size: 0.82rem;
    font-weight: 500;
    padding: 0.35rem 0.75rem;
    border-radius: 20px;
    margin: 0.25rem 0.25rem 0.25rem 0;
}
</style>
""", unsafe_allow_html=True)

h = get_hospital_info()

# Hero Banner
st.markdown(f"""
<div class="hero-banner">
    <h1>🏥 {h.get('name', 'MetroHealth Central Hospital')}</h1>
    <p>24/7 AI-Powered Clinical Care, Triage & Navigational Portal</p>
</div>
""", unsafe_allow_html=True)

# Emergency Alert
st.markdown(f"""
<div class="emergency-strip">
    <div class="emergency-text">
        🚨 <strong>Immediate Trauma or Critical Emergency?</strong> Gate 1, Ground Floor is open 24/7.
    </div>
    <div class="emergency-phone">{h.get('emergency_phone', '+1 (555) 019-9111')}</div>
</div>
""", unsafe_allow_html=True)

# 3 Stat Cards
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-card-title">Outpatient Department</div>
        <div class="stat-card-val">08:00 AM - 08:00 PM</div>
        <div class="stat-card-sub">Mon - Sat Active Consultation</div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-card-title">Trauma & ICU Unit</div>
        <div class="stat-card-val">24/7 Operations</div>
        <div class="stat-card-sub">Continuous Level 1 Response</div>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-card-title">Rapid Ambulance Fleet</div>
        <div class="stat-card-val">12 Active Units</div>
        <div class="stat-card-sub">Integrated Telemetry Life-Support</div>
    </div>
    """, unsafe_allow_html=True)

# Split Sections: Facilities & Contact Info
left, right = st.columns([1.6, 1])
with left:
    facilities_raw = h.get("facilities", "")
    facility_list = [f.strip() for f in facilities_raw.split(",") if f.strip()]
    badges_html = "".join([f'<span class="facility-badge">✓ {item}</span>' for item in facility_list])

    st.markdown(f"""
    <div class="content-card">
        <h3>Key Hospital Infrastructure</h3>
        <p style="color: #475569; font-size: 0.95rem; margin-bottom: 1rem;">
            Located at <strong>{h.get('address', 'Medical District')}</strong>. Accredited tertiary care facility equipped with advanced surgical and diagnostic suites:
        </p>
        <div>{badges_html}</div>
    </div>
    """, unsafe_allow_html=True)

with right:
    visiting = h.get('visiting_hours', '10:00 AM - 12:00 PM & 04:30 PM - 07:00 PM')
    st.markdown(f"""
    <div class="content-card">
        <h3>Directory & Hours</h3>
        <p style="margin: 0.4rem 0; font-size: 0.92rem;">
            <span style="color: #64748b;">Central Line:</span><br/>
            <strong style="color: #0284c7;">{h.get('phone', 'N/A')}</strong>
        </p>
        <p style="margin: 0.8rem 0; font-size: 0.92rem;">
            <span style="color: #64748b;">Visiting Hours:</span><br/>
            <span style="color: #334155;">{visiting}</span>
        </p>
        <p style="margin: 0.8rem 0 0.2rem 0; font-size: 0.92rem;">
            <span style="color: #64748b;">Ambulance Status:</span><br/>
            <span style="color: #0d9488; font-weight: 500;">{h.get('ambulance_status', 'Available 24/7')}</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
