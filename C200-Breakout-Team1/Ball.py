#a file to contain our ball class -LF
#import statements to allow access of other modules
import pygame as py

#beginning of the class used to create the ball object
class Ball():
    def __init__(self, locX, locY):
        #self.image = py.image.load("C:/python/ball.jpg")
        #self.imageRect = self.image.get_rect()
        pass
    def getRect(self):
       self.imageRect = self.image.get_rect()
       return self.imageRect

    def setLocation(self):
        pass