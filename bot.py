import dotenv
import discord
from discord.ext import commands
from random import randint


client = discord.Client()
bot = commands.Bot(command_prefix='$')
dotenv.load()

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name, bot.user.id)
    print('------')

############################


@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(str(str(a) + ' + ' + str(b) + ' = ' + str(a + b)))

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(str(str(a) + ' * ' + str(b) + ' = ' + str(a * b)))

@bot.command()
async def greet(ctx):
    await ctx.send("Oh hello there.")

@bot.command()
async def rjomba(ctx):
    await ctx.send("https://media.discordapp.net/attachments/431980913090625566/551459591888830526/unknown.png")

@bot.command()
async def think(ctx):
    thinking = ['https://images.emojiterra.com/twitter/v11/512px/1f914.png', 'https://ih1.redbubble.net/image.414142526.5284/flat,800x800,070,f.u7.jpg',
             'https://media1.tenor.com/images/2a764d05a274d64389e905d062179da7/tenor.gif', 'https://i.kym-cdn.com/photos/images/original/001/256/183/9d5.png',
             'https://i.redd.it/qp5fmb9q7vg11.png', 'https://i.imgflip.com/v2ggn.jpg', 'https://media.tenor.com/images/b46349f4d4062ed96b94c3f82c1959f6/tenor.gif',
             'https://media1.tenor.com/images/ba9bb6157a5d1242a938c918d07456cd/tenor.gif?itemid=11253235', 'https://media1.tenor.com/images/046c5cfdfb264975a4ed2bb10f71d778/tenor.gif?itemid=5236580',
             'https://media1.tenor.com/images/37766d23c4c902aa19b44d39f120377e/tenor.gif?itemid=9951866', 'https://media1.tenor.com/images/c8e8d5069b7c0de27c7898ca7fd55ff9/tenor.gif?itemid=8387963']
    await ctx.send(thinking[randint(0, len(thinking))])

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Bot", description="Alexa", color=0xeee657)

    embed.add_field(name="Author", value="defolt_17#3701")

    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    embed.add_field(name="Group", value="№22")

    embed.add_field(name="GitHub", value="https://github.com/defolt17/Py-Discord-Bot-Alexa")

    await ctx.send(embed=embed)


###############################


@client.event
async def on_member_join(member):
    await client.send_message(member, 'Welcome to the club buddy.')



################################

bot.run(dotenv.get('BOT_TOKEN')) #Your '.env' file variable
