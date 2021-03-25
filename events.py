import discord
from discord.ext import commands
token = "ODI0MjIyNDQ3MDExODg5MTcz.YFsO-A.TpUoaQDgvDiQhM-ORbax4AqFXp4"

client = commands.Bot(
    command_prefix = "$ ",
    description    = "a test python-discord bot")

@client.event
async def on_ready():
    print(f"bot {client.user} is active...")

@client.event
async def on_member_join(member):
    print(f"{member} has joined...")

@client.event
async def on_member_remove(member):
    print(f"{member} has left...")

client.run(token)