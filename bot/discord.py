from discord.ext import commands
import discord
import sqlite3

def run_query(query, word):
    connection = sqlite3.connect('news.db')
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    results = cursor.fetchall()
    connection.close()
    for key, value in results.items():
        if value == 'title':
            if word in key:
                x = key
                url = key == 'image'
                description = key == 'description'
            return x, url, description



BOT_TOKEN = 'MTA4MTEzMTQ1MDEwNTA3Mzc3Ng.GfjxV8.VrjtioJTJ5NGH72Mi6D9R3kgwZc5sxBQyUYUGo'
CHANNEL_ID = 1081134222015733794

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Hello World!')
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Link The Megatron Clowns is online!')


@bot.command()
async def news(ctx, word, x, url, description):
    run_query(word)
    await ctx.send(x)
    await ctx.send(url)
    await ctx.send(description)


bot.run(BOT_TOKEN)





