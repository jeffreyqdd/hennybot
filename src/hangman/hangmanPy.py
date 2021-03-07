#interface between the cpp file and the henny file

from subprocess import Popen, PIPE
import os
import sys

#print(os.path)
def interface_hangman(word, current_guess, guess_letter, num_wrong):
    path = os.path.dirname(os.path.relpath(__file__))
    #print(path)
    executable_loc = "./"+path+"/hangman"
    #print(executable_loc)
    
    p = Popen([executable_loc], shell=True, stdout=PIPE, stdin=PIPE)
    value = word + '\n' + current_guess + '\n' + guess_letter + '\n' + str(num_wrong) + '\n' + path + '\n'
    value = bytes(value, 'UTF-8')  # Needed in Python 3.

    p.stdin.write(value)
    p.stdin.flush()
    result = p.stdout.readline().strip().decode("utf-8").split(" ")


    return result

# test = {
#     'hangman' : {
#         'word' : "phil",
#         'current_guess' : "....",
#         'num_wrong' : 0
#     }
# }



stock_pics_hangman = [ ["   ________      ",
                "           |     ",
                "           |     ",
                "           |     ",
                "           |     ",
                "           |     ",
                "           |     ",
                "           |     ",
                "================="],

                ["   ________      ",
                 "  |        |     ",
                 " ['']      |     ",
                 "           |     ",
                 "           |     ",
                 "           |     ",
                 "           |     ",
                 "           |     ",
                 "================="],

                ["   ________      ",
                 "  |        |     ",
                 " ['']      |     ",
                 "  |        |     ",
                 "  |        |     ",
                 "  |        |     ",
                 "           |     ",
                 "           |     ",
                 "================="],

                ["   ________      ",
                 "  |        |     ",
                 " ['']      |     ",
                 "  |        |     ",
                 " /|        |     ",
                 "  |        |     ",
                 "           |     ",
                 "           |     ",
                 "================="],

                ["   ________      ",
                 "  |        |     ",
                 " ['']      |     ",
                 "  |        |     ",
                 " /|\       |     ",
                 "  |        |     ",
                 "           |     ",
                 "           |     ",
                 "================="],

                ["   ________      ",
                 "  |        |     ",
                 " ['']      |     ",
                 "  |        |     ",
                 " /|\       |     ",
                 "  |        |     ",
                 " /         |     ",
                 "/          |     ",
                 "================="],

                ["   ________      ",
                 "  |        |     ",
                 " ['']      |     ",
                 "  |        |     ",
                 " /|\       |     ",
                 "  |        |     ",
                 " / \       |     ",
                 "/   \      |     ",
                 "================="],

]

# def logic():
#     guess = 'm'

#     result = interface(word=test['hangman']['word'],
#               current_guess = test['hangman']['current_guess'],
#               guess_letter = guess,
#               num_wrong= 0,
#     )
#     ##['philosophy', '..........', '0', 'ongoing']
#     string = '\n'.join(stock_pics[int(result[2])]) + '\n'

#     test['hangman']['word'] = result[0]
#     test['hangman']['current_guess'] = result[1]


#     for i in range(len(test['hangman']['word'])):
#         string += "_ "
#     string += '\n'

#     print(string)


# logic()
#print(os.path.dirname(os.path.relpath(__file__)))
