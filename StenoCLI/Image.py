from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from pprint import pprint
from PIL import Image

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
            ],
        }
    ]

    while (True):
        answers = prompt(questions)
        if (len(answers['command']) != 0):
            break
        print('Please select an options!')

    command = answers['command'][0]

    if command == 'Encode':
        ImageEncode()
    elif command == 'Decode':
        ImageDecode()
    else:
        print("Wrong option")

def ImageEncode():
    q1 = [
        {
            'type': 'input',
            'qmark': '😎',
            'message': 'Enter name of file to be used as cover image (with extention):',
            'name': 'coverImage',
        },
    ]

    while True:
        answers = prompt(q1)
        if len(answers['coverImage']) != 0:
            try:
                img1 = Image.open(answers['coverImage'], 'r')
                break
            except FileNotFoundError:
                print('File not found:', answers['coverImage'])
        print('Try Again')

    q2 = [
        {
            'type': 'input',
            'qmark': '🧐',
            'message': 'Enter name of file to hide in cover image (with extention):',
            'name': 'secretImage',
        },
    ]

    while True:
        answers = prompt(q2)
        if len(answers['secretImage']) != 0:
            try:
                img2 = Image.open(answers['secretImage'], 'r')
                break
            except FileNotFoundError:
                print('File not found:', answers['secretImage'])
        print('Try Again')

    q3 = [
        {
            'type': 'input',
            'qmark': '🥱',
            'message': 'Enter resultant file name (with extention .png):',
            'name': 'encodedFile'
        },
    ]

    answers = prompt(q3)

    encodedFile = answers['encodedFile']

    try:
        resultImage = merge(img1, img2)
    except ValueError:
        print('Not encoding because user tried to hide higher resolution image in lower resolution image')
        return
    
    enArr = encodedFile.split(".")
    resultImage.save(encodedFile, str(enArr[-1].upper()))

def ImageDecode():
    questions = [
        {
            'type': 'input',
            'qmark': '🤑',
            'message': 'Enter file name of cover image to decoded (with extention):',
            'name': 'coverImage',
        },
    ]
    while (True):
        answers = prompt(questions)
        if (len(answers['coverImage']) != 0):
            break
        print('Please select an options!')

    coverImage = answers['coverImage']
    img1 = Image.open(coverImage, 'r')
    hiddenImage = unmerge(img1)
    hiddenImage.save("hiddenImage.png", "PNG")


def mergeRGB(rgb1, rgb2):
        r1, g1, b1 = rgb1
        r2, g2, b2 = rgb2
        rgb = (r1[:4] + r2[:4],
               g1[:4] + g2[:4],
               b1[:4] + b2[:4])
        return rgb

def merge(img1, img2):

        # Check the images dimensions
        if img2.size[0] > img1.size[0] or img2.size[1] > img1.size[1]:
            raise ValueError('Image 2 should not be larger than Image 1!')

        # Get the pixel map of the two images
        pixel_map1 = img1.load()
        pixel_map2 = img2.load()

        # Create a new image that will be outputted
        new_image = Image.new(img1.mode, img1.size)
        pixels_new = new_image.load()

        for i in range(img1.size[0]):
            for j in range(img1.size[1]):
                r, g, b = pixel_map1[i, j]
                rgb1 = ('{0:08b}'.format(r), '{0:08b}'.format(g), '{0:08b}'.format(b))

                # Use a black pixel as default
                r, g, b = (0, 0, 0)
                rgb2 = ('{0:08b}'.format(r), '{0:08b}'.format(g), '{0:08b}'.format(b))

                # Check if the pixel map position is valid for the second image
                if i < img2.size[0] and j < img2.size[1]:
                    r, g, b = pixel_map2[i, j]
                    rgb2 = ('{0:08b}'.format(r), '{0:08b}'.format(g), '{0:08b}'.format(b))

                # Merge the two pixels and convert it to a integer tuple
                rgb = mergeRGB(rgb1, rgb2)

                r, g, b = rgb
                pixels_new[i, j] = (int(r,2), int(g,2), int(b,2))
        
        return new_image

def unmerge(img):
        # Load the pixel map
        pixel_map = img.load()

        # Create the new image and load the pixel map
        new_image = Image.new(img.mode, img.size)
        pixels_new = new_image.load()

        # Tuple used to store the image original size
        original_size = img.size

        for i in range(img.size[0]):
            for j in range(img.size[1]):

                # Get the RGB (as a string tuple) from the current pixel
                r, g, b = pixel_map[i, j]
                r, g, b = ('{0:08b}'.format(r), '{0:08b}'.format(g), '{0:08b}'.format(b))

                # Extract the last 4 bits (corresponding to the hidden image)
                # Concatenate 4 zero bits because we are working with 8 bit
                rgb = (r[4:] + '0000',
                       g[4:] + '0000',
                       b[4:] + '0000')

                # Convert it to an integer tuple
                r, g, b = rgb
                pixels_new[i, j] = (int(r,2), int(g,2), int(b,2))

                # If this is a 'valid' position, store it
                # as the last valid position
                if pixels_new[i, j] != (0, 0, 0):
                    original_size = (i + 1, j + 1)

        # Crop the image based on the 'valid' pixels
        new_image = new_image.crop((0, 0, original_size[0], original_size[1]))

        return new_image
