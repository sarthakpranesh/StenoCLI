from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from pprint import pprint

def photoSteganography():
    questions = [
        {
            'type': 'checkbox',
            'qmark': '🤔',
            'message': 'What operation would you like to perform on Image?',
            'name': 'command',
            'choices': [
                {
                    'name': 'Encode'
                },
                {
                    'name': 'Decode'
                },
                {
                    'name': 'Back'
                },
            ],
        }
    ]

    while (True):
        answers = prompt(questions)
        if (len(answers['command']) != 0):
            break
        print('Please select an options!')

    command = answers['command'][0]

    pprint(command)

