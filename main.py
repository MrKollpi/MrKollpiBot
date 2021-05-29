#импорты и т.д.
import discord
import os
import requests
import json
import random


client = discord.Client()


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


#приветсивие
@client.event
async def on_guild_join(guild):
    
    text_channels = guild.text_channels
    
    if text_channels:
        channel = text_channels[0]
    
    await channel.send('Hi, {}!'.format(guild.name))


#вдохновение
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('.quote'):
    quote = get_quote()
    await message.channel.send(quote)


#команды
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  




  data1 = '''```
    if you want to write any of these commands, then write". " at the beginning, and then the command:
    .commands channel
      ". command channel"
    1 | "channel"
    2 | "speed_renders" - soon...
    3 | "rigs" - on 1k - 1.5k subs
    4 | "assets" - on 2k subs
    ```'''




  if message.content.startswith(".commands"):
    await message.channel.send('''
    if you want to write any of these commands, then write". " at the beginning, and then the command:
    .commands channel

    1 | **"channel"**
    2 | ~~"speed_renders"~~ - soon...
    3 | ~~"rigs"~~ - on 1k - 1.5k subs
    4 | ~~"assets"~~ - on 2k subs''')


  #канал
  if message.content.startswith("channel"):
    await message.channel.send('https://www.youtube.com/channel/UCIvkbXOc77IjG79SuhcKCMg')


  #speed_renders
  if message.content.startswith('.speed_renders'):
    await message.channel.send('Coming Soon...')


  #textures
  if message.content.startswith('.textures'):
    await message.channel.send('Opens after the achievement 1k subs on my channel')
  

  #rigs
  if message.content.startswith('.rigs'):
    await message.channel.send('Opens after the achievement 1.5k subs on my channel')


  #assets
  if message.content.startswith('.assets'):
    await message.channel.send('Opens after the achievement 2k subs on my channel')

#help
  if message.content.startswith('.help'):
    await message.channel.send('''
    if you want to write any of these commands, then write". " at the beginning, and then the command:
    .roc 

    commands:
    1 | **"roc"**
    2 | **"ping"**
    3 | **"Hello!"** - on 3 languages (ru/en/es) *dont write'.' before message*
    4 | ~~"random"~~''')
  
  if message.content.startswith('.ping'):
    await message.channel.send('pong!')

#roc
  if message.content.startswith('.roc'):
    await message.channel.send('''
    If you want to play ROC,
    write "stone / paper / scissors":
    .stone
    1 | **"stone"**
    2 | **"scissors"**
    3 | **"paper"**''')

  roc1 = ['**stone**', '**paper**', '**scissors**']
  roc2 = random.choice(roc1)

  if message.content.startswith('.stone'):
    await message.channel.send(roc2)

  if message.content.startswith('.paper'):
    await message.channel.send(roc2)

  if message.content.startswith('.scissors'):
    await message.channel.send(roc2)
#SUPER-DUPER SECRET!
  if message.content.startswith('/protocol top_secret'):
    await message.channel.send(
      'http://pm1.narvii.com/6900/110d78c859d721103715e29a933ccd8f348f7dc7r1-1920-1080v2_uhq.jpg'
    )

client.run(os.getenv('TOKEN'))