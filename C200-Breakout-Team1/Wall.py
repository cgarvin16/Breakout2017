#a file to contain our wall class -LF
#import statements to allow access of other modules
import pygame as py
from Brick import Brick
py.init()
#beginning of the class used to creat the brick wall object
class Wall:
    def __init__(self):
        pass

    def buildWall(self, gameDisplay):
        locCounterY = 2
        for i in range(0, 3):
            locCounterX = 2
            for i in range(0,7):
                brick = Brick()
                brick.makeBrick(locCounterX, locCounterY, gameDisplay)
                locCounterX += 103
            locCounterY += 32
            

