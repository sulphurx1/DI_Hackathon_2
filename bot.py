from discord.ext import commands
import discord
import sqlite3 as sql
<<<<<<< Updated upstream


BOT_TOKEN = 'MTA4MTEzMTQ1MDEwNTA3Mzc3Ng.GB2WxL.pIMaOgrddtDBNyKMHBVM8VKAz5rTIDLKvZPYGs'
=======
import random
import ctypes


BOT_TOKEN = 'MTA4MTEzMTQ1MDEwNTA3Mzc3Ng.Gs40vp.fpUqz0f-eCmWlDyDeEUZhD3UqTUFApiRvbeq4o'
>>>>>>> Stashed changes
CHANNEL_ID = 1081134222015733794

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Hello World!')
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Link The Megatron Clowns is online!')

<<<<<<< Updated upstream

@bot.command()
async def news(ctx, word):
    async with sql.connect('Database.db') as db:
        async with db.cursor() as cursor:
            await cursor.execute('SELECT title FROM News WHERE title = word')
            data = await cursor.fetchone()
            if data:
                await ctx.send(data)
            else:
                pass    
=======
db = sql.connect('news.db')
cursor = db.cursor()

x = random.randint(1, 7)
y = cursor.execute("SELECT * FROM News ORDER BY {} LIMIT 1".format(x))
y = cursor.fetchall()
print()
@bot.command()
async def news(ctx):
    await ctx.send(y)    
>>>>>>> Stashed changes


bot.run(BOT_TOKEN)
