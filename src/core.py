"""The core file and entry point for Puppeteer."""
# Standard Library Imports
import json
import logging
from os import listdir, path

# Third Party Imports
from discord.ext import commands
import coloredlogs, asyncio, asyncpg

class Client(commands.Bot):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        #Additional kwargs for database
        self.db_address = kwargs["address"] if "address" in kwargs else None
        self.db_username = kwargs["username"] if "username" in kwargs else None
        self.db_password = kwargs["password"] if "password" in kwargs else None

        self.db_conn = None
    
    async def on_ready(self):
        logging.info("%s is online!", self.user.name)
        logging.info("Connecting to PostgreSQL server...")
        #TODO Connect to database
        

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
        command_prefix=config["prefix"] if "prefix" in config else "rp!", 
        owner_ids=config["owners"] if "owners" in config else [],
        address=config["db-address"] if "db-address" in config else None,
        username=config["db-username"] if "db-username" in config else None,
        password=config["db-password"] if "db-password" in config else None
        )
    client.load_modules()
    client.run(config["token"])

if __name__ == "__main__":
    main()