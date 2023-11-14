import json
import os
import aiohttp
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands

load_dotenv()

api_url = os.getenv("API_URL")
headers = {"Content-Type": "application/json"}

payload = {
    "max_tokens": 512,
    "messages": []
}

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @app_commands.command(name="ask_waifu_chan")
    async def askwaifuchan(self, interaction: discord.Interaction, message: str):
        print(f"Received interaction: {interaction}")
        print(f"Received interaction-message: {interaction.message}")
        print(f"Received interaction-message: {message}")
        prompt_message = {
            "role": "user",
            "content": f"{message} ### Response: "
        }
        payload["messages"].append(prompt_message)
        await interaction.response.defer(ephemeral=True)
        async with aiohttp.ClientSession() as session:
            async with session.post(url=api_url, data=json.dumps(payload), headers=headers) as response:
                reply = await response.json()
                reply_content = reply["choices"][0]["message"]["content"]

                # Send an ephemeral response to the interaction
                print(f"Sending response: {reply_content}")
                await interaction.followup.send(reply_content, ephemeral=True)

        payload["messages"][payload["messages"].index(prompt_message)]["content"] += reply_content