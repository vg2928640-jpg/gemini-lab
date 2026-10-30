from google import genai
from dotenv import load_dotenv
import os

#Using gemini

# Load variables from .env
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = input("How can I help you: ")

# Send request using a stable model alias to avoid 503 overloads
response = client.models.generate_content(
    model="gemini-3.5-flash", 
    contents=prompt,
)

# Display the response
print(response.text)
