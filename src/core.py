"""The core file and entry point for Puppeteer."""
# Standard Library Imports
import json
import logging

# Third Party Imports
from discord.ext import commands
import coloredlogs


class Client(commands.Bot):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    
    async def on_ready(self):
        logging.info("%s is online!", self.user.name)

def main() -> None:
    coloredlogs.DEFAULT_FIELD_STYLES.update({'funcName': {'color': 'cyan'}})
    coloredlogs.DEFAULT_FIELD_STYLES["name"]["color"] = 'yellow'
    coloredlogs.install(
        level="INFO",
        fmt="[%(hostname)s] %(asctime)s %(funcName)s(%(lineno)s) %(name)s[%(process)d] %(levelname)s %(message)s"
    )
    config = json.load(open("config.json"))
    client = Client(
        command_prefix=config["prefix"], 
        owner_ids=config["owners"]
        )
    client.run(config["token"])

if __name__ == "__main__":
    main()