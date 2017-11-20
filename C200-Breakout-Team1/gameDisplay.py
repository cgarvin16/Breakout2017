#a file used to contain the main operations of the game
#imports to allow use of other modules
from Wall import Wall
from Ball import Ball
from Brick import Brick
from Paddle import Paddle 
import pygame as py
import sys
import random
#beginning of the required pygame skeleton
py.init()

#sets the game display size as 800px width and 700px height
gameDisplay = py.display.set_mode((800, 700))

#adds title to window top of game
py.display.set_caption("Breakout")

#updates the display
py.display.flip()

#creates ball image; having problems doing inside a class
ball = py.image.load("C:/python/ballNoBackground.png")
ballRect = ball.get_rect()

#randomizes initial location with assumed paddle location under 100px and assumed brick location over 600px
ballRect.x = random.randrange(20, 680)
ballRect.y = random.randrange(100, 600)

#variable to change ball direction
ballDirection = [-1, -1]
#code for the game
while 1:

    #how to react to events like key presses or mouse movement
    for event in py.event.get():

        #exits game if you press close window
        if event.type == py.QUIT:
            sys.exit()
        #add other reactions to user here as elif

    #check if ball is below paddle 
    if ballRect.bottom <= 0:
        pass #do something that means you lost

    #check if ball is at top
    if ballRect.top >= 100:
        pass #do something that means you won/move on

    #if ball hits walls, send in opposite direction [needs fine tuning for angles, not opposite]
    if ballRect.left == 0 or ballRect.right == 800:
        ballDirection[0] = -ballDirection[0]
        ballDirection[1] = -ballDirection[1]


    
        
    #slows down game
    py.time.delay(10)



    #paints over last screen
    gameDisplay.fill((0,0,0))

    #moves ball [so far in only one direction]
    ballRect = ballRect.move(ballDirection)

    #adds ball to screen 
    gameDisplay.blit(ball, ballRect)

    #renders screen
    py.display.flip()

#exits python
quit()