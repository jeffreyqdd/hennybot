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

wait c++? Don't you have to build it? Yes...now assuming my jank python file management works, follow the instructions below. 

1. Navigate to src/credentials and read "read_this_file" and follow the instructions.
2. Navigate to src/base
3. Change c++ build command to whatever one you use
4. Run ```python setup.py```
5. Run ```python henny.py```
6. Brace for 100000 errors (may or may not happen)
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
we can use stdin and stdout as a means of providing input and reading output from the c++ executable. Separating arguments using newlines appears to work fine.
```
p = Popen([./executable], shell=True, stdout=PIPE, stdin=PIPE)
value = bytes("input value", 'UTF-8')
p.stdin.write(value)
p.stdin.flush()
result = p.stdout.readline().strip().decode("utf-8").split(" ")
```
Then in the c++ file, we can use cin and cout to communicate. THe only drawback is "value" has to have the same number of arguments every time to maintain simplicity. (cin >> x; will wait indefinitely if there is no input value)
```
#include <iostream>
using namespace std;

int main()
{
    int x,y,z;
    cin >> x >> y >> z;
    
    x*=2;
    y*=2;
    z*=3;

    cout << x << endl << y << endl << z <<endl;

    return 0;
}
```
^^didn't test the code above. no guarentees it compiles. (though it should).