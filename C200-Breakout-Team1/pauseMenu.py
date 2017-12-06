import pygame as py
import sys

py.init()
py.font.init()
py.init()

gameDisplay = py.display.set_mode((800, 700))

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,200,0)
blue = (0,0,255)

def button(x,y,w,h,ib,ab, action=None):
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,200,0)
    blue = (0,0,255)

    #displays mouse
    mouse = py.mouse.get_pos()

    click = py.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
            instructionIcon = py.image.load(ab)
            gameDisplay.blit(instructionIcon, (x,y))
            if click[0] == 1 and action != None:
                if action == "resume":
                    pause()
                elif action == "quit":
                    py.quit()
                    quit()
                elif action == "restart":
                    newGame()
                elif action == "menu":
                    game_intro()

    else:
        instructionIcon = py.image.load(ib)
        gameDisplay.blit(instructionIcon, (x,y))

    #This displays the Title on the pause screen
        largeText = py.font.SysFont("times", 100)
        text = py.font.Font.render(largeText, "Paused", 0, red, None)
        gameDisplay.blit(text, (290, 0))


def pause():
    pause = True

    background = py.image.load("pause_background.png")
    while pause:
        for event in py.event.get():
                if event.type == py.QUIT:
                    sys.exit()

        #gameDisplay.fill()
        gameDisplay.blit(background, (0,0))

        #this displays the icons from buttons
        button(370,330,40,40,"mainMenu_icon.jpg","mainMenu_icon.jpg", "menu")
        button(370,530,40,40,"quit_icon.jpg","quit_icon.jpg", "quit")
        button(370,430,40,40,"restart_icon.png","restart.png", "restart")
        button(370,230,40,40,"resume_icon.jpg","resume_icon.jpg", "resume")

        #This diplays the texts texts next to the icons
        instr = py.font.SysFont("times", 50)
        Instrtext = py.font.Font.render(instr, "Menu", 0, green, None)
        gameDisplay.blit(Instrtext, (420, 320))

        instr = py.font.SysFont("times", 50)
        Instrtext = py.font.Font.render(instr, "Quit", 0, green, None)
        gameDisplay.blit(Instrtext, (420, 520))

        HS = py.font.SysFont("times", 50)
        HStext = py.font.Font.render(HS, "Restart", 0, green, None)
        gameDisplay.blit(HStext, (420, 420))

        play = py.font.SysFont("times", 50)
        Playtext = py.font.Font.render(play, "Resume", 0, green, None)
        gameDisplay.blit(Playtext, (420, 220))


 

        py.display.update()
        clock = py.time.Clock()
        clock.tick(15)

pause()