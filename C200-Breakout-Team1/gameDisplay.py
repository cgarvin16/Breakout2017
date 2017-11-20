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

#randomizes initial location with assumed paddle location under 100px and assumed brick location over 600px
ballRect.x = r.randrange(20, 680) #change ranges once paddles and bricks are set
ballRect.y = r.randrange(100, 600) #change ranges once paddles and bricks are set

#variable to change ball direction; begins in random direction
ballDirection = [r.choice([1, -1]), r.choice([1, -1])]

#creates wall
wall = Wall()
paddle = Paddle()
paddleRect = paddle.image.get_rect()
paddleRect.x = 300
paddleRect.y = 620
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
    if ballRect.bottom == 0: #change to <= under paddle later
        ballDirection[1] = -ballDirection[1] #do something that means you lost later; keep this now for testing

    #check if ball is at top
    if ballRect.top == 700: #change to >= top of bricks later
        ballDirection[1] = -ballDirection[1] #do something that means you won/move on later; keep this now for testing

    #if ball hits walls, send in opposite direction 
    if ballRect.left == 0 or ballRect.right == 800:
        ballDirection[0] = -ballDirection[0]
        
    #ball reacting to paddle
    if ballRect.colliderect(paddleRect):
        ballDirection[0] = -ballDirection[0]
        ballDirection[1] = -ballDirection[1]
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