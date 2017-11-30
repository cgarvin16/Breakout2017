#import statements to allow access of other modules
import pygame as py
from Brick import Brick

#initializes pygame module
py.init()

#sets image options to be used for bricks in a list to loop through
colors = ["wBrick.png", "rBrick.png", "gBrick.png", "bBrick.png"]

#beginning of the class used to creat the brick wall object
class Wall:
    def __init__(self):
        pass

    def buildWall(self, gameDisplay, ballRect, ballDirection):
        #creates empty list to hold variable for reference in the main game
        self.recList = []
        self.brickList = []
        self.colorList = []

        #base numbers for graph location of bricks
        locCounterY = 2
        counterColor = 0

        #creates four lines of bricks
        for i in range(0, 4):
            locCounterX = 2

            #creates seven bricks per line
            for i in range(0,7):
                self.brick = Brick(locCounterX, locCounterY, gameDisplay, colors[counterColor])
                self.brickList.append(self.brick.image)
                self.recList.append(py.Rect(locCounterX, locCounterY, 110, 30))
                self.colorList.append(counterColor)
                locCounterX += 114
            locCounterY += 35
            counterColor += 1
            

