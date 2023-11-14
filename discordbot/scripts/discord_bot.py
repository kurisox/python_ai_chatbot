import json
import os
import aiohttp
import discord
from discord.ext import commands
from dotenv import load_dotenv
from cogs import AskAI, Help

load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")

class MyClient(commands.Bot):

    def __init__(self, intents):
        super().__init__(command_prefix="!", intents=intents)
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        await self.add_cog(AskAI.AI(self))
        await self.add_cog(Help.Help(self))
        print("Cogs loaded.")
        print('------')
        await self.tree.sync()
        print("Tree loaded.")
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        await self.process_commands(message)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(discord_token)