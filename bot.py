from discord.ext import commands
import discord
import sqlite3 as sql


BOT_TOKEN = 'MTA4MTEzMTQ1MDEwNTA3Mzc3Ng.GB2WxL.pIMaOgrddtDBNyKMHBVM8VKAz5rTIDLKvZPYGs'
CHANNEL_ID = 1081134222015733794

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Hello World!')
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Link The Megatron Clowns is online!')


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


bot.run(BOT_TOKEN)
