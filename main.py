import discord
import os
from dotenv import load_dotenv
load_dotenv()

from discord.ext import commands

bot = commands.Bot(command_prefix='>', help_command=None)


@bot.event
async def on_ready():
    print('bot is ready')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def help(ctx):
    await ctx.send('ur mom')


@bot.command(name='pottyX')
async def pottyx(ctx, spamAmount):
    if not spamAmount.isnumeric():
        await ctx.send('Please enter a number')
        return
    spamAmount = int(spamAmount)
    if spamAmount <= 0 or spamAmount > 25:
        await ctx.send('Please enter a number between 1 and 25')
        return
    for _ in range(spamAmount):
        await ctx.send('<@362862038042673152>')


bot.run(os.getenv("TOKEN"))
