def createCharacterDictionary(gap, characters, dictionary):
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

def print_image(image, dictionary, secenek, devam = 'h'):
    for x in range(image.shape[0]):
        print()
        for y in range(image.shape[1]):
            if (secenek == '1'):
                pixelBrightness = round((image[x, y, 0] + image[x, y, 1] + image[x, y, 2]) / 3)
            elif (secenek == '2'):
                pixelBrightness = round(((-0.21 * image[x, y, 0]) + (0.72 * image[x, y, 1]) + (0.07 * image[x, y, 2])) / 3)
            elif (secenek == '3'):
                pixelBrightness = round(((findMax(image[x, y, 0], image[x, y, 1], image[x, y, 2]) + findMin(
                    image[x, y, 0], image[x, y, 1], image[x, y, 2])) / 2))
            else: pixelBrightness = 0

            if(devam == 'e'):
                pixelBrightness -= 255
            if (pixelBrightness < 0): pixelBrightness *= -1
            if(pixelBrightness >= 256) : pixelBrightness-=255

            if (pixelBrightness % 4 == 0):
                print(dictionary['%d' % pixelBrightness], end='')
                print(dictionary['%d' % pixelBrightness], end='')
                print(dictionary['%d' % pixelBrightness], end='')

            elif (pixelBrightness % 4 == 1):
                print(dictionary['%d' % (pixelBrightness - 1)], end='')
                print(dictionary['%d' % (pixelBrightness - 1)], end='')
                print(dictionary['%d' % (pixelBrightness - 1)], end='')

            elif (pixelBrightness % 4 == 2):
                print(dictionary['%d' % (pixelBrightness - 2)], end='')
                print(dictionary['%d' % (pixelBrightness - 2)], end='')
                print(dictionary['%d' % (pixelBrightness - 2)], end='')

            elif (pixelBrightness % 4 == 3):
                print(dictionary['%d' % (pixelBrightness - 3)], end='')
                print(dictionary['%d' % (pixelBrightness - 3)], end='')
                print(dictionary['%d' % (pixelBrightness - 3)], end='')




