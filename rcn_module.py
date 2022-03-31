import sys
import random
from termcolor import colored, cprint
from sty import fg

def textRGB(text):
    def generateRGB():
        red = random.randint(0, 256)
        green = random.randint(0, 256)
        blue = random.randint(0, 256)
        return red, green, blue

    def generateCOLOR(red, green, blue):
        return fg(red, green, blue)

    red, green, blue = generateRGB()
    color = generateCOLOR(red, green, blue)
    print(color, text)

def textcolor(*t):
     for str_txt in t:
         str_t = str(str_txt)
         textcol(str_t)

def textstyle(*text, color = 'red'):
    for txt in text:
        txt = colored(txt, color, attrs=['reverse', 'blink'])
        print(txt, end=' ')


def textcol(*txt):
    for text in txt:
        col = random.randint(30, 38)
        t = '\033[1;' + str(col) + 'm' + text
        print(t, end=' ')
    print(end='\n')

def nameformat(nam):
    naam = ''
    name_list = nam.split()
    length_name = len(name_list)
    for i in range(length_name):
        if i == length_name-1:
            naam += name_list[i].upper()
        else:
            naam += name_list[i].title() + ' '

    return naam # return formated name and surname

def namecontrol(prompt, err):
    control = True
        # split name by word to check if it is valid
    while control:
        name = input(f"  {prompt} ==> ")
        name = nameformat(name)
        list_name = name.split()
      #  length = len(list_name)

        control = False
        for k in list_name: # check each characters if it is alphabet
            if not k.isalpha():
                control = True
        if control:
           print(err)

    return name

def numbercontrol(prompt, err):
    """
        this is some info on myfunc
        """
    state = False
    while not state:
        number = input(f"{prompt} ==> ")
        if number.isnumeric():
            state = True
        else:
            print(err)
            state = False
    return number

import string
def generate_password(ln):
    """ Generate random passwords, including letters, digits, and punctuation, with optional length"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(ln))
    return password
