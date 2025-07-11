# test_groq.py
import os
from groq import Groq # Make sure you have 'groq' library installed: pip install groq

# Ensure your API key is truly in the environment
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    print("Error: GROQ_API_KEY environment variable not set.")
    exit()

client = Groq(api_key=groq_api_key)

try:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say hello to the world.",
            }
        ],
        model="llama3-8b-8192",
        temperature=0.7,
        max_tokens=50, # Set a small max_tokens for a quick test
    )
    print("Groq API call successful!")
    print(chat_completion.choices[0].message.content)
except Exception as e:
    print(f"Groq API call failed: {e}")