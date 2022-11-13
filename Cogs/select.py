import discord
from discord import Interaction, SelectOption, app_commands, Object
from discord.ext import commands
from discord.ui import View, Select

class select(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="메뉴")
    async def select(self, interaction: Interaction) -> None:
        selects = Select(options=[
            SelectOption(
                label="Test 1",
                description="Test 1 역할을 지급 받습니다."
            ),
            SelectOption(
                label="Test 2",
                description="Test 2 역할을 지급 받습니다."
            )
        ])

        async def select_callback(interaction: interaction) -> None:
            if selects.values == ['World 1']:
                await interaction.response.send_message("Hello!")

        selects.callback = select_callback
        view = View()
        view.add_item(selects)
        await interaction.response.send_message("테스트용 메뉴입니다.", view=view)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        select(bot)
    )