import discord
import os
from dotenv import load_dotenv
load_dotenv()

from discord.ext import commands

bot = commands.Bot(command_prefix='>', help_command=None)


@bot.event
async def on_ready():
    print('bot is ready')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please enter a number')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('ur mom')
    else:
        print(error)
        await ctx.send('Error')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command(name='urmom')
async def ur_mom(ctx):
    await ctx.send('is fat')


@bot.command()
async def help(ctx):
    emoji = bot.get_emoji(750548895146180659)
    await ctx.send(emoji)


@bot.command(name='pottyX')
async def pottyx(ctx, spamAmount: int):
    print(f"called by {ctx.author}")
    emoji = bot.get_emoji(729563457892122787)
    for x in range(spamAmount):
        await ctx.send(f'sexy boi arya {emoji} <@362862038042673152> ({x + 1})'
                       )


bot.run(os.getenv("TOKEN"))
