from discord.ext import commands


class ShameCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # TODO: Check documentation about this
        self.converter = commands.MemberConverter()

    @commands.command(brief="Shame")
    async def shame(self, ctx):
        await ctx.send("test")


def setup(bot):
    bot.add_cog(ShameCog(bot))
