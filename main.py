import os
import json
import requests

from dotenv import load_dotenv

from tools import book_search
from memory import load_memory, save_memory
from prompts import SYSTEM_PROMPT

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "openrouter/free"

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "book_search",
            "description": "Search books using Google Books API.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Book title, author or subject"
                    }
                },
                "required": ["query"]
            }
        }
    }
]

TOOL_FUNCTIONS = {
    "book_search": book_search
}


import time
import requests

def call_llm(messages):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": messages,
        "tools": TOOLS
    }

    retries = 3

    for i in range(retries):

        response = requests.post(
            OPENROUTER_URL,
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 429:
            print(f"Rate limited. Retrying ({i+1}/{retries})...")
            time.sleep(5)
            continue

        print(response.text)
        response.raise_for_status()

    raise Exception("OpenRouter is currently rate limited. Please try again later.")


def run_tool(tool_call):

    tool_name = tool_call["function"]["name"]
    tool_args = json.loads(tool_call["function"]["arguments"])

    print("\nCalling Tool:", tool_name)
    print("Arguments:", tool_args)

    result = TOOL_FUNCTIONS[tool_name](**tool_args)

    print("\nTool Output:\n")
    print(result)

    return result


def agent_loop(user_input):

    memory = load_memory()

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(memory)

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    for _ in range(5):

        response = call_llm(messages)

        message = response["choices"][0]["message"]

        messages.append(message)

        if message.get("tool_calls"):
            for tool_call in message["tool_calls"]:

                tool_result = run_tool(tool_call)

                # Debug: Print what is being sent back to the LLM
                print("\n==============================")
                print("Tool Result Sent To LLM:")
                print("==============================")
                print(tool_result)

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call["id"],
                        "name": tool_call["function"]["name"],
                        "content": tool_result
                    }
                )

            continue

        final_answer = message.get("content") or "No response generated."

        save_memory(messages[1:])

        return final_answer

    return "Maximum iterations reached."


if __name__ == "__main__":

    print("=" * 50)
    print("📚 Book Search Agent")
    print("=" * 50)

    while True:

        query = input("\nYou: ")

        if query.lower() == "exit":
            break

        try:
            answer = agent_loop(query)
            print("\nAgent:\n")
            print(answer)

        except Exception as e:
            print(e)