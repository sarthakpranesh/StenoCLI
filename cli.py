from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, Separator
from pprint import pprint

questions = [
    {
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Select Command',
        'name': 'command',
        'choices': [
            {
                'name': 'Photo Stenography'
            },
            {
                'name': 'Text Stenography'
            },
            {
                'name': 'Exit'
            },
        ],
        'validate': lambda answer: 'Choose one command to proceed!' \
            if len(answer) == 0 else True
    }
]

answers = prompt(questions)
pprint(answers)
