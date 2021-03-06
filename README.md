# Henny Bot

## What is henny bot? 
A million questions might be running through your head right now – what is henny bot? can henny bot be my salvation? Just remember, those questions that you just asked are wrong. You should be asking: what can YOU do for henny bot?

Henny bot is just a side-project I created to add a little more fun into my friend's discord server. He can play games, converse with your lonely self, and show you the right way (not just the way). Don't forget to pray to him, or you risk not finding the way.

You assume all risks using henny bot. I'm not responsible if he shows up in the middle of the night holding a physics c worksheet. You forgot to pray and worship him. Your fault entirely. 



## How do I use henny bot?
### A. Setting up the environment
The setup is rather painful. Why? Because I wrote it for myself...it's not intended for public release. By using it, you have to set it up yourself. (sorry).

*You'll have to setup your own python environment*
*There are c++ files that probably need to be re-compiled*

Why c++ in python? Are you insane? why not cython? C++ is fast, and can perform search operations for games like tic tac toe much faster. Cython is another can of worms I refuse to open for this project (I need to learn it first).

1. Navigate to src/credentials and read "read_this_file" and follow the instructions.
2. Navigate to src/base.
3. TODO: not needed – cython compile
4. Run ```python henny.py```
5. Worship henny or he will come for you.



_To make setup even less painful...a docker setup will come in the future(hopefully)_

Note to self: to create an env, use: 
```python3 -m venv env```

### B. Using Henny Bot
Just use that 200 iq big brain of yours. Once henny bot is added to the server, just use the command ```-help```.

## Notes to self:
### A) commands 
The code below sets the command prefix to '-'. I chose '-' because it is easy to type and should avoid clashes with the more common '!', '$', or '?'

```
bot = Bot(intents=intents, command_prefix='-')
```

The code below creates a command that the bot will respond to. To call it, it should be command_prefix + name, or '-pray'. '-help' is implicitly defined. Calling it will send a message containing the command + text under help.


Link to what context is: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Context

*args should contain the text after the command.

```
@bot.command(name = 'pray', help = 'brief explanation')
async def pray(context, *args):
```

### B) C++ + Python
How to communicate with c++? 

TODO

