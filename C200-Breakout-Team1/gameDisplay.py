#                                    Breakout Beta Version 0.1
#                                    Milestone 1 Complete
#                                    Done By:
#                                           Logan Fields
#                                           Charles Brooks
#                                           Carolyn Garvin
#                                    For:
#                                        CSCI-C200 Fall 2017



#imports to allow use of other modules
from Wall import Wall
from Paddle import Paddle 
import pygame as py
import sys
import random as r 

#function to add scores to a scores text file for saving
def addScore():
    variable = open("highScores.txt", "a")
    name = input("Add 3 initials: ")
    score = 0
    variable.write("{0}. . . . .{1}\n".format(name, score))
    variable.close()

def resetBall():
    #randomizes initial location between bricks and paddle
    ballRect.x = r.randrange(10, 790) #width is 800, above 10 and bellow 790 so not on edge of screen
    ballRect.y = r.randrange(146, 610) #4 rows of bricks ending at 146px, paddle begin at 620px

    #variable to change ball direction; begins in random direction
    #tried using trig to calculate better angle options, but move() function only takes int
    global ballDirection
    ballDirection = [r.choice([2, -2]), r.choice([2, -2])]

def newGame():
    #holds initial level value
    global levelCount
    levelCount = 1

    wall = Wall()
    #builds wall of bricks
    wall.buildWall(gameDisplay, ballRect, ballDirection, levelCount)

    #creates new lists to avoid bugs
    global newBrickList
    global newRecList
    global newColorList
    global newHitList
    newBrickList = wall.brickList
    newRecList = wall.recList
    newColorList = wall.colorList
    newHitList = wall.hitList

    #resets intial life value
    lifeCount = 3

    resetBall()

    py.display.flip()


def levelTwo():
    wall = Wall()
    gameDisplay.fill((0,0,0))
    #builds wall of bricks
    global levelCount
    wall.buildWall(gameDisplay, ballRect, ballDirection, levelCount)

    #creates new lists to avoid bugs
    global newBrickList
    global newRecList
    global newColorList
    global newHitList
    newBrickList = wall.brickList
    newRecList = wall.recList
    newColorList = wall.colorList
    newHitList = wall.hitList

    resetBall()

    py.display.flip()
    global play
    play = True

play = True
#beginning of the required pygame skeleton
#initializes the pygame module
py.init()

#sets the game display size as 800px width and 700px height
gameDisplay = py.display.set_mode((800, 700))

#adds title to window top of game
py.display.set_caption("Breakout")

#updates the display
py.display.flip()

#creates ball image and gives it a rectangle to manipulate later
ball = py.image.load("ballNoBackground.png")
ballRect = ball.get_rect()

#sets initial ball direction and location
resetBall()

#wall = Wall()

#creates and places paddle with a rectangle
paddle = Paddle()
paddleRect = paddle.image.get_rect()
paddleRect.x = 300
paddleRect.y = 620

#allows for held down keys to continue movement
py.key.set_repeat(10, 10)

#holds initial life value
lifeCount = 3

#initialized ballDirection variable
ballDirection = [0,0]

#initialized level count
levelCount = 1

newBrickList = []
newRecList = []
newColorList = []
newHitList = []

while play:
    if levelCount == 1:
        newGame()
    elif levelCount == 2:
        levelTwo()
    
    while play:
        #code for the game
        #how to react to events like key presses or mouse movement
        for event in py.event.get():
            #exits game if you press close window
            if event.type == py.QUIT:
                sys.exit()
            #moves paddle based on left and right arrow keys
            elif py.key.get_pressed()[py.K_LEFT]:
                paddleRect.x -= 10
            elif py.key.get_pressed()[py.K_RIGHT]:
                paddleRect.x += 10
            elif py.key.get_pressed()[py.K_RETURN]:
                play = True
        

        #check if ball is at the top of the screen 
        if ballRect.y == 0: 
            #creates image object to be put to the screen 
            passMessage= py.image.load("editedLevelPassed.png")

            #paints over the previous screen
            gameDisplay.fill((0,0,0))
            gameDisplay.blit(passMessage, (100,100))

            #moves and pauses ball to prevent if loop from repeating
            ballRect.x = 300
            ballRect.y = 400
            ballDirection[0] = 0
            ballDirection[1] = 0

            #updates the screen
            py.display.flip()

            #pauses while loop to make image visible
            py.time.wait(3000)

            #adds one to the level indicator for use later
            levelCount += 1

            #prints level value to console for testing purposes
            print(levelCount)

            resetBall()

            if levelCount == 2: 
                levelTwo()
            #exits the game
            #quit()

        #check if ball is at bottom
        if ballRect.y > 700: 
            #creates image object to be put to the screen 
            failMessage= py.image.load("editedLevelFailed.png")
            gameDisplay.fill((0,0,0))
            gameDisplay.blit(failMessage, (100,100))

            #moves and pauses ball to prevent if loop from repeating
            ballRect.x = 300
            ballRect.y = 400
            ballDirection[0] = 0
            ballDirection[1] = 0

            #updates the screen
            py.display.flip()

            #pauses while loop to make image visible
            py.time.wait(3000)

            resetBall()
            #exits the game
            #quit()

        #if ball hits walls, send in opposite direction 
        if ballRect.x <= 0 or ballRect.x >= 800:
            ballDirection[0] = -ballDirection[0]
        

        
        #how ball reacting to paddle (paddle pixel ranges: -42 <- -21 = 21 -> 42)
        if ballRect.colliderect(paddleRect):
            ballDirection[1] = -ballDirection[1]

            #variable holds the x location of the differences between the centers of the ball and the paddle
            offset = ballRect.center[0] - paddleRect.center[0]

            #tried using trig to calculate better angle options, but move() function only takes int
            if offset >= 21: #right side of paddle, pos x and neg y, sends up to right 
                ballDirection[0] = 1
                ballDirection[1] = -1
            elif offset < 21 and offset > -21: #middle of paddle, sends up 
                ballDirection[0] = 0
                ballDirection[1] = -1
            elif offset <= -21: #left side of paddle, neg x and neg y, sends up to left 
                ballDirection[0] = -1
                ballDirection[1] = -1
       
        #using Clock object in pygame and setting frames per second
        clock = py.time.Clock()
        clock.tick(600000)

        #paints over last screen
        gameDisplay.fill((0,0,0))

         #checks level and changes things if needed
    
        
        #moves ball 
        ballRect = ballRect.move(ballDirection)

        #adds ball to screen 
        gameDisplay.blit(ball, ballRect)

        #adds paddle to screen
        gameDisplay.blit(paddle.image, paddleRect)

        #updates the remaining bricks to the screen and checks if a brick has been hit
        #if the brick has been hit, it removes it from the lists
        for i in range(len(newBrickList)):
            gameDisplay.blit(newBrickList[i], newRecList[i])
            if ballRect.colliderect(newRecList[i]):
                del(newBrickList[i])
                del(newRecList[i])
                del(newColorList[i])
                ballDirection[0] = -ballDirection[0] 
                ballDirection[1] = -ballDirection[1] 
             
                #updates screen
                py.display.flip()
 
                #ends loop
                break
        #updates screen
        py.display.flip()

    #exits python
    quit()