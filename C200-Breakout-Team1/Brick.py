#a file to contain our brick class -LF
import pygame as py
import random as r

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
colors = [white, red, green, blue]
py.init()
class Brick:
    def __init__(self):
        pass

    def makeBrick(self, locCounterX, locCounterY, gameDisplay):
        py.draw.rect(gameDisplay, red, [locCounterX, locCounterY , 110, 30])
        py.draw.rect(gameDisplay, blue, [locCounterX, locCounterY , 110, 30])
        py.draw.rect(gameDisplay, green, [locCounterX, locCounterY , 110, 30])
        py.draw.rect(gameDisplay, white, [locCounterX, locCounterY , 110, 30])
  
#trying to figure out how to make each line of bricks change
    

 
