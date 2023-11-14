import discord
from discord.ext import commands
from discord import app_commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def help(self, interaction: discord.Interaction):
        await interaction.response.send_message('Commands:' +
                                "\n/ask_waifu_chan - ask your personal waifu assistance a question." +
                                "\n/request - place a service request. (not implemented yet)",
                                ephemeral=True)
