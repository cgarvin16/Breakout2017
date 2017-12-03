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

    def buildWall(self, gameDisplay, ballRect, ballDirection, levelCount):
        #base numbers for graph location of bricks
        locCounterY = 2
        counterColor = 0

        if levelCount == 1:
            #creates empty list to hold variable for reference in the main game
            self.recList = []
            self.brickList = []
            self.colorList = []
            self.hitList = []

            #creates four lines of bricks
            for i in range(0, 4):
                locCounterX = 2
                lineCounter = i
                #creates seven bricks per line
                for i in range(0,7):
                    self.brick = Brick(locCounterX, locCounterY, gameDisplay, colors[counterColor])
                    self.brickList.append(self.brick.image)
                    self.recList.append(py.Rect(locCounterX, locCounterY, 110, 30))
                    self.colorList.append(counterColor)
                    #self.hitList.append(1)
                    if i == 1 or i == 3 or i == 6:
                        self.hitList.append(2)
                    else:
                        self.hitList.append(1)
                    locCounterX += 114
                locCounterY += 35
                counterColor += 1
        elif levelCount ==2:
            #creates empty list to hold variable for reference in the main game
            self.recList = []
            self.brickList = []
            self.colorList = []
            self.hitList = []

            #creates four lines of bricks
            for i in range(0, 4):
                locCounterX = 2

                #creates seven bricks per line
                for i in range(0,7):
                    self.brick = Brick(locCounterX, locCounterY, gameDisplay, colors[counterColor])
                    self.brickList.append(self.brick.image)
                    self.recList.append(py.Rect(locCounterX, locCounterY, 110, 30))
                    self.colorList.append(counterColor)
                    self.hitList.append(1)
                    locCounterX += 114
                locCounterY += 35
                counterColor += 1
        '''
        elif levelCount == 2:
             #creates empty list to hold variable for reference in the main game
            self.recList = []
            self.brickList = []
            self.colorList = []
            self.hitList = []

            #make some bricks require 2 hits to break
            for x in range(0, 4):
                locCounterX = 2
                for i in range(0,7):
                    self.brick = Brick(locCounterX, locCounterY, gameDisplay, colors[counterColor])
                    self.brickList.append(self.brick.image)
                    self.recList.append(py.Rect(locCounterX, locCounterY, 110, 30))
                    self.colorList.append(counterColor)

                    #sets the hit number of certain bricks in index to two
                    #at some point in the future, try to randomize these selections
                    #also changes which bricks are chosen to be two hit based on which line
                    
                    if i == 1 or i == 3 or i == 6:
                        self.hitList.append(2)
                    else:
                        self.hitList.append(1)
         
                    elif x == 1:
                        if i == 1 or i == 4:
                            self.hitList.append(2)
                        else:
                            self.hitList.append(1)
                    elif x == 2:
                        if i == 0 or i == 3 or i == 4:
                            self.hitList.append(2)
                        else:
                            self.hitList.append(1)
                    elif x == 3:
                        if i == 2 or i == 5 or i == 6:
                            self.hitList.append(2)
                        else:
                            self.hitList.append(1)
                            

        elif levelCount == 3:
            #inherit level 2 qualities plus add some unbreakable/iron bricks
            pass
        elif levelCount == 4:
            #inherit level 3 qualities, except all bricks require 2 hits and some require 3
            pass
        elif levelCount == 5:
            #inherit level 4 qualities, except add extra rows of bricks
            pass
               '''
