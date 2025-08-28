import os 
from dotenv import load_dotenv
from openai import AsyncOpenAI



#1.
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")


if not gemini_key:
    raise ValueError("Gemini_api_key was not found")


#2.
client = AsyncOpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


