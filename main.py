import os
import discord

my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$hello"):
    await message.channel.send("Hello!")

  if message.content.startswith("!Gryffindor"):
    await message.channel.send("Their daring, nerve and chivalry set Gryffindors apart")

client.run(my_secret)