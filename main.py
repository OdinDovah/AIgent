import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    user_prompt = sys.argv[1]
    verbose = "--verbose" in sys.argv[2:]
    messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    if len(sys.argv) < 2:
        print("Error: Missing prompt")
        sys.exit(1)
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"Response: \n{response.text}")
    else:
        print(f"Response: \n{response.text}")


if __name__ == "__main__":
    main()
