from PyInquirer import prompt
from PIL import Image

def askAndLoadImage(qmark, message):   
    q1 = [  
        {
            'type': 'input',
            'qmark': qmark,
            'message': message,
            'name': 'image',
        },
    ]

    while True:
        answers = prompt(q1)
        if len(answers['image']) != 0:
            try:
                img1 = Image.open(answers['image'], 'r')
                break
            except FileNotFoundError:
                print('File not found:', answers['image'])
        print('Try Again')

    return img1