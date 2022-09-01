import os
import discord
import random
import chat
from discord.ext import commands
import asyncio
import cal
import functions

# import commands
# from keep_alive import keep_alive

# client = discord.Client()
client = commands.Bot(command_prefix='$')

cycle = dict(loop=True)


@client.command()
async def flip(ctx):
    flip = random.choice(["head", "tail"])
    await ctx.send(flip)


@client.command()
async def select(ctx, arg1, arg2, arg3, arg4):
    list = [arg1, arg2, arg3, arg4]
    select = random.choice(list)
    await ctx.send(select)


@client.command(pass_context=True)
async def user(ctx, user: discord.User):
    await ctx.send(user)


@client.command()
async def stop(ctx):
    cycle['loop'] = False


@client.command()
async def start(ctx):
    cycle['loop'] = True
    text = cal.cal()
    new_msg = await ctx.send(text)
    while cycle['loop']:
        new_con = cal.cal()
        await new_msg.edit(content=new_con)


@client.event
async def on_ready():
    print("I am ready as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)
    msg = message.content

    if any(word in msg.lower() for word in chat.qoute):
        qoute = functions.get_qoute()
        await message.channel.send(qoute)

    elif any(word in msg.lower() for word in chat.poem):
        poem = functions.get_poem()
        await message.channel.send(poem)

    elif any(word in msg.lower() for word in chat.meme):
        meme = functions.get_meme()
        await message.channel.send(meme)

    elif any(word in msg.lower() for word in chat.joke):
        joke = functions.get_jokes()
        await message.channel.send(joke)

    elif any(word in msg.lower() for word in chat.sad):
        hug = functions.get_hugs()
        await message.channel.send(hug)

    # elif any (word in msg.lower() for word in chat.price):
    #   val = functions.value()
    #   await message.channel.send(val)

    elif any(word in msg.lower() for word in chat.check):
        val = functions.get_data()
        await message.channel.send(val)

    elif any(word in msg.lower() for word in chat.greetings):
        await message.channel.send(random.choice(chat.bot_greets))

    elif any(word in msg.lower() for word in chat.insults):
        await message.channel.send(random.choice(chat.bot_insults))

    elif any(word in msg.lower() for word in chat.goodbyes):
        await message.channel.send(random.choice(chat.bot_byes))

    elif any(word in msg.lower() for word in chat.babies):
        await message.channel.send(random.choice(chat.bot_baby))

    elif any(word in msg.lower() for word in chat.smalltalks):
        await message.channel.send(random.choice(chat.bot_smalltalk))

    elif any(word in msg.lower() for word in chat.sarcastics):
        await message.channel.send(random.choice(chat.bot_sar))

    elif any(word in msg.lower() for word in chat.name):
        await message.channel.send(random.choice(chat.bot_name))

    elif any(word in msg.lower() for word in chat.time):
        await message.channel.send(random.choice(chat.bot_time))

    elif any(word in msg.lower() for word in chat.fav_movies):
        await message.channel.send(random.choice(chat.bot_fav_movies))

    elif any(word in msg.lower() for word in chat.love):
        await message.channel.send(random.choice(chat.bot_love))

    elif any(word in msg.lower() for word in chat.grandma):
        await message.channel.send(random.choice(chat.bot_grandma))

    elif any(word in msg.lower() for word in chat.sassy):
        await message.channel.send(random.choice(chat.bot_sassy))

    elif any(word in msg.lower() for word in chat.identity):
        await message.channel.send(random.choice(chat.bot_identity))

    elif any(word in msg.lower() for word in chat.exclamination):
        await message.channel.send(random.choice(chat.bot_exclaim))


# keep_alive()
client.run(os.environ['EvanToken'])
