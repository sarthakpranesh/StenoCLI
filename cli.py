from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from pprint import pprint

import photoStegano
import textStegano

questions = [
    {
        'type': 'checkbox',
        'qmark': '🤔',
        'message': 'What do you wanna do ?',
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

def StartCLI():
    while (True):
        answers = prompt(questions)
        if(len(answers['command']) != 0):
            print('Ready to perform ', answers['command'][0])
            break
        print("Please select at least one option!")

    command = answers['command'][0]

    if command == 'Photo-steganography':
        photoStegano.photoSteganography()
    elif command == 'Text-steganography':
        textStegano.textSteganography()
    else:
        print('Exiting Program')
        
