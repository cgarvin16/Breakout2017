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

#randomizes initial location between bricks and paddle
ballRect.x = r.randrange(10, 790) #width is 800, above 10 and bellow 790 so not on edge of screen
ballRect.y = r.randrange(146, 610) #4 rows of bricks ending at 146px, paddle begin at 620px

#variable to change ball direction; begins in random direction
#tried using trig to calculate better angle options, but move() function only takes int
ballDirection = [r.choice([1, -1]), r.choice([1, -1])]

#creates wall object
wall = Wall()

#builds wall of bricks
wall.buildWall(gameDisplay, ballRect, ballDirection)

#creates new lists to avoid bugs
newBrickList = wall.brickList
newRecList = wall.recList
newColorList = wall.colorList

#creates and places paddle with a rectangle
paddle = Paddle()
paddleRect = paddle.image.get_rect()
paddleRect.x = 300
paddleRect.y = 620

#allows for held down keys to continue movement
py.key.set_repeat(10, 10)

#code for the game
while 1:

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

    #check if ball is at the bottom of the screen 
    if ballRect.y == 0: 
        #creates image object to be put to the screen 
        passMessage= py.image.load("editedLevelPassed.png")
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

        #exits the game
        quit()

    #check if ball is at top
    if ballRect.y > 700: 
        #creates image object to be put to the screen 
        failMessage= py.image.load("editedLevelFailed.png")
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

        #exits the game
        quit()

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
    clock.tick(300)

    #paints over last screen
    gameDisplay.fill((0,0,0))

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