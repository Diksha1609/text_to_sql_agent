import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt
        )

        if response and response.candidates:
            candidate = response.candidates[0]
            if candidate.content and candidate.content.parts:
                return candidate.content.parts[0].text.strip()
        
        return "No response generated."

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("API KEY LOADED:", os.getenv("GEMINI_API_KEY") is not None)
    print(generate_response("Explain SQL SELECT in one line"))
