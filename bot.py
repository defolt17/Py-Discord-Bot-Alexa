import dotenv
import discord
from discord.ext import commands


client = discord.Client()
bot = commands.Bot(command_prefix='$')
dotenv.load()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

############################


@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(str(str(a) + ' + ' + str(b) + ' = ' + str(a + b)))

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a * b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Bot", description="Alexa", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="defolt_17#3701")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Group", value="№22")

    embed.add_field(name="GitHub", value="https://github.com/defolt17/Py-Discord-Bot-Alexa")

    await ctx.send(embed=embed)


###############################


bot.run(dotenv.get('BOT_TOKEN')) #Your '.env' file variable
