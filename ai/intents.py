INTENT_PATTERNS = {
    "emergency": ["emergency", "ambulance", "accident", "severe pain", "bleeding heavily", "unconscious", "stroke"],
    "appointment": ["appointment", "book", "schedule", "consultation", "visit doctor"],
    "visiting_hours": ["visiting hours", "visiting time", "visitor", "see patient", "open hours"],
    "documents": ["documents", "id card", "what to bring", "insurance papers", "required papers"],
    "contact": ["contact", "phone number", "call", "address", "location", "where are you located"],
    "cardiology": ["chest pain", "heart", "cardio", "palpitations", "angina", "shortness of breath"],
    "dermatology": ["skin", "rash", "acne", "mole", "itching", "dermatologist", "hair loss"],
    "orthopedics": ["bone", "joint", "fracture", "knee", "back pain", "sprain", "ortho"],
    "neurology": ["headache", "migraine", "brain", "numbness", "seizure", "paralysis", "tremor"],
    "pediatrics": ["child", "baby", "infant", "pediatric", "kid fever", "vaccine for kid"]
}

INTENT_RESPONSES = {
    "emergency": "**CRITICAL NOTICE**: For life-threatening medical emergencies, dial our 24/7 Emergency Line immediately at **+1 (555) 019-9111** or go to Gate 1, Ground Floor.",
    "appointment": "You can schedule a consultation using the **Appointments** page in the left sidebar, or phone central booking at **+1 (555) 010-8800**.",
    "visiting_hours": "General wards: **10:00 AM – 12:00 PM** and **04:30 PM – 07:00 PM** daily. ICU visitation is restricted to **05:00 PM – 06:00 PM**.",
    "documents": "Please bring: 1) Photo ID, 2) Insurance Card, 3) Prior diagnostic records, and 4) Current medication list.",
    "contact": "Address: **742 Healthcare Parkway, NY 10001**.\nGeneral: **+1 (555) 010-8800** | Emergency: **+1 (555) 019-9111**.",
    "cardiology": "Your symptoms indicate our **Cardiology Department** (Wing A, 2nd Floor). Specialist: Dr. Sarah Jenkins (Mon, Wed, Fri).",
    "dermatology": "For skin or hair concerns, schedule with our **Dermatology Department** (Wing B, 1st Floor). Specialist: Dr. Marcus Vance (Tue, Thu, Sat).",
    "orthopedics": "For bone, joint, or spine symptoms, consult the **Orthopedics Department** (Wing C, Ground Floor). Specialist: Dr. Elena Rostova (Mon, Tue, Thu).",
    "neurology": "For nervous system or persistent head pain, visit the **Neurology Department** (Wing A, 3rd Floor). Specialist: Dr. Tariq Al-Mansoor (Wed, Thu, Fri).",
    "pediatrics": "For infants and children, consult our **Pediatrics Department** (Wing D, 1st Floor). Specialist: Dr. Priya Sharma (Mon, Wed, Sat)."
}