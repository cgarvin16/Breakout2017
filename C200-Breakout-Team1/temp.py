#import statements to allow access of other modules
import pygame as py
from Brick import Brick

#initializes pygame module
py.init()

#sets image options to be used for bricks in a list to loop through
colors = ["wBrick.png", "rBrick.png", "gBrick.png", "bBrick.png", "mBrick.png", "zBrick.png"]
iron = "ironBrick.png"
#powerup images
heartPU = py.image.load("drop_heart_icon.png")
paddlePU = py.image.load("largePaddleImage.png")

#beginning of the class used to creat the brick wall object
class Wall():
    def __init__(self):
        pass

    def buildWall(self, gameDisplay, ballRect, ballDirection, levelCount):
        #base numbers for graph location of bricks
        locCounterY = 42
        counterColor = 0

        if levelCount == 1:
            #creates empty list to hold variable for reference in the main game
            self.recList = []
            self.brickList = []
            self.colorList = []
            self.hitList = []
            self.powerList = []

            #creates four lines of bricks
            for i in range(0, 4):
                locCounterX = 2
                lineCounter = i
                #creates seven bricks per line
                for i in range(0,7):
                    self.brick = Brick(locCounterX, locCounterY, gameDisplay, colors[counterColor])
                    self.brickList.append(self.brick.image)
                    self.recList.append(py.Rect(locCounterX, locCounterY, 110, 30))
                    self.colorList.append(colors[counterColor])
                    self.hitList.append(1)
                    self.powerList.append("none")
                    locCounterX += 114
                locCounterY += 35
                counterColor += 1
        elif levelCount ==2:
            #creates empty list to hold variable for reference in the main game
            self.recList = []
            self.brickList = []
            self.colorList = []
            self.hitList = []
            self.powerList = []
            lineCounter = 0

            #creates four lines of bricks
            for i in range(0, 4):
                locCounterX = 2
                #creates seven bricks per line
                for i in range(0,7):
                    self.brick = Brick(locCounterX, locCounterY, gameDisplay, colors[counterColor])
                    self.brickList.append(self.brick.image)
                    self.recList.append(py.Rect(locCounterX, locCounterY, 110, 30))
                    self.colorList.append(colors[counterColor])
                    self.powerList.append("none")
                    if lineCounter == 0:
                        if i == 1 or i == 3 or i == 6:
                            self.hitList.append(2)
                        else:
                            self.hitList.append(1)
                    elif lineCounter == 1:
                        if i == 1 or i == 4:
                            self.hitList.append(2)
                        else:
                            self.hitList.append(1)
                    elif lineCounter == 2:
                        if i == 0 or i == 3 or i == 4:
                            self.hitList.append(2)
                        else:
                            self.hitList.append(1)
                    elif lineCounter == 3:
                        if i == 2 or i == 5 or i == 6:
                            self.hitList.append(2)
                        else:
                            self.hitList.append(1)
                            
                    locCounterX += 114
                locCounterY += 35
                counterColor += 1
                lineCounter += 1
        elif levelCount == 3:
            #creates empty list to hold variable for reference in the main game
            self.recList = []
            self.brickList = []
            self.colorList = []
            self.hitList = []
            self.powerList = []

            lineCounter = 0
            #creates four lines of bricks
            for i in range(0, 4):
                locCounterX = 2
                #creates seven bricks per line
                for i in range(0,7):
                    if lineCounter == 0 and i == 0:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, iron)
                    elif lineCounter == 1 and i == 5:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, iron)
                    elif lineCounter == 2 and i == 1:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, iron)
                    elif lineCounter == 3 and i == 6:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, iron)
                    else:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, colors[counterColor])
                    self.brickList.append(self.brick.image)
                    self.recList.append(py.Rect(locCounterX, locCounterY, 110, 30))
                    self.colorList.append(colors[counterColor])
                    if lineCounter == 0:
                        if i == 1 or i == 3 or i == 6:
                            self.hitList.append(2)
                            #powerups:
                            self.powerList.append(1)
                        elif i == 0:
                            self.hitList.append(0)
                        else:
                            self.hitList.append(1)
                        if i == 2:
                            self.powerList.append("heartPU")
                        else:
                            self.powerList.append("none")
                    elif lineCounter == 1:
                        if i == 1 or i == 4:
                            self.hitList.append(2)
                        elif i == 5:
                            self.hitList.append(0)
                        else:
                            self.hitList.append(1)
                        if i == 3:
                            self.powerList.append("paddlePU")
                        else:
                            self.powerList.append("none")
                    elif lineCounter == 2:
                        if i == 0 or i == 3 or i == 4:
                            self.hitList.append(2)
                        elif i == 1:
                            self.hitList.append(0)
                        else:
                            self.hitList.append(1)
                    if i == 6:
                            self.powerList.append("paddlePU")
                        else:
                            self.powerList.append("none")
                    elif lineCounter == 3:
                        if i == 2 or i == 5:
                            self.hitList.append(2)
                        elif i == 6:
                            self.hitList.append(0)
                        else:
                            self.hitList.append(1)
                       if i == 0:
                           self.powerList.append("heartPU")
                        else: 
                            self.powerList.append("none")
                    locCounterX += 114
                locCounterY += 35
                counterColor += 1
                lineCounter += 1
        elif levelCount == 4: #level 4 has all 2 hit bricks, some 3 hit bricks, and some iron bricks
            #creates empty list to hold variable for reference in the main game
            self.recList = []
            self.brickList = []
            self.colorList = []
            self.hitList = []
            #powerup lists
            self.powerList = []

            lineCounter = 0
            #creates four lines of bricks
            for i in range(0, 4):
                locCounterX = 2
                #creates seven bricks per line
                for i in range(0,7):
                    if lineCounter == 0 and i == 2:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, iron, heartPU, paddlePU)
                    elif lineCounter == 1 and i == 4:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, iron, heartPU, paddlePU)
                    elif lineCounter == 2 and i == 6:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, iron, heartPU, paddlePU)
                    elif lineCounter == 3 and i == 4:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, iron, heartPU, paddlePU)
                    else:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, colors[counterColor])
                    self.brickList.append(self.brick.image)
                    self.recList.append(py.Rect(locCounterX, locCounterY, 110, 30))
                    self.colorList.append(colors[counterColor])
                    if lineCounter == 0:
                        if i == 3 or i == 0 or i == 4:
                            self.hitList.append(3)
                            #powerups:
                            self.powerList.append(3)
                        elif i == 2:
                            self.hitList.append(0)
                            #powerups:
                            self.powerList.append(3)
                        else:
                            self.hitList.append(2)

                    elif lineCounter == 1:
                        if i == 2 or i == 6:
                            self.hitList.append(3)
                            #powerups:
                            self.powerList.append(3)
                        elif i == 4:
                            self.hitList.append(0)
                            #powerups:
                            self.powerList.append(3)
                        else:
                            self.hitList.append(2)
                    elif lineCounter == 2:
                        if i == 5 or i == 2 or i == 0:
                            self.hitList.append(3)
                            #powerups:
                            self.powerList.append(3)
                        elif i == 6:
                            self.hitList.append(0)
                            #powerups:
                            self.powerList.append(3)
                        else:
                            self.hitList.append(1)
                    elif lineCounter == 3:
                        if i == 1 or i == 3:
                            self.hitList.append(3)
                            #powerups:
                            self.powerList.append(3)
                        elif i == 4:
                            self.hitList.append(0)
                            #powerups:
                            self.powerList.append(3)
                        else:
                            self.hitList.append(2)
                            
                    locCounterX += 114
                locCounterY += 35
                counterColor += 1
                lineCounter += 1
        elif levelCount == 5: #level 5 has all two hit brick, some three hit bricks, some iron, and two extra rows
            #creates empty list to hold variable for reference in the main game
            self.recList = []
            self.brickList = []
            self.colorList = []
            self.hitList = []
            #powerup lists
            self.powerList = []

            lineCounter = 0
            #creates 6 lines of bricks
            for i in range(0, 6):
                locCounterX = 2
                #creates seven bricks per line
                for i in range(0,7):
                    if lineCounter == 0 and i == 2:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, iron, heartPU, paddlePU)
                    elif lineCounter == 1 and i == 1:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, iron, heartPU, paddlePU)
                    elif lineCounter == 2 and i == 6:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, iron, heartPU, paddlePU)
                    elif lineCounter == 3 and i == 4:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, iron, heartPU, paddlePU)
                    elif lineCounter == 4 and i == 0:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, iron, heartPU, paddlePU)
                    elif lineCounter == 5 and i == 5:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, iron, heartPU, paddlePU)
                    else:
                        self.brick = Brick(locCounterX, locCounterY, gameDisplay, colors[counterColor])
                    self.brickList.append(self.brick.image)
                    self.recList.append(py.Rect(locCounterX, locCounterY, 110, 30))
                    self.colorList.append(colors[counterColor])
                    if lineCounter == 0:
                        if i == 3 or i == 0 or i == 4:
                            self.hitList.append(3)
                            #powerups:
                            self.powerList.append(3)
                        elif i == 2:
                            self.hitList.append(0)
                            #powerups:
                            self.powerList.append(3)
                        else:
                            self.hitList.append(2)
                    elif lineCounter == 1:
                        if i == 2 or i == 6:
                            self.hitList.append(3)
                            #powerups:
                            self.powerList.append(3)
                        elif i == 1:
                            self.hitList.append(0)
                            #powerups:
                            self.powerList.append(3)
                        else:
                            self.hitList.append(2)
                    elif lineCounter == 2:
                        if i == 5 or i == 2 or i == 0:
                            self.hitList.append(3)
                            #powerups:
                            self.powerList.append(3)
                        elif i == 6:
                            self.hitList.append(0)
                            #powerups:
                            self.powerList.append(3)
                        else:
                            self.hitList.append(2)
                    elif lineCounter == 3:
                        if i == 1 or i == 3:
                            self.hitList.append(3)
                            #powerups:
                            self.powerList.append(3)
                        elif i == 4:
                            self.hitList.append(0)
                            #powerups:
                            self.powerList.append(3)
                        else:
                            self.hitList.append(2)
                    elif lineCounter == 4:
                        if i == 2 or i == 6:
                            self.hitList.append(3)
                            #powerups:
                            self.powerList.append(3)
                        elif i == 0:
                            self.hitList.append(0)
                            #powerups:
                            self.powerList.append(3)
                        else:
                            self.hitList.append(2)
                    elif lineCounter == 5:
                        if i == 1 or i == 4 or i == 2:
                            self.hitList.append(3)
                            #powerups:
                            self.powerList.append(3)
                        elif i == 5:
                            self.hitList.append(0)
                            #powerups:
                            self.powerList.append(3)
                        else: 
                            self.hitList.append(2)
                    locCounterX += 114
                locCounterY += 35
                counterColor += 1
                lineCounter += 1