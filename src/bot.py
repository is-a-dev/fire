import nextcord
from nextcord.ext import tasks
import asyncio
from nextcord.ext import commands
import logging
from database import Database
import os
from dotenv import load_dotenv
import subprocess


class Bot(commands.Bot):
    def __init__(self, db_path: str, bot_extensions: list[str]):
        intents = nextcord.Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(
            intents=intents,
            allowed_mentions=nextcord.AllowedMentions(
                everyone=False, roles=False, users=True, replied_user=True
            ),
        )
        self.persistent_views_added = False
        self.bot_extensions = bot_extensions
        self.db = Database(db_path)

        # Logging
        self.logger = logging.getLogger("fire")
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(filename="fire.log", encoding="utf-8", mode="w")
        handler.setFormatter(
            logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
        )
        self.logger.addHandler(handler)

    @tasks.loop(seconds=60)
    async def update(self):
        output = subprocess.check_output(["git", "pull"]).decode()
        if "Already up to date." not in output:
            self.logger.info("Changes detected, updating bot")
            exit("Changes detected, updating bot")

    async def on_ready(self):
        await self.db.create_tables()
        self.update.start()
        self.logger.info(f"Logged in as {self.user} ({self.user.id})")
        print(f"Logged in as {self.user} ({self.user.id})")

    def load_extensions(self):
        for ext in self.bot_extensions:
            self.load_extension(ext)
            self.logger.info(f"Loaded extension {ext}")
            print(f"Loaded extension {ext}")


if __name__ == "__main__":
    load_dotenv()
    bot = Bot(
        os.getenv("DATABASE_PATH"),
        ["exts.help", "exts.errors", "exts.utils", "exts.fun"],
    )
    try:
        bot.load_extensions()
        bot.run(os.getenv("TOKEN"))
    except KeyboardInterrupt:
        bot.logger.info("Bot terminated by SIGINT")
        print("Bot terminated by SIGINT")
    finally:
        asyncio.run(bot.db.disconnect())
