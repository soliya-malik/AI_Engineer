import os
from google import genai

def main():
    # Retrieve the API key from environment variables
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: Please set the GEMINI_API_KEY environment variable.")
        print("Example: $env:GEMINI_API_KEY='your_api_key_here'")
        return

    # Initialize the GenAI client
    client = genai.Client(api_key=api_key)

    prompt = "Explain the role of an AI Engineer in 3 bullet points."
    print(f"Sending prompt to Gemini: '{prompt}'\n")

    # Call the model
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    
    print("--- Response ---")
    print(response.text)

if __name__ == "__main__":
    main()