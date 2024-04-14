import urllib.parse
import nextcord
from nextcord.ext import commands
from bot import Bot
from exts.help import LinkView


class Utils(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command()
    async def ping(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(
            title="Pong!", description=f"Latency: {round(self.bot.latency * 1000)}ms"
        )
        await interaction.send(embed=embed)

    @nextcord.slash_command()
    async def google(self, interaction: nextcord.Interaction, query: str):
        google_url = f"https://www.google.com/search"
        params = {"q": query}
        search_url = f"{google_url}?{urllib.parse.urlencode(params)}"
        search_view = LinkView(query, search_url)
        await interaction.send(view=search_view)


def setup(bot: Bot):
    bot.add_cog(Utils(bot))
