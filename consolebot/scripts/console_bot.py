import json
import os
import aiohttp
import asyncio
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv("API_URL")
headers = {"Content-Type": "application/json"}

payload = {
    "max_tokens": 512,
    "messages": []
}


async def main():
    while True:
        async with aiohttp.ClientSession() as session:
            prompt = input("User: ")
            message = {
                "role": "user",
                "content": f"{prompt} ### Response: "
            }
            payload["messages"].append(message)
            async with session.post(url=api_url, data=json.dumps(payload), headers=headers) as response:
                reply = await response.json()
                reply_content = reply["choices"][0]["message"]["content"]
                print(reply_content)

            payload["messages"][payload["messages"].index(message)]["content"] += reply_content


asyncio.run(main())
