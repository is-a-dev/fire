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

    @nextcord.slash_command()
    @application_checks.is_owner()
    async def database(self, interaction: nextcord.Interaction):
        pass

    @database.subcommand()
    @application_checks.is_owner()
    async def reconnect(self, interaction: nextcord.Interaction):
        await interaction.response.defer()
        await self.bot.db.disconnect()
        await self.bot.db.connect()
        await interaction.send("Reconnected to the database.")


def setup(bot: Bot):
    bot.add_cog(Utils(bot))
