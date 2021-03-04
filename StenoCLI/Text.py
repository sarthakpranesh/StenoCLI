from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from pprint import pprint
from PIL import Image

from StenoCLI.helpers import askAndLoadImage

def textSteganography():
    questions = [
        {
            'type': 'checkbox',
            'qmark': '🤭',
            'message': 'What operation would you like to perform?',
            'name': 'command',
            'choices': [
                {
                    'name': 'Encode'
                },
                {
                    'name': 'Decode'
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

    if (command == 'Encode'):
        textEncoding()
    elif (command == "Decode"):
        textDecoding()
    else:
        print("Wrong option")


def textEncoding():
    questions = [
        {
            'type': 'input',
            'qmark': '😎',
            'message': 'Enter file name to be used as cover image (with extention):',
            'name': 'coverImage',
        },
        {
            'type': 'input',
            'qmark': '🧐',
            'message': 'Enter secret message:',
            'name': 'secret',
        },
        {
            'type': 'input',
            'qmark': '🥱',
            'message': 'Enter encoded file name (with extention .png):',
            'name': 'encodedFile'
        }
    ]
    while (True):
        answers = prompt(questions)
        if (len(answers['coverImage']) != 0 and len(answers['secret']) != 0 and len(answers['encodedFile']) != 0):
            break
        print('Please select an options!')

    coverImage = answers['coverImage']
    secretText = answers['secret']
    encodedFile = answers['encodedFile']
    encode(coverImage, secretText, encodedFile)

def textDecoding():
    questions = [
        {
            'type': 'input',
            'qmark': '🤑',
            'message': 'Enter file name of image to decoded (with extention):',
            'name': 'coverImage',
        },
    ]
    while (True):
        answers = prompt(questions)
        if (len(answers['coverImage']) != 0):
            break
        print('Please select an options!')

    coverImage = answers['coverImage']
    secret = decode(coverImage)
    print("Secret Message: ", secret)


def genData(secretText):
        newBinaryText = []
 
        for i in secretText:
            newBinaryText.append(format(ord(i), '08b'))
        return newBinaryText


def modPix(pix, data):
 
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)
 
    for i in range(lendata):

        pix = [value for value in imdata.__next__()[:3] +
                                imdata.__next__()[:3] +
                                imdata.__next__()[:3]]
 
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1
 
            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
                
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
 
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1
 
        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)
 
    for pixel in modPix(newimg.getdata(), data):
 
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1


def encode(img, data, encodedFile):
    image = Image.open(img, 'r')
    if (len(data) == 0):
        raise ValueError('Data is empty')
    newimg = image.copy()
    encode_enc(newimg, data)
    newimg.save(encodedFile, str(encodedFile.split(".")[1].upper()))


def decode(img):
    image = Image.open(img, 'r')
 
    data = ''
    imgdata = iter(image.getdata())
 
    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]
 
        binstr = ''
 
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
 
        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data
