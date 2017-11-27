#a file to contain our brick class -LF
import pygame as py
import random as r


py.init()
class Brick:
    def __init__(self):
        pass

    def makeBrick(self, locCounterX, locCounterY, gameDisplay, colors):
        py.draw.rect(gameDisplay, colors, [locCounterX, locCounterY , 110, 30])
        brickRect = py.Rect(locCounterX, locCounterY, 110, 30)
        return brickRect


  
#trying to figure out how to make each line of bricks change
    

 
