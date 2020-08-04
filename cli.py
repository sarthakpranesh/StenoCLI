from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from pprint import pprint

import photoStegano
import textStegano

print("\tWelcome to StenoCLI\n")

questions = [
    {
        'type': 'input',
        'name': 'name',
        'message': 'What is your name?',
    }
]

while(True):
    answers = prompt(questions)
    if (len(answers['name']) != 0):
        print("Hello ", answers['name'], "! ")
        break
    print("Please input your name!")

name = answers['name']

questions = [
    {
        'type': 'checkbox',
        'qmark': '🤔',
        'message': 'What do you wanna do ' + name + "?",
        'name': 'command',
        'choices': [
            {
                'name': 'Photo-steganography'
            },
            {
                'name': 'Text-steganography'
            },
            {
                'name': 'Exit'
            },
        ],
    }
]

while (True):
    answers = prompt(questions)
    if(len(answers['command']) != 0):
        print('Ready to perform ', answers['command'][0])
        break
    print("Please select at least one option!")

command = answers['command'][0]

if command == 'Photo-steganography':
    print('\tPhoto steganography\n')
    photoStegano.photoSteganography(name)
elif command == 'Text-steganography':
    print('Text steganography Ready')
    textStegano.textSteganography(name)
else:
    print('Exiting Program')
