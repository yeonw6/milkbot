import discord
from discord import app_commands
from discord.ext import commands
from discord import Interaction
from discord import Object

class _help(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="도움말", description="명령어 목록을 출력합니다.")
    async def _help(self, interaction: Interaction) -> None:
        embed = discord.Embed(color=0x00FF00)
        embed.set_author(name="🥛 MilkBot v2 Commands | Update 22.10.26.", url="", icon_url="")
        embed.add_field(name="🔎 기본 기능", value="\n  `$따라하기` - 봇이 채팅을 따라칩니다.\n  `$주사위` - 주사위를 굴립니다.\n  `$내정보` - 자신의 정보를 확인합니다.", inline=False)
        embed.add_field(name="🔎 전적 검색",value="<:lol:937559239239536651> League of Legends\n  `$L [소환사명]` - 해당 소환사의 롤 전적을 확인합니다.\n  `$LR` - 이번 주 로테이션 챔피언을 확인합니다.\n  `$TFT [소환사명]` - 해당 소환사의 TFT 랭크를 확인합니다.\n\n<:er:937560199709995128> Eternal Return\n  `$ER [유저명] [시즌]` - 해당 유저의 프로필을 확인합니다.\n\n<:la:937560796509110322> Lostark\n  `$LA [캐릭터명]` - 해당 캐릭터의 정보를 확인합니다. (Test ver.)", inline=False)
        #embed.add_field(name="🔎 음악", value="`$play [제목]` - 해당 제목의 노래를 재생합니다.\n  `$playurl [url]` - 해당 링크 영상을 재생합니다.\n  `$stop` - 현재 재생 중인 노래를 멈춥니다.\n  `$join` - 봇을 음성 채팅방에 넣습니다.\n  `$leave` - 봇을 음성 채팅방에서 내보냅니다.")
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        _help(bot)
    )