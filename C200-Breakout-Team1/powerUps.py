import pygame as py
import sys
import random as r


py.init()



class powerUps(py.sprite.Sprite):
    powerup_images = {}
    powerup_images = [life] = py.image.load("drop_heart_icon.png").convert()
    powerup_images = [bigPaddle] = py.image.load("largePaddleImage.png").convert()

    def __init__(self,center):
        py.sprite.Sprite.__init__(self)
        self.type = r.choice('life', 'bigPaddle')
        self.image = powerup_images[self.type]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y =+ self.speedy
        if self.rect.top > HEIGHT:
            self.kill()




        

"""def powerups():
    self.type = random.choice(lifRect, paddlePRect)
    self.image = powerup_images[self.type]
    self.rect.center = center
    self.speedy = 2


    lifepowerUP = py.image.load("drop_heart_icon.png")
    lifeRect = lifepowerUp.get_rect()
    paddlepowerUP = py.image.load("largePaddleImage.png")
    paddlePRect = paddlepwerUp.get_rect()

newBrickList = []
newRecList = []
newColorList = []
newHitList = []"""

