#import statements to allow access of other modules
import pygame as py

#initializes pygame module
py.init()

#beginning of the class used to create the paddle object
#class is min. used at the moment but is being kept for planned changes in the future
class Paddle:
    def __init__(self):
        self.image = py.image.load("editedPaddleImage.png")



   """Welcome to Winter Breakout! 
    To play this game, you need to move your paddle with the left and right arrow keys. 
    You must knock the ball with your paddle and try to reach the top! 
    The ball must hit each brick at least one time to break through. 
    Unless you've reached level 2+ the bricks may require more hits to break through.
    Once you have made a path to the top and your ball has touched the top of the screen, 
    you will pass the level and move on! Be careful! don't miss the ball or you will lose a life! 
    Now that you know how to play, have fun and break down those bricks!"""