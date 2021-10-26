import discord
from discord.ext import commands

client = commands.Bot(command_prefix="/", case_insensitive=True)

@client.event
async def on_ready():
    print(f"{client.user.name} is ready.")

@client.command()
async def ip(ctx):
    user=ctx.author
    emb=discord.Embed(title=" IP Comming Soon", description="",colour=user.colour)
    await ctx.send(embed=emb)

@client.command()
async def ping(ctx):
    await ctx.channel.send(f"Returned in {round(client.latency * 1000)} ms")

client.run("OTAxODY2MDcyODI5OTg0NzY4.YXWGOw.sJOXAyGHtboKvwUoPcQtiP76vc4")