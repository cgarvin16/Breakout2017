#import statements to allow access of other modules
import pygame as py

#initializes pygame module
py.init()

#beginning of the class used to create the paddle object
#class is min. used at the moment but is being kept for planned changes in the future
class Paddle:
    def __init__(self):
        self.image = py.image.load("editedPaddleImage.png")