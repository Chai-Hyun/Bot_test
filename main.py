import os
import discord
import asyncio
from profanity_filter import ProfanityFilter

my_secret = os.environ['TOKEN']

client = discord.Client()

pf = ProfanityFilter()

@property
def name(self):
  return self._name

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("hello"):
    await message.channel.send("Hello!")

  if message.content.startswith("botname"):
    await message.channel.send("My name is {0.user}".format(client))

  if message.content.startswith("change name"):
    await message.channel.send("To which name do you want to change?")

    def check(msg):
      return msg.author == message.author

    try:
      new_name=await client.wait_for('message', check=check, timeout=10);
    except asyncio.TimeoutError:
      await message.channel.send("Timeout!")
      return

    await message.guild.me.edit(nick=new_name.content)

client.run(my_secret)