#import statements to allow access of other modules
import pygame as py

#initializes pygame module
py.init()

#beginning of the class used to create the brick object
#class is min. used at the moment but is being kept for planned changes in the future
class Brick:
    def __init__(self, locCounterX, locCounterY, gameDisplay, colors):
        self.image = py.image.load(colors)

