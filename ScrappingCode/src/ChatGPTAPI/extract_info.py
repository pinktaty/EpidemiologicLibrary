from __future__ import print_function
import sys
from openai import OpenAI

def ask_chatGPT(content, api_key, instructions):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": instructions
            },
            {
                "role": "user",
                "content": content
            }
        ],
        temperature=0.7,
        max_tokens=64,
        top_p=1
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_info.py <CONTENT>")
        sys.exit(1)
    print(ask_chatGPT(sys.argv[1]))