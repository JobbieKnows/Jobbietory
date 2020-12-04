import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello, My name is Pendragon, apparently I am the most useless bot since I cannot comprehend more than one command simutaneously, but thats most probably my creators fault cause he sucks as well, also Vasilis is a dick!')

    if message.content.startswith('!bye'):
        await message.channel.send('ante re gamisou mounopano')

    if message.content.startswith('!Tell me something about you'):
        await message.channel.send('Well,' +message.author.nick+ ' I am 2 days old atm and I can fuck yo mama')

client.run('NzgzNjY2Mjg1OTAwODU3MzY1.X8eEGg.ljn1AUm7OOn7ntWPNRxF3lSPvmg')
