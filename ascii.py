import numpy as np
np.seterr(over='ignore')

def createCharacterDictionary(gap, characters, dictionary): #map characters
    for i in range(len(characters)):
        if i == len(characters) - 1:
            dictionary.update({'%d' % ((gap * i) - 1): characters[i]})
            break
        dictionary.update({'%d' %(gap * i) : characters[i]})

def findMax(i, j, k):
    list = [i, j, k]
    return max(list)
def findMin(i, j, k):
    list = [i, j, k]
    return min(list)

def print_as_requested(n, var):
    for x in range(n):
        print(var, end = '')

def print_image(image, dictionary, option, inverse_brightness = 'n'):
    for x in range(image.shape[0]): #height
        print()
        for y in range(image.shape[1]): #width
            if (option == '1'):
                pixelBrightness = round((image[x, y, 0] + image[x, y, 1] + image[x, y, 2]) / 3)
            elif (option == '2'):
                pixelBrightness = round(((-0.21 * image[x, y, 0]) + (0.72 * image[x, y, 1]) + (0.07 * image[x, y, 2])) / 3)
            elif (option == '3'):
                pixelBrightness = round(((findMax(image[x, y, 0], image[x, y, 1], image[x, y, 2]) + findMin(
                    image[x, y, 0], image[x, y, 1], image[x, y, 2])) / 2))
            else: pixelBrightness = round(((-0.21 * image[x, y, 0]) + (0.72 * image[x, y, 1]) + (0.07 * image[x, y, 2])) / 3) #if user input is invalid we will use the formula works best

            if(inverse_brightness == 'y'):
                pixelBrightness -= 255
            if (pixelBrightness < 0): pixelBrightness *= -1
            if(pixelBrightness >= 256) : pixelBrightness-=255

            if (pixelBrightness % 4 == 0):
                print_as_requested(4, dictionary['%d' % pixelBrightness])
            elif (pixelBrightness % 4 == 1):
                print_as_requested(4, dictionary['%d' % (pixelBrightness - 1)])
            elif (pixelBrightness % 4 == 2):
                print_as_requested(4, dictionary['%d' % (pixelBrightness - 2)])
            elif (pixelBrightness % 4 == 3):
                print_as_requested(4, dictionary['%d' % (pixelBrightness - 3)])





