import pygame as py

py.init()
py.font.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,200,0)
blue = (0,0,255)

gameDisplay = py.display.set_mode((800, 700))

def instruction_screen():
    gameDisplay.fill(black)
    largeText = py.font.SysFont("times", 100)
    text = py.font.Font.render(largeText, "Instructions:", 0, white, None)
    gameDisplay.blit(text, (150, 0))

    py.display.update()
    clock = py.time.Clock()
    clock.tick(15)

instruction_screen()


