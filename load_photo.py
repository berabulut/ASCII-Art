import cv2

def load_photo(image, filename, scale_percent):
    image = cv2.imread(filename)
    print("IMAGE LOADED SUCCESSFULLY")
    print("IMAGE SIZE : %d x %d " % (image.shape[0], image.shape[1]))

    h = int(image.shape[0] * scale_percent / 100)
    w = int(image.shape[1] * scale_percent / 100)
    dim = (w, h)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    print("Resized Image size : %d x %d " % (image.shape[0], image.shape[1]))
    print()
    return image

def scale_photo(image, dim):
    cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return image