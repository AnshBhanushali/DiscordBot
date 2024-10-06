import discord
from discord.ext import commands

# Create bot instance with a command prefix
bot = commands.Bot(command_prefix='!')

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f'Bot is online and connected as {bot.user}')

# Command: Greet the user
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}, how are you?')

# Command: Repeat back the user's message
@bot.command()
async def repeat(ctx, *, message):
    await ctx.send(message)

# Command: Get server info
@bot.command()
async def serverinfo(ctx):
    server_name = ctx.guild.name
    member_count = ctx.guild.member_count
    await ctx.send(f'Server Name: {server_name}\nMember Count: {member_count}')

# Command: Roll a dice
import random
@bot.command()
async def roll(ctx):
    dice_roll = random.randint(1, 6)
    await ctx.send(f'🎲 You rolled a {dice_roll}!')

# Error handling: If a command is not found
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Sorry, that command does not exist.')

# Run the bot with your token
bot.run('YOUR_DISCORD_BOT_TOKEN')