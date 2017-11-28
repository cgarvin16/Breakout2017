#a file to contain our brick class -LF
import pygame as py
import random as r


py.init()
class Brick:
    def __init__(self, locCounterX, locCounterY, gameDisplay, colors):
        self.brick = py.image.load(colors)
        self.rect = py.Rect(locCounterX, locCounterY, 110, 30)

    def makeBrick(self, locCounterX, locCounterY, gameDisplay, colors):
        return py.draw.rect(gameDisplay, colors, (locCounterX, locCounterY))

    def isBroken(self, ballRect, gameDisplay, locCounterX, locCounterY, brickRect):
        if ballRect.colliderect(brickRect):
            if self.brick != py.image.load("bkBrick.png"):
                return True
        else:
            return False

#brick = Brick()
#brick.makeBrick(100, 100, 30, "colors")
#print(brick.rect.x)
  
#trying to figure out how to make each line of bricks change
    

 
