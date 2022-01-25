from cgi import print_environ
import random
from traceback import print_tb

# letters symbols and numbers
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z', 'w', 'y', 'k']
symbols = ['#', '%', '*']

# list_pass length handler
pass_length = int(input("enter list_pass length: "))

passwords = []


# random number handler
def random_nums():
    return random.choice(num)

# # random letters handler


def random_letters():
    return random.choice(letter)


# # random symbols handler
def random_symbols():
    return random.choice(symbols)


def shuffle_array():
    pass_list = random_nums() + random_letters() + random_symbols()

    return pass_list


for i in range(pass_length):
    shuffled_pass = random.choice(shuffle_array())

    passwords.append(shuffled_pass)

curr_pass = ""

for i in passwords:
    curr_pass += i

with open('pass.txt', 'w') as f:
    f.write(f"your password: {curr_pass}")
