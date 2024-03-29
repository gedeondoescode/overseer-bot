import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import wavelink

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(aliases = ['summon'])
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"Connected to {channel}.")

    @commands.command(aliases = ['scram', 'exit'])
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.send(f"Exited {channel}.")

def setup(client):
    client.add_cog(Music(client))
