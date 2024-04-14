import nextcord
from nextcord.ext import commands, application_checks
from bot import Bot


class Utils(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command()
    async def ping(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(
            title="Pong!", description=f"Latency: {round(self.bot.latency * 1000)}ms"
        )
        await interaction.send(embed=embed)


def setup(bot: Bot):
    bot.add_cog(Utils(bot))
