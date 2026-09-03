import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    client = genai.Client(api_key=GEMINI_API_KEY)
else:
    client = None


def generate_helpline_response(user_message, conversation_history=None):
    if not GEMINI_API_KEY or client is None:
        return "I am currently running in offline simulation mode. Please set a valid GEMINI_API_KEY."

    system_instruction = (
        "You are a helpful, empathetic medical helpdesk assistant "
        "at MetroHealth Central Hospital. "
        "Guide patients politely based on hospital details. "
        "Never diagnose complex conditions. "
        "Always advise patients to book appointments or seek "
        "immediate emergency care if symptoms appear severe."
    )

    prompt = f"""
{system_instruction}

Patient message:
{user_message}
"""

    # Primary model choice
    primary_model = "gemini-3.6-flash"
    fallback_model = "gemini-2.5-flash"

    try:
        # Attempt generation using primary model
        response = client.models.generate_content(
            model=primary_model,
            contents=prompt,
        )
        return response.text

    except Exception as e:
        # If primary model is down due to a 503 high demand spike, seamlessly try the fallback
        if "503" in str(e) or "UNAVAILABLE" in str(e).upper():
            try:
                response = client.models.generate_content(
                    model=fallback_model,
                    contents=prompt,
                )
                return response.text
            except Exception as fallback_error:
                return f"All Gemini model pipelines are experiencing heavy global demand. Please retry in a few seconds. Details: {str(fallback_error)}"
        
        return f"An error occurred while generating context: {str(e)}"
