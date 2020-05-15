import ascii
import read
import os


import numpy as np

filename = "photos/photo.jpeg"
scale_percent = 11
image = None
image = read.read_photo(image, filename, scale_percent)


pixelBrightness = []
asciiCharacters = []
dictionary = {}

characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
gap = round(255 / len(characters))

ascii.createCharacterDictionary(gap, characters, dictionary)


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

while(1):
    cls()
    print("BASTIRMA SECENEGI: ")
    secenek = input()
    ascii.print_image(image, dictionary, secenek)
    print()
    print("PARLAKLIK TERSINE?")
    devam = input()
    if(devam == 'e') :
        cls()
        ascii.print_image(image, dictionary, secenek, devam)
        print()
        print("PROGRAMA DEVAM MI")
        devam = input()
        if (devam == 'e'):
            cls()
        else:
            cls()
            break
    else:
        print()
        print("PROGRAMA DEVAM MI")
        devam = input()
        if(devam == 'e') :
            cls()
        else:
            cls()
            break



