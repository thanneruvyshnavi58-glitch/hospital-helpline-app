import os
import json
import re
import urllib.parse
import certifi

from datetime import datetime
from pymongo import MongoClient

# ==========================================
# MongoDB Configuration
# ==========================================

username = os.getenv("MONG0_USER_NAME")

# IMPORTANT:
# Put your NEW MongoDB Atlas database-user password here.
password = os.getenv("MONG0_USER_PASSWORD")
db_name:os.getenv("MONGO_DB_NAME")

escaped_username = urllib.parse.quote_plus(username)
escaped_password = urllib.parse.quote_plus(password)
escaped_db_name = urllib.parse.quote_plus(db_name)

MONGO_URI = (
    f"mongodb+srv://{escaped_username}:{escaped_password}"
    "@{escaped_db_name}.z1tnmjn.mongodb.net/"
    "?retryWrites=true&w=majority&appName=Hospitalhelpline"
)

DB_NAME = "hospital_helpline"

DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data"
)


# ==========================================
# Get Database
# ==========================================

def get_db():
    client = MongoClient(
        MONGO_URI,
        serverSelectionTimeoutMS=5000,
        tlsCAFile=certifi.where()
    )

    client.admin.command("ping")

    return client[DB_NAME]


# ==========================================
# Initialize Database
# ==========================================

def init_db():

    try:
        db = get_db()
        db.command("ping")

        print("MongoDB connected successfully!")

    except Exception as e:
        print(f"[WARN] MongoDB offline or unreachable: {e}")
        return

    # Hospital information
    if db.hospital_info.count_documents({}) == 0:

        db.hospital_info.insert_one({
            "name": "MetroHealth Central Hospital",
            "address": "742 Healthcare Parkway, Medical District, NY 10001",
            "phone": "+1 (555) 010-8800",
            "emergency_phone": "+1 (555) 019-9111",
            "working_hours": "OPD: Mon-Sat 08:00 AM - 08:00 PM | Emergency: 24/7",
            "visiting_hours": "10:00 AM - 12:00 PM & 04:30 PM - 07:00 PM",
            "facilities": "24/7 Emergency & Trauma, CT & MRI, Dialysis Unit, NICU",
            "ambulance_status": "24/7 Mobile ICU Fleet Available"
        })

    # Load JSON files
    def load_json_seed(filename, collection):

        if collection.count_documents({}) == 0:

            path = os.path.join(DATA_DIR, filename)

            if os.path.exists(path):

                with open(path, "r", encoding="utf-8") as f:
                    items = json.load(f)

                if items:
                    collection.insert_many(items)

    load_json_seed("departments.json", db.departments)
    load_json_seed("doctors.json", db.doctors)
    load_json_seed("faqs.json", db.faqs)


# ==========================================
# Hospital Information
# ==========================================

def get_hospital_info():

    db = get_db()

    info = db.hospital_info.find_one(
        {},
        {"_id": 0}
    )

    if not info:

        return {
            "name": "MetroHealth Central Hospital",
            "address": "742 Healthcare Parkway, Medical District, NY 10001",
            "phone": "+1 (555) 010-8800",
            "emergency_phone": "+1 (555) 019-9111",
            "working_hours": "OPD: Mon-Sat 08:00 AM - 08:00 PM | Emergency: 24/7",
            "visiting_hours": "10:00 AM - 12:00 PM & 04:30 PM - 07:00 PM",
            "facilities": "24/7 Trauma, Advanced ORs, CT & MRI, Dialysis Unit, NICU",
            "ambulance_status": "24/7 Mobile ICU Fleet Available"
        }

    return info


# ==========================================
# Departments
# ==========================================

def get_departments(search_term=""):

    db = get_db()

    if not search_term:
        return list(
            db.departments.find(
                {},
                {"_id": 0}
            )
        )

    safe_term = re.escape(search_term.strip())

    regex = {
        "$regex": safe_term,
        "$options": "i"
    }

    return list(
        db.departments.find(
            {
                "$or": [
                    {"name": regex},
                    {"description": regex},
                    {"symptoms": regex}
                ]
            },
            {"_id": 0}
        )
    )


# ==========================================
# Doctors
# ==========================================

def get_doctors(dept_filter=None, search_name=""):

    db = get_db()

    query = {}

    if dept_filter and dept_filter != "All Departments":
        query["department"] = dept_filter

    if search_name:

        safe_name = re.escape(search_name.strip())

        query["$or"] = [
            {
                "name": {
                    "$regex": safe_name,
                    "$options": "i"
                }
            },
            {
                "specialization": {
                    "$regex": safe_name,
                    "$options": "i"
                }
            }
        ]

    return list(
        db.doctors.find(
            query,
            {"_id": 0}
        )
    )


# ==========================================
# FAQs
# ==========================================

def get_faqs(search_query=""):

    db = get_db()

    if not search_query:
        return list(
            db.faqs.find(
                {},
                {"_id": 0}
            )
        )

    safe_query = re.escape(search_query.strip())

    regex = {
        "$regex": safe_query,
        "$options": "i"
    }

    return list(
        db.faqs.find(
            {
                "$or": [
                    {"question": regex},
                    {"answer": regex}
                ]
            },
            {"_id": 0}
        )
    )


# ==========================================
# Appointments
# ==========================================

def insert_appointment(
    patient_name,
    age,
    phone,
    department,
    doctor,
    preferred_date,
    preferred_time,
    reason
):

    db = get_db()

    result = db.appointments.insert_one({

        "patient_name": patient_name,
        "age": age,
        "phone": phone,
        "department": department,
        "doctor": doctor,
        "preferred_date": preferred_date,
        "preferred_time": preferred_time,
        "reason": reason,
        "created_at": datetime.utcnow()
    })

    return str(result.inserted_id)