import discord
import random


def genpass(sifre_uzunlugu):
    degiskenler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    sifre = ""
    for i in range(sifre_uzunlugu):
        sifre += random.choice(degiskenler)
    print("Parolanız :",sifre)
    return sifre


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$olustur'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$genpass'):
        await message.channel.send("Şifreniz Oluşturuldu!")
        await message.channel.send(genpass(10))

client.run("token buraya")
