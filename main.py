# Main program to read animation images and stream them to a POV system
# Intended for Battlebots Team Heartless
# Version 0.1 Alpha -- Rough draft for Proof of Concept
# Authors Ben Hibben/Blenster and Charles Lehman/The Hat
# Started: Jan 20 2016
# Last updated: Jan 23 2016 - Blenster

# Notes:
# Assumes square images
# max data rate 4 Mbps

# libraries and dependencies
from PIL import Image  # ImageSequence

# variables
imageName = "test.jpg"
directoryName = "test01/"  # folder name to search for images in
# loadMode = "single"  # single | multi
loadMode = "multi"  # single | multi
multiMode = "folder"  # folder | zip
# multiMode = "zip"  # folder | zip
# TODO variables for Pi to micro-controller data exchange, etc. (resolution, GPIO to set HI/LOW - count, period)

# lists and dictionaries
multiImageDict = {}  # holds a list of lists; each list holds a list of pixel RGB tuples
imageDataList = []  # holds a list of pixel RGB tuples

# constants
BLACK_THRESHOLD = 15  # The cutoff point where we decide not to light up the LEDs; anything below this is "off"
# ^^^^^^^^^^^^ This constant may not be used after all; battery conservation isn't too critical on this project

# objects
# img = Image.open(imageName)  #

# ****  primary code:  ****

# read in image(s)
if loadMode == "single":
    img = Image.open(imageName)  # load a single image
elif loadMode == "multi":
    if multiMode == "folder":
        print('Loading a folder of images')
        # for file in
    elif multiMode == "zip":
        print('Loading a zip file')
    else:
        print('Error: incorrect argument - "folder" or "zip" expected')
        quit()
else:
    print('Error: incorrect argument - "single" or "multi" expected')
    quit()

# If we have image data we need to sort it and prepare to output it in a way that the POV display can use
# convert the cartesian coordinates to polar


# read in the RGB values of the images into arrays
imgData = list(img.getdata())  # test code
# print imgData # note: works great but all in one line
for pixelData in imgData:
    print pixelData  # prints out each value on a separate line


# sort those arrays to render in a circle


# send rendering via SPI to the LEDs
