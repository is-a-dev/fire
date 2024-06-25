import nextcord
from nextcord.ext import commands
from bot import Bot


class Utils(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.author.id in [598245488977903688]:
            await message.add_reaction("🥚")


def setup(bot: Bot):
    bot.add_cog(Utils(bot))
