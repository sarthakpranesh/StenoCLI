from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from pprint import pprint

from StenoCLI.Image import photoSteganography
from StenoCLI.Text import textSteganography

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

def main():
    while (True):
        answers = prompt(questions)
        if(len(answers['command']) != 0):
            print('Ready to perform ', answers['command'][0])
            break
        print("Please select at least one option!")

    command = answers['command'][0]

    if command == 'Photo-steganography':
        photoSteganography()
    elif command == 'Text-steganography':
        textSteganography()
    else:
        print('Exiting Program')

if __name__ == "__main__":
    main()
        
