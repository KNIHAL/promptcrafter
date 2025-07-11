
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()

llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.7,
    max_tokens=1024,  # safer default
    timeout=60,
    max_retries=2,
    api_key=os.getenv("GROQ_API_KEY")
)
