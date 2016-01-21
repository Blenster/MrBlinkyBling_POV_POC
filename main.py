# Main program to read animation images and stream them to a POV system
# Intended for Battlebots Team Heartless
# Version 0.1 Alpha -- Rough draft for Proof of Concept
# Authors Ben Hibben/Blenster and Charles Lehman/The Hat
# Started: Jan 20 2016
# Last updated: Jan 20 2016 - Blenster

# libraries and dependencies
from PIL import Image

# variables
imageName = "test.jpg"

# constants
BLACK_THRESHOLD = 15  # The cutoff point where we decide not to light up the LEDs; anything below this is "off"

# objects
img = Image.open(imageName)  # temporary single image - TODO load a folder or ZIP file of images

# ****  primary code:  ****

# read in image(s);
# TODO Loop through ZIP or folder here

# read in the RGB values of the images into arrays
imgData = list(img.getdata())  # test code
# print imgData # note: works great but all in one line
for pixelData in imgData:
    print pixelData  # prints out each value on a separate line


# sort those arrays to render in a circle


# send rendering via SPI to the LEDs
