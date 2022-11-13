import discord
import random
from discord import app_commands
from discord.ext import commands
from discord import Interaction
from discord import Object

class _common(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="따라하기", description="봇이 말을 따라합니다.")
    async def 따라하기(self, interaction: Interaction, 말:str):
        await interaction.response.send_message(f'{말}')

    @app_commands.command(name="주사위", description="주사위를 굴립니다.")
    async def 주사위(self, interaction: Interaction, 최대:int):
        await interaction.response.send_message(f'> :game_die:를 던져 `{+random.randint(1, 최대)}`이 나왔습니다. (1~{최대})')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        _common(bot)
    )