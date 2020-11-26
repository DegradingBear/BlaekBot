import discord, random
from discord.utils import get
import os
import getPrice

client = discord.Client()
with open('jokes.txt', 'r', encoding='utf-8') as f:
    jokes = f.readlines()

with open('hate.txt', 'r', encoding='utf-8') as f:
    hated = f.readlines()

with open('admins.txt', 'r', encoding='utf-8') as f:
    admins = f.readlines()

noiceList = []
for root, direcories, files in os.walk('noice/', topdown=False):
    for name in files:
        noiceList.append(os.path.join(root, name))

poglist = []
for root, direcories, files in os.walk('pog/', topdown=False):
    for name in files:
        poglist.append(os.path.join(root, name))


@client.event
async def on_ready():
    print(f'we have logged in as {client}')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!hate'):
        name = message.content.replace('!hate ', '')
        with open('hate.txt', 'w', encoding='utf-8') as f:
            f.writelines(name)
        await message.channel.send(f'ok, we hate {name.split("#")[0]} now :)')

    if message.content == '!hello':
        name = str(message.author)
        await message.channel.send(f'Hello {name.split("#")[0]} ')
    
    if message.content.startswith('!penis'):
        if message.author != 'Threat <3#0001':
            for i in range(5):
                await message.channel.send('🍆')
            await message.channel.send('lol')
    
    if message.content.startswith('!joke'):
        await message.channel.send(random.choice(jokes))
    
    if str(message.author) in hated:
        if random.randint(1,10) == 10:
            name = str(message.author).split("#")[0]
            await message.channel.send(f'Shut up, {name}')
    
    if "noice" in message.content.lower() or "nice" in message.content.lower():
        niceImg = random.choice(noiceList)
        with open(niceImg, 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
        await message.channel.send("NOICE XD")
    
    if "69" in message.content:
        await message.channel.send("HAHA thats the funny number! XD")
    
    if "pog" in message.content.lower() or "poggers" in message.content.lower():
        pogImg = random.choice(poglist)
        with open(pogImg, 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
    
    if message.content.startswith("!priceof"):
        name = message.content.replace("!priceof ", "")
        try:
            price, url = getPrice.getPrice(name)
            await message.channel.send(f"{name} is currently ${price} \n {url}")
        except IndexError:
            await message.channel.send(f"sorry, I couldnt find {name} on isthereanydeal.com")
        except AttributeError:
            await message.channel.send(f"sorry, I couldnt find {name} on isthereanydeal.com")
    
    if message.content.startswith("!kys"):
        await message.channel.send(f":cry: ok, ill leave :cry:")
        exit()

client.run('NzgxMTExMTU4NjA1MDg2NzIw.X744dA.KsQJCBcKmEk_gyYeYiu05FLZMYA')