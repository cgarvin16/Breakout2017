#a file used to contain the main operations of the game
#imports to allow use of other modules
from Wall import Wall
from Ball import Ball
from Brick import Brick
from Paddle import Paddle 
import pygame as py
import sys
import random as r 
#beginning of the required pygame skeleton
py.init()

#sets the game display size as 800px width and 700px height
gameDisplay = py.display.set_mode((800, 700))

#adds title to window top of game
py.display.set_caption("Breakout")

#updates the display
py.display.flip()

#creates ball image; having problems doing inside a class
ball = py.image.load("ballNoBackground.png")
ballRect = ball.get_rect()

#randomizes initial location between bricks and paddle
ballRect.x = r.randrange(10, 790) #width is 800, above 10 and bellow 790 so not on edge of screen
ballRect.y = r.randrange(146, 610) #4 rows of bricks ending at 146px, paddle begin at 620px

#variable to change ball direction; begins in random direction
ballDirection = [r.choice([1, -1]), r.choice([1, -1])]

#creates wall
wall = Wall()

#creates and places paddle
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
        elif py.key.get_pressed()[py.K_LEFT]:
            paddleRect.x -= 10
        elif py.key.get_pressed()[py.K_RIGHT]:
            paddleRect.x += 10
        #add other reactions to user here as elif

    #check if ball is below paddle 
    if ballRect.y > 630: 
        ballDirection[1] = -ballDirection[1] #do something that means you lost later; keep this now for testing
        failedMessage= py.image.load("editedLevelFailed.png")
        gameDisplay.blit(failedMessage, (300,400))
        #moves and pauses ball to prevent if loop from repeating
        ballRect.x = 300
        ballRect.y = 400
        ballDirection[0] = 0
        ballDirection[1] = 0
        py.display.flip()
        #pauses while loop to make image visible
        py.time.wait(3000)
        quit()

    #check if ball is at top
    if ballRect.y < 0: #change to >= top of bricks later
        ballDirection[1] = -ballDirection[1] #do something that means you won/move on later; keep this now for testing

    #if ball hits walls, send in opposite direction 
    if ballRect.x == 0 or ballRect.x == 800:
        ballDirection[0] = -ballDirection[0]
        
    #how ball reacting to paddle
    if ballRect.colliderect(paddleRect):
        ballDirection[1] = -ballDirection[1]
        #variable holds the x location of the differences between the centers of the ball and the paddle
        offset = ballRect.center[0] - paddleRect.center[0]
        if offset > 0: #right side of paddle, pos x and neg y, sends up to right
            ballDirection[0] = abs(ballDirection[0])
            ballDirection[1] = -abs(ballDirection[1])
        elif offset < 0: #left side of paddle, neg x and neg y, sends up to left
            ballDirection[0] = -abs(ballDirection[0])
            ballDirection[1] = -abs(ballDirection[1])
    #I changed a lot of the above couple lines and then added the offset-Charles
    #I played around with the code provided by charles and got something working
       
    #slows down game; larger number, slower it goes
    py.time.delay(5)

    #paints over last screen
    gameDisplay.fill((0,0,0))

    #builds wall of bricks
    wall.buildWall(gameDisplay)

    #moves ball [so far in only one direction]
    ballRect = ballRect.move(ballDirection)

    #adds ball to screen 
    gameDisplay.blit(ball, ballRect)
    gameDisplay.blit(paddle.image, paddleRect)

    #renders screen
    py.display.flip()

#exits python
quit()