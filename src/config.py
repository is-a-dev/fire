from dotenv import load_dotenv
import os

load_dotenv()


def replace_placeholders(string: str, placeholders: dict) -> str:
    for key, value in placeholders.items():
        string = string.replace(key, value)
    return string


TOKEN = "" or os.getenv("TOKEN")
DATABASE_PATH = "" or os.getenv("DATABASE_PATH")
VIEW_GUILD_ID = 830872854677422150
VIEW_CHANNEL_ID = 1220286726711545926

VIEW_OPEN_LABEL = "Open Thread"
VIEW_CLOSE_LABEL = "Close Thread"

THREAD_MIN_CHAR = 50
THREAD_MIN_FAIL = "Your message must be at least 50 characters long. Please provide more detail about the issue which you are facing."
THREAD_NAME = "Dev Help (member.name)"
THREAD_EMBED_TITLE = "Help Thread"
THREAD_EMBED_RESOURCES = "- [Documentation](https://is-a.dev/docs)\n- [GitHub Repository](https://github.com/is-a-dev/register)"
THREAD_EMBED_DESCRIPTION = "Hello member.mention,\n\nPlease describe your issue in as much detail as possible. If you would like to close this thread, click the button below."
THREAD_CLOSE_MSG = "This thread has been closed. If you have any further questions, feel free to open a new thread."
THREAD_CLOSE_DM = "Your thread has been closed. If you have any further questions, feel free to open a new thread."

SETUP_HELP_ALREADY = "This guild already has a help system set up."
SETUP_HELP_SUCCESS = "Successfully set up help system."
