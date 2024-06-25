import nextcord
from nextcord.ext import commands
from bot import Bot
import random


class Utils(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.author.id in [598245488977903688] and "." in message.content:
            await message.add_reaction("🥚")
        if message.author.id in [961063229168164864] and "." in message.content:
            await message.add_reaction("🐒")

    @nextcord.slash_command()
    async def toss(self, interaction: nextcord.Interaction):
        choice = random.choice(["Heads", "Tails"])
        await interaction.send(f"{choice}!")


def setup(bot: Bot):
    bot.add_cog(Utils(bot))
