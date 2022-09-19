import os
import discord
from dotenv import load_dotenv

#start discord client
load_dotenv()

my_secret = os.getenv('DISCORD_TOKEN')
prefix = '!'
client = discord.Client(intents=discord.Intents.default())

hello_message = '''Hey there! Thanks for inviting me! Let\'s snag all the amazing sales off SSENSE!!!
Please check out my commands by typing !help or !commands'''

@client.event
async def on_ready():
  print(f'{client.user} is now online!')

@client.event
async def on_message(message): 
  if message.author == client.user:
      return  
  # lower case message
  message_content = message.content.lower()  

  
  if message.content.startswith(f'!hello'):
    await message.channel.send(hello_message)
#get token and run file
#must e at the end of the file vvvv
client.run(my_secret)