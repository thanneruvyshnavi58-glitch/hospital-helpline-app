import os
import time
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
        return (
            "I am currently running in offline simulation mode. "
            "Please set a valid GEMINI_API_KEY."
        )

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

    # Current Gemini model
    model = "gemini-3.6-flash"

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
            )

            return response.text

        except Exception as e:

            error_message = str(e)

            if "503" in error_message or "UNAVAILABLE" in error_message.upper():

                if attempt < 2:
                    time.sleep(3)
                    continue

                return (
                    "Gemini is temporarily experiencing high demand. "
                    "Please try sending your message again in a few seconds."
                )

            return f"An error occurred while generating response: {error_message}"