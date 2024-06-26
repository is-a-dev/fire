import nextcord
from nextcord.ext import commands
from bot import Bot
import random


class Utils(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command()
    async def toss(self, interaction: nextcord.Interaction):
        choice = random.choice(["Heads", "Tails"])
        await interaction.send(f"{choice}!")


def setup(bot: Bot):
    bot.add_cog(Utils(bot))
