# Class to load and process animation images
# Intended for Battlebots Team Heartless
# Version 0.1 Alpha -- Rough draft for Proof of Concept
# Authors Ben Hibben/Blenster and Charles Lehman/The Hat
# Started: Jan 24 2016
# Last updated: Jan 24 2016 - Blenster

# Notes:
# Assumes square images
# Assumes POV with two LED strips rather than a single LED strip

# libraries and dependencies
from PIL import Image
import math

class Frame(object):
    """Class to hold animation frame data cached as an object. Frames have the
    following properties:

    Attributes:
        image: A String pointing to an image to be loaded.
        imageBufferData: A List of RGB tuples for each pixel in the image.
        size: An Integer showing the size of the square (all frames will be made square).
        middleOffset: A Float of the middle offset amount (space in the center of the POV strips)
        numOfLEDs: An Integer representing the total number of LEDs
    """

    def __init__(self, imageFile, middleOffset, numOfLEDs):
        """
        Returns a frame object that holds all the cached data and attributes we need for the POV.
        """
        # Load the image:
        self.image = Image.open(imageFile)

        # Grab the pixel data object:
        self.imgData = list(self.image.getdata())

        # Pass along the arguments to the class variables
        self.middleOffset = middleOffset # Offset for the center gap between the LED strips; should be small (0-1)
        self.numOfLEDs = numOfLEDs # The number of LEDs in our POV strands (both combined)

        # Setup some more class variables
        self.imageBufferData = []  # Holds a list of pixel RGB tuples for a single image
        self.size = min(self.image.size)  # The shortest size of the square image data we are working with (width, height)

        # Setup scaling variables based on image size
        self.mPrime = (self.middleOffset * self.size) / 2
        self.pitch = ((1 - self.middleOffset) * self.size) / (2 * self.numOfLEDs)

        # Loop through the pixel data and push it into the cache
        for pixelData in self.imgData:
            self.imageBufferData.append(pixelData)

        # Create cache of pixel data mapped to polar coordinates
        self.cacheMaxPosition = 2 * math.pi * self.numOfLEDs
        self.cache = []  # Cache of transformed pixel data to send to LEDs
        center = self.size / 2.0  # Calculate the center of the square
        anglePitch = 2 * math.pi / self.cacheMaxPosition
        for i in xrange(int(self.cacheMaxPosition)):
            theta = i * anglePitch  # / float(self.numOfLEDs)
            s = math.sin(theta)
            c = math.cos(theta)
            cacheLine = []
            for j in xrange(self.numOfLEDs):
                x = center + (((j * self.pitch) + self.mPrime) * c)
                y = center + (((j * self.pitch) + self.mPrime) * s)
                cacheLine.append(tuple(self.imageBufferData[(int(self.size) * int(y)) + int(x)][:3]))
            for j in xrange(self.numOfLEDs):
                x = center - (((j * self.pitch) + self.mPrime) * c)  # NOTE: if image is backwards; change the +/- after center
                y = center - (((j * self.pitch) + self.mPrime) * s)
                cacheLine.append(tuple(self.imageBufferData[(int(self.size) * int(y)) + int(x)][:3]))
            self.cache.append(cacheLine)

    # ***** Properties ******

    def getImageBuffer(self):
        """
        :return: Returns the cache of image pixel RGB tuples.
        """
        return self.imageBufferData

    def getSize(self):
        """
        :return: Returns the size of the image square.
        """
        return self.size

    def getData(self, count, period):
        """
        Returns the data to send to the POV based on the count and period data from the microcontroller
        :param count:
        :param period:
        :return:
        """
        return self.cache[int(count * self.cacheMaxPosition / period)]

