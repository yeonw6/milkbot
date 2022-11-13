import discord
from discord import Intents
from discord.ext import commands
from discord import Game
from discord import Status
from discord import Object

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!',
            intents=Intents.all(),
            sync_command=True,
            application_id='561417853417422858'
        )
        self.initial_extension = [
            "Cogs.0_help",
            "Cogs.1_common",
            "Cogs.select",
        ]

    async def setup_hook(self):
        for ext in self.initial_extension:
            await self.load_extension(ext)
        await bot.tree.sync()

    async def on_ready(self):
        print("login")
        print(self.user.name)
        print(self.user.id)
        print("===============")
        game = Game("....")
        await self.change_presence(status=Status.online, activity=game)

bot = MyBot()
bot.run('NTYxNDE3ODUzNDE3NDIyODU4.Gv9pxf.P7rai3X_7l9UPOsP4C3v9l9xrpy5GT5boJiXME')