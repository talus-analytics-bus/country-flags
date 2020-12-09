from PIL import Image
import argparse
from time import sleep
import os

class bColors:
    CLEAR = "\033[0m"
    RED = "\033[31;1m"
    GREEN = "\033[32;1m"
    BLUE = "\033[34;1m"

def confirmImgBlowUp():
    contAnyway = input('Warning: the size you have selected for resizing is larger than your original image. Some loss of quality may occur.\nContinue anyway? Y/N:')
    if contAnyway.lower() == 'y':
        return True
    elif contAnyway.lower() == 'n':
        return False
    else: 
        print(bColors.RED + 'Invalid input, please try again.' + bColors.CLEAR)
        confirmImgBlowUp()

# RESIZE IMAGE SMALLER AND GENERATE 
# adapted from https://stackoverflow.com/questions/44231209/resize-rectangular-image-to-square-keeping-ratio-and-fill-background-with-black/44231784
def generate_square(img, new_size, fill_color=(0, 0, 0, 0)):
    ox, oy = img.size # get dimensions of original image

    # if resizing dimensions are larger than original image, shut down
    if new_size > ox and new_size > oy:
        print(bColors.RED + 'Fatal error: ' + bColors.CLEAR + 'The size you are trying to resize to (' + str(new_size) + 'px) is larger than your original images (1000px). Please try again with a smaller size.')
        print("Shutting down...")
        sleep(1)
        exit()
    
    img.thumbnail((new_size, new_size)) # resize image, while preserving aspect ratio
    x, y = img.size # get dimensions of resized image
    new_img = Image.new('RGBA', (new_size, new_size), fill_color) # create new (empty/transparent) square image of desired dimensions
    new_img.paste(img, (int((new_size - x) / 2), int((new_size - y) / 2))) # paste resized image into center of transparent square
    return new_img

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("size", help="number of pixels to resize images to (images will be square)", type=int)
    args = parser.parse_args()

    # grab all images in 1000px folder
    sourceDir = '../png1000px'

    # get resize dimensions from arg inputs
    size = args.size

    # create correct exports folder if it doesn't exist already
    if not os.path.exists('exports/' + str(size) + 'px'):
        os.makedirs('exports/' + str(size) + 'px')

    # iterate through images and resize them, saving to proper folder
    for file in os.listdir(sourceDir):
        img = Image.open(os.path.join(sourceDir, file))
        resized = generate_square(img, size)
        print('Resizing ' + file)
        resized.save('exports/' + str(size) + 'px/' + file)

    print('Images have been successfully resized and saved to /exports folder.')

