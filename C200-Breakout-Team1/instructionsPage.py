import pygame as py
import sys

py.init()
py.font.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,200,0)
blue = (0,0,255)

gameDisplay = py.display.set_mode((800, 700))

def instruction_screen():
    
    while paused == True:
        gameDisplay.fill(black)

        largeText = py.font.SysFont("times", 100)
        text = py.font.Font.render(largeText, "Instructions:", 0, white, None)
        gameDisplay.blit(text, (150, 0))

        instr = py.font.SysFont("calibri",30)
        instrText = py.font.Font.render(instr,"Welcome to Winter Breakout!", 0, red, None)
        gameDisplay.blit(instrText,(230,200))

        instr = py.font.SysFont("calibri",20)
        instrText = py.font.Font.render(instr,"To play this game, you need to move your paddle with the left and right arrow keys.", 0, blue, None)
        gameDisplay.blit(instrText,(80,300))

        instr = py.font.SysFont("calibri",20)
        instrText = py.font.Font.render(instr,"You must knock the ball with your paddle and try to reach the top!", 0, blue, None)
        gameDisplay.blit(instrText,(80,320))

        instr = py.font.SysFont("calibri",20)
        instrText = py.font.Font.render(instr,"The ball must hit each brick at least one time to break through.", 0, blue, None)
        gameDisplay.blit(instrText,(80,340))

        instr = py.font.SysFont("calibri",20)
        instrText = py.font.Font.render(instr,"*Once you reach level 2 and above the bricks may require more hits to break through.*", 0, blue, None)
        gameDisplay.blit(instrText,(80,360))

        instr = py.font.SysFont("calibri",20)
        instrText = py.font.Font.render(instr,"Once you have made a path to the top and your ball has touched the top of the screen,", 0, blue, None)
        gameDisplay.blit(instrText,(80,380))

        instr = py.font.SysFont("calibri",20)
        instrText = py.font.Font.render(instr,"you will pass the level and move on! Be careful! don't miss the ball or you will lose a life!", 0, blue, None)
        gameDisplay.blit(instrText,(80,400))

        instr = py.font.SysFont("calibri",20)
        instrText = py.font.Font.render(instr,"Now that you know how to play, have fun and break down those bricks!", 0, blue, None)
        gameDisplay.blit(instrText,(80,420))

        py.display.update()
        clock = py.time.Clock()
        clock.tick(15)
while 1:        
    paused = True
    for e in py.event.get():
        if py.key.get_pressed()[py.K_p]:
            paused == True
        elif e.type == py.QUIT:
            sys.exit()
        elif py.key.get_pressed()[py.K_ESCAPE]:
            sys.exit()
    instruction_screen()


