import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)


def generate_helpline_response(user_message, conversation_history=None):

    if not GEMINI_API_KEY:
        return "I am currently running in offline simulation mode. Please set a valid GEMINI_API_KEY."

    try:
        # Updated Gemini model
        model = genai.GenerativeModel("gemini-3.6-flash")

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

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"An error occurred while generating context: {str(e)}"