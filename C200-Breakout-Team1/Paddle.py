#a file to contain our paddle class -LF
#import statements to allow access of other modules
import pygame as py
from Ball import Ball
py.init()
#beginning of the class used to create the paddle object
class Paddle:
    def __init__(self):
        self.image = py.image.load("editedPaddleImage.png")
        
    def buildPaddle(self):
        #self.image.rect = self.image.build_rect()
        #return self.image.rect
        pass