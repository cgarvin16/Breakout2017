#a file used to contain the main operations of the game
#imports to allow use of other modules
from Wall import Wall
from Ball import Ball
from Brick import Brick
from Paddle import Paddle 
import pygame as py
import sys

#beginning of the required pygame skeleton
py.init()

#sets the game display size as 800px width and 700px height
gameDisplay = py.display.set_mode((800, 700))
#adds title to window top of game
py.display.set_caption("Breakout")

#updates the display
py.display.flip()

#creates a Ball object
ball = py.image.load("C:/python/ballResizeColored.jpg")
ballRect = ball.get_rect()
ballRect.x = 400
ballRect.y = 300
#code for the game
while 1:
    #how to react to events like key presses or mouse movement
    for event in py.event.get():
        #exits game if you press close window
        if event.type == py.QUIT:
            sys.exit()
        #add other reactions to user here as elif
    
    gameDisplay.blit(ball, (ballRect.x, ballRect.y))
    py.display.flip()
#exits python
quit()