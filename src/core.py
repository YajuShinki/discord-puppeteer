"""The core file and entry point for Puppeteer."""
# Standard Library Imports
import json
import logging
from os import listdir

# Third Party Imports
from discord.ext import commands
import coloredlogs


class Client(commands.Bot):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    
    async def on_ready(self):
        logging.info("%s is online!", self.user.name)

    def load_modules(self):
        """Load all the modules in the bot."""
        for module in listdir("src/modules"):
            if not module.startswith("__"):
                self.load_extension(f"modules.{module[:-3]}")
                logging.info("Loaded module: '%s'", module)

def main() -> None:
    coloredlogs.DEFAULT_FIELD_STYLES.update({'funcName': {'color': 'cyan'}})
    coloredlogs.DEFAULT_FIELD_STYLES["name"]["color"] = 'yellow'
    coloredlogs.DEFAULT_FIELD_STYLES["asctime"]["color"] = 'magenta'
    coloredlogs.install(
        level="INFO",
        fmt="<%(asctime)s> %(name)s / %(funcName)s(%(lineno)s) %(levelname)s %(message)s"
    )
    config = json.load(open("config.json"))
    client = Client(
        command_prefix=config["prefix"], 
        owner_ids=config["owners"]
        )
    client.load_modules()
    client.run(config["token"])

if __name__ == "__main__":
    main()