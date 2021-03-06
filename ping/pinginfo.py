import discord
from redbot.core import commands
from redbot.core import checks

BaseCog = getattr(commands, "Cog", object)

class Pinginfo(BaseCog):

    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("ping")

    @commands.command(aliases=["pinginfo"])
    async def ping(self, ctx):
        """Ping the shard and latency"""
        latencies = self.bot.latencies
        msg = ""
        for shard, pingt in latencies:
            msg += "Shard {}/{}: {}ms\n".format(shard + 1, len(latencies), round(pingt*1000))
        em = discord.Embed(title=msg, colour=(await ctx.embed_colour()))
        await ctx.send(embed=em)
