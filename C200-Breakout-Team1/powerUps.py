import pygame as py
import sys
import random as r


py.init()



class powerUps(py.sprite.Sprite):

    def __init__(self, type ='dropHeart'):
        py.sprite.Sprite.__init__(self)
        self.type = r.choice('life', 'bigPaddle')
        self.image = powerup_images[self.type]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

        print("yes")

    def update(self):
        self.rect.y =+ self.speedy
        if self.rect.top > HEIGHT:
            self.kill()


life = py.image.load("drop_heart_icon.png")
bigPaddle = py.image.load("largePaddleImage.png")
        


