from discord.ext import commands
import discord
import sqlite3 as sql
import random


BOT_TOKEN = 'MTA4MTEzMTQ1MDEwNTA3Mzc3Ng.GxMW6t.GClNF3vWNXm6DZJOr32ThYJMaqXciPLVho3UEI'
CHANNEL_ID = 1081134222015733794

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Hello World!')
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Link The Megatron Clowns is online!')


db = sql.connect('Database.db')
cursor = db.cursor()

x = random.randint(1, 6)
y = cursor.execute("SELECT * FROM NEWS ORDER BY {} LIMIT 1".format(x))
y = cursor.fetchall()
print(y)
@bot.command()
async def news(ctx):
    await ctx.send(y)    


bot.run(BOT_TOKEN)
