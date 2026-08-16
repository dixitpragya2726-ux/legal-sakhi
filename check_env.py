import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GEMINI_API_KEY")

if key:
    print(f"Key found! Starts with: {key[:10]}...")
else:
    print("Key NOT found - .env is not being read correctly")   