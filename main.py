import ascii
import load_photo
import os

filename = "photos/photo.jpeg"
scale_percent = 11
image = None
image = load_photo.load_photo(image, filename, scale_percent) #loading image and scaling


pixelBrightness = []
asciiCharacters = []
dictionary = {}

characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
gap = round(255 / len(characters))

ascii.createCharacterDictionary(gap, characters, dictionary) #mapping characters


def cls(): #clear cmd
    os.system('cls' if os.name=='nt' else 'clear')

while(1):
    cls()
    print("SELECT AN OPTION: ")
    option = input()
    ascii.print_image(image, dictionary, option)
    print()
    print("DO YOU WANT TO INVERSE BRIGHTNESS?")
    inverse_brightness = input()
    if(inverse_brightness == 'y') :
        cls()
        ascii.print_image(image, dictionary, option, inverse_brightness)
        print()
        print("DO YOU WANT TO CONTINUE?")
        will_it_continue = input()
        if (will_it_continue == 'y'):
            cls()
        else:
            cls()
            break
    else:
        print()
        print("DO YOU WANT TO CONTINUE?")
        will_it_continue = input()
        if(will_it_continue == 'y') :
            cls()
        else:
            cls()
            break



