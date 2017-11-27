#a file to contain our wall class -LF
#import statements to allow access of other modules
import pygame as py
from Brick import Brick
py.init()
#beginning of the class used to creat the brick wall object

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
colors = [white, red, green, blue]

class Wall:
    def __init__(self):
        pass

    def buildWall(self, gameDisplay):
        brickList = []
        locCounterY = 2
        counterColor = 0
        for i in range(0, 4):
            locCounterX = 2
            for i in range(0,7):
                brick = Brick()
                brickList.append(brick.makeBrick(locCounterX, locCounterY, gameDisplay,colors[counterColor]))
                locCounterX += 114
            locCounterY += 35
            counterColor += 1
    def brickList(self):
        return brickList

            

