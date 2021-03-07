import sys
import os
from tqdm import tqdm

path_to_src = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


build_command = "/usr/bin/clang++ --std=c++17 -g {} -o {}"

path_to_cpp = [
    path_to_src + "/hangman/hangman.cpp"
]

path_to_executable = [
    path_to_src + "/hangman/hangman"
]

for i in tqdm(range(len(path_to_cpp))):
    os.system( build_command.format(path_to_cpp[i], path_to_executable[i]))

