# Main program to read animation images and stream them to a POV system
# Intended for Battlebots Team Heartless
# Version 0.3 Alpha -- Rough draft for Proof of Concept
# Authors Ben Hibben/Blenster and Charles Lehman/The Hat
# Started: Jan 20 2016
# Last updated: Jan 24 2016 - Blenster

# Notes:
# Assumes square images
# max data rate 4 Mbps
# Assumes two LED strips joined at the center

# libraries and dependencies
import os
from frame import Frame

# ***** variables *****

# Configuration variables
imageName = "test.jpg"  # Single image only; ignored when processing a folder
fileExtension = ".png"  # When processing a folder, what extension are we looking for? NOTE: keep the "." in there
                        # Ignores non-image files in the folder; when processing a single image this is ignored.
folderName = "test01/"  # folder name to search for images in
loadMode = "multi"  # single | multi
multiMode = "folder"  # folder | zip
NUMBER_OF_LEDS = 60  # The number of pixels/LEDs in each side (radius of the circle)
MIDDLE_OFFSET = 0  # The number of pixels in the center is effected by the gap in the middle; range 0 to 1 proportional

# TODO variables for Pi to micro-controller data exchange, etc. (resolution, GPIO to set HI/LOW - count, period)

# Program variables


# lists and dictionaries
multiImageList = []  # holds a list of lists; each list holds a list of pixel RGB tuples


# *****  primary code:  *****

# read in image(s) and store them in frame objects
if loadMode == "single":
    myImage = Frame(imageName, MIDDLE_OFFSET, NUMBER_OF_LEDS)  # load a single image
elif loadMode == "multi":
    if multiMode == "folder":
        print('Loading a folder of images')
        fileList = []
        for root, dirs, files in os.walk(folderName):
            for file in files:
                if file.endswith(fileExtension):
                    fileList.append(file)
        for myFile in fileList:
            multiImageList.append(Frame(folderName + myFile, MIDDLE_OFFSET, NUMBER_OF_LEDS))
    elif multiMode == "zip":
        print('Loading a zip file')
        # TODO finish this some day
    else:
        raise ValueError('Error: incorrect argument - "folder" or "zip" expected')
else:
    raise ValueError('Error: incorrect argument - "single" or "multi" expected')

# If we have image data we need to sort it and prepare to output it in a way that the POV display can use
# convert the cartesian coordinates to polar


# send rendering via SPI to the LEDs

# test code
print(repr(multiImageList[0].getData(43, 500)))

print('Done.')
