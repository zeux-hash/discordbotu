import discord
from discord.ext import commands
import random
import requests
import os
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def cop(ctx, cop: str):
    await ctx.send("Düşünüyorum...")
    if cop == "pet_şişe" or cop == "dergi":
        await ctx.send("Kağıt ve Plastik Kutusuna At!")
    elif cop == "cam_şişesi" or cop == "maden_suyu_şişesi":
        await ctx.send("Cam Kutusuna At!")
    elif cop == "alet_çantası" or cop == "çivi":
        await ctx.send("Metal Kutusuna At!")
    else:
        await ctx.send("Bilmiyom Ki!.")


@bot.command()
async def mem(ctx):
    await ctx.send("resim geliooo..")
    dosya = os.listdir("C:\\Users\\zeux\\Desktop\\yazilimlar\\images")
    bam = random.choice(dosya)
    await ctx.send("geldi.")
    await ctx.send(file=discord.File(f"C:\\Users\\zeux\\Desktop\\yazilimlar\\images\\{bam}"))

@bot.command()
async def animal(ctx):
    await ctx.send("resim geliooo..")
    dosya = os.listdir("C:\\Users\\zeux\\Desktop\\yazilimlar\\animalimages")
    bam = random.choice(dosya)
    await ctx.send("geldi.")
    await ctx.send(file=discord.File(f"C:\\Users\\zeux\\Desktop\\yazilimlar\\images\\{bam}"))

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def commands(ctx):
    """Help"""
    await ctx.send("Komutlar : hello,add,roll,choose,repeat,heh,joined")

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

bot.run("no way")
