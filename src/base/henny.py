import discord
from discord.ext.commands import Bot
from discord.utils import get

from discord import Intents

import sys
import os
sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import datetime
import asyncio
import random
import yaml
import math

#import credentials
from credentials.credentials import TOKEN
#import IO handling
from fileIO.file import fetch_user_data, write_user_data, __read_data
#import hangman
from hangman.hangmanPy import interface_hangman, stock_pics_hangman


#initiate client
intents = Intents.all()
bot = Bot(intents=intents, command_prefix='-') # or whatever prefix you choose(!,%,?)

#commands
@bot.command(name = 'pray', help = 'Sends prayers to your savior')
async def pray(context):
    #updates streak
    data = fetch_user_data(context)

    emoji = get(bot.emojis, name='hennessey')

    if 'last-streak-day' not in data:
        data['last-streak-day'] = datetime.datetime.now()
    if 'streak' not in data:
        data['streak'] = 1

    last_pray = data['last-streak-day']
    time_now =  datetime.datetime.now()

    delta = time_now - last_pray
    delta_hours = delta.total_seconds() / 3600
    

    #do sentence stem
    if delta_hours >= 22 and delta_hours < 50:
        data['streak'] += 1
        data['last-streak-day'] = datetime.datetime.now()
        msg_stem = f"```Thanks for praying to me {data['streak']} times in a row. Your worship is much needed you peasant.```"

        await context.message.channel.send(msg_stem)
        await context.message.add_reaction(emoji=emoji)

        #give coins
        num_coins = random.randint(max(data['streak']-5, 0), min(data['streak'] + 5, 20))

        await context.message.channel.send(f"```Here are some coins: {num_coins} 🪙```")

        if 'coins' not in data:
            data['coins'] = num_coins
        else:
            data['coins'] += num_coins

    elif delta_hours < 22:
        msg_stem = f"```Thank you for your prayers :) (streak={data['streak']})```"
        data['last-streak-day'] = data['last-streak-day']
        data['streak'] = data['streak']
        
        await context.message.channel.send(msg_stem)
        await context.message.add_reaction(emoji=emoji)

    else:
        data['streak'] = 0
        msg_stem = f"```Wow. How dare you not pray to me. You lost your streak = {data['streak']}```"
        data['last-streak-day'] = datetime.datetime.now()

        await context.message.channel.send(msg_stem)
        await context.message.add_reaction(emoji=emoji)

    write_user_data(context, data)

@bot.command(name ='coins', help = 'Shows how many coins you have')
async def coins(context):
    data = fetch_user_data(context)
    if 'coins' not in data:
        data['coins'] = 0

    await context.message.channel.send(f"```you have: {data['coins']} 🪙```")

@bot.command(name = 'debug', help = 'Shows debug information (include: -self, -all)')
async def debug(context, *args):
    try:
        if args[0] == '-self':
            data = fetch_user_data(context)
            await context.message.channel.send("```"+yaml.dump(data)+"```")
        elif args[0] == '-all':
            data = __read_data()
            await context.message.channel.send("```"+yaml.dump(data)+"```")
        else: 
            await context.message.channel.send("```with '-self' or '-all' you big meme?```")
    except:
        await context.message.channel.send("```with '-self' or '-all' you big meme?```")

@bot.command(name = 'help-test', help = 'Ask henny for his blessing (include: testname)')
async def test(context, *args):
    data = fetch_user_data(context)

    try:
        test_name = ' '.join(args)

        if 'streak' not in data:
            data['streak'] = 0
        
        if data['streak'] <= 1:
            await context.message.channel.send("```You haven't been praying to me lately. I refuse to help.```")
            return

        response = [
            f"```Sorry, I'm lazy. Can't help you with {test_name}.```",
            f"```I gotta go grind league. Being top 10 is hard work.```",
            f"```I got banned from league for six weeks, but the grind doesn't stop on my alt!```",
            f"```Sorry, I'm teaching .....sanjay get on league...class.```",
            f"```Why should I help you if you didn't study? **blesses 19***```",
            f"```Hmmmm I'm feeling quite generous today. **blesses 69**```",
            f"```Alright stop asking me. **blesses 71**```",
            f"```The henny deems you worthy and blesses you with an 100 for {test_name}```"
        ]

        await context.message.channel.send(random.choice(response))
    except:
        await context.message.channel.send("with what test you big meme?")

@bot.command(name ='cube', help = "Cube henny is not real. He can't hurt you.")
async def cube(context):
    links = [
        'https://cdn.discordapp.com/attachments/752033664841547811/799511257131647006/Henny_Cube.gif',
        'https://cdn.discordapp.com/attachments/752033664841547811/799511767592075264/3dgifmaker26212.gif'
    ]
    await context.message.channel.send(random.choice(links))

