import discord
print("Welcome!")
print("Bubatz Bot by J.Kakaofanatiker")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="420"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

# Bubatz message
    if "420" or "Bubatz" or "Weed" or "Cannabis" or "Joint" in message.content:
        await message.channel.send('Bubatz:thumbsup:')

# Doge Picture
    if "Bot" in message.content:
        await message.channel.send('https://jkakaofanatiker.tk/DCimg/Bubatz_lustiges_wort.jpg')

# Credits
    if "credits" in message.content:
        await message.channel.send("""**Bubatz Bot**
        Made by J.Kakaofanatiker
        https://twitter.com/kakaofanatiker
        License: GLP-3.0
        https://github.com/JKakaofanatiker/bubatz-bot
        """)


f = open("token.txt")
text = f.read()
f.close()
client.run(text)
