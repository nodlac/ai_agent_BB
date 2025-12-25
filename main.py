import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():
    argparser = argparse.ArgumentParser(description="chatbot")
    argparser.add_argument("user_prompt", type=str, help="User Prompt")
    args = argparser.parse_args()

    messages = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]

    print(messages)

    response = client.models.generate_content(model="gemini-2.5-flash",
                                              contents=messages)
    print(
        f"Candidate Tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
    print(f"response: {response.text}")


if __name__ == "__main__":
    main()
