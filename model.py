from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def create_groq_client():
    return ChatGroq(
        model="llama-3.3-70b-versatile",
    )

