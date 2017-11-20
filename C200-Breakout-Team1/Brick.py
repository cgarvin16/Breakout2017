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
        py.draw.rect(gameDisplay, (255, 0, 0), [locCounterX, locCounterY , 100, 30])
  
#drawing the bricks and coordinates
    '''
    def drawBricks(self, gameDisplay):
        py.draw.rect(gameDisplay, red, [0,0,100,30])
        py.draw.rect(gameDisplay, red, [100,0,100,30])
        py.draw.rect(gameDisplay, red, [200,0,100,30])
        py.draw.rect(gameDisplay, red, [300,0,100,30])
        py.draw.rect(gameDisplay, red, [400,0,100,30])
        py.draw.rect(gameDisplay, red, [500,0,100,30])
        py.draw.rect(gameDisplay, red, [600,0,100,30])
        py.draw.rect(gameDisplay, green, [0,100,100,30])
    '''

    

 
