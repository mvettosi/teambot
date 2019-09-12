from discord.ext import commands
from discord import utils


def setup(bot):
    bot.add_cog(DevCog(bot))


class DevCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test_command(self, context):
        times_iterator = filter(lambda em: em.name.startswith('schedule_'), context.guild.emojis)
        time_emojis = [time_emoji for time_emoji in times_iterator]
        time_emojis = sorted(time_emojis, key=lambda emoji: emoji.name)
        for emoji in time_emojis:
            await context.send(f'`{emoji.name}`')

    @commands.command()
    async def reload(self, context):
        for extension in self.bot.loaded_extensions:
            self.bot.reload_extension(extension)