@bot.command(name = 'magic8', help = "Ask my 8ball any question. (include: question). Costs 1🪙")
async def magic8(context, *args):
    if len(args) == 0:
        await context.message.channel.send("What question you pleb?")
    else:
        data = fetch_user_data(context)

        if 'coins' not in data:
            data['coins'] = 0

        if data['coins'] < 1:
            await context.message.channel.send("Dude, I don't respond to poor people.")
            return
        
        data['coins'] -= 1

        outcome = [ "It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
               "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
               "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
               "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don't count on it", "My reply is no", " My sources say no", "Outlook not so good", "Very Doubtful"]


        await context.message.channel.send("```hmmmm...```")
        await asyncio.sleep(random.randint(2,5))
        await context.message.channel.send("```" + random.choice(outcome) + "```")

        await asyncio.sleep(random.randint(2,3))
        await context.message.channel.send(f"```thank you for asking. You now have {data['coins']}🪙```")

        write_user_data(context, data)


#game 1 code
@bot.command(name = 'hangman', help = 'bet money by playing hangman (include: number or letter)')
async def test(context, *args):
    try:

        data = fetch_user_data(context)
        multiplier = 1.2

        def render_string(num_wrong, word):
            string = '\n'.join(stock_pics_hangman[num_wrong]) + '\n'
            for i in word:
                if(i == "."):
                    string += "_ "
                else:
                    string += i + " "
            string += '\n'
            return string


    
        #create data if it doesn't exist
        if 'hangman' not in data:
            data['hangman'] = { 
                'word' : ".",
                'current_guess' : ".",
                'num_wrong' : 0,
                'pay': 0,
            }
        
        if len(args) == 0:
            if data['hangman']['word'] == ".": 
                await context.message.channel.send(f"```To start a game, use '-hangman <coins to bet>' ```")
                return
            else:
                await context.message.channel.send(f"```You already have a game in progress, use '-hangman <letter guess>'...\n{render_string(data['hangman']['num_wrong'], data['hangman']['current_guess'])} ```")
                return

        #check if is new play
        if data['hangman']['word'] == ".":
            coin = int(args[0])
            await context.message.channel.send(f"```I will take {coin}🪙. If you win, I will reward you with {math.ceil(coin * multiplier)}🪙```")
            await asyncio.sleep(2)
            
            if 'coins' not in data:
                data['coins'] = 0
            
            if data['coins'] - coin < 0:
                await context.message.channel.send(f"```Hey! You're too poor. Come back when you have money```")
                return
            data['coins'] -= coin
            data['hangman']['pay'] = math.ceil(coin * multiplier)
                
            
            await context.message.channel.send(f"```Thinking....```")
            await asyncio.sleep(2)


            #communicate with interface to get new word
            #['philosophy', '..........', '0', 'ongoing']
            result = interface_hangman(
                word=data['hangman']['word'],
                current_guess = data['hangman']['current_guess'],
                guess_letter = '.',
                num_wrong= 0
            )

            #update
            data['hangman']['word'] = result[0]
            data['hangman']['current_guess'] = result[1]
            data['hangman']['num_wrong'] = int(result[2])
            #display
            await context.message.channel.send(f"```{render_string(data['hangman']['num_wrong'], data['hangman']['current_guess'])}```")

            write_user_data(context, data)


        #play
        else:
            #communciate with interface
            guess = args[0]
            #['philosophy', '..........', '0', 'ongoing']
            result = interface_hangman(
                word=data['hangman']['word'],
                current_guess = data['hangman']['current_guess'],
                guess_letter = guess,
                num_wrong= data['hangman']['num_wrong']
            )

            #update
            data['hangman']['word'] = result[0]
            data['hangman']['current_guess'] = result[1]
            data['hangman']['num_wrong'] = int(result[2])
            #display
            await context.message.channel.send(f"```{render_string(data['hangman']['num_wrong'], data['hangman']['current_guess'])}```")

            outcome = result[3]

            if outcome == "loss":
                await context.message.channel.send(f"```Oops you suck.```")
                data['hangman']['word'] = "."
            elif outcome == "win":
                data['hangman']['word'] = "."
                data['coins'] += data['hangman']['pay']

                await context.message.channel.send(f"```Gj. +{data['hangman']['pay']}🪙```")
            
            write_user_data(context, data)

    except:
        await context.message.channel.send(f"```dude...tf is wrong with you```")






        




#start client
bot.run(TOKEN)