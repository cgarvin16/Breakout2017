import pygame as py
import sys

py.init()
py.font.init()
py.init()

gameDisplay = py.display.set_mode((800, 700))


def pause():
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,200,0)
    blue = (0,0,255)
    pause = True

    background = py.image.load("pause_background.png")
    while pause:
        for event in py.event.get():
                if event.type == py.QUIT:
                    sys.exit()

        #gameDisplay.fill()
        gameDisplay.blit(background, (0,0))


        #This displays the Title on the Main Menu screen
        largeText = py.font.SysFont("times", 100)
        text = py.font.Font.render(largeText, "Paused", 0, red, None)
        gameDisplay.blit(text, (290, 0))

        mouse = py.mouse.get_pos()
        print(mouse)

        #This displays the menu icon
        if 370+40 > mouse[0] > 370 and 400+40 > mouse[1] > 400:
            instructionIcon = py.image.load("mainMenu_icon.jpg")
            gameDisplay.blit(instructionIcon, (370,330))
        else:
            instructionIcon = py.image.load("mainMenu_icon.jpg")
            gameDisplay.blit(instructionIcon, (370,330))
        instr = py.font.SysFont("times", 50)
        Instrtext = py.font.Font.render(instr, "Menu", 0, green, None)
        gameDisplay.blit(Instrtext, (420, 320))

        #This diplays the Quit Icon
        if 370+40 > mouse[0] > 370 and 400+40 > mouse[1] > 400:
            instructionIcon = py.image.load("quit_icon.jpg")
            gameDisplay.blit(instructionIcon, (370,530))
        else:
            instructionIcon = py.image.load("quit_icon.jpg")
            gameDisplay.blit(instructionIcon, (370,530))
        instr = py.font.SysFont("times", 50)
        Instrtext = py.font.Font.render(instr, "Quit", 0, green, None)
        gameDisplay.blit(Instrtext, (420, 520))

  
        #This displays the restart icon
        if 370+40 > mouse[0] > 370 and 500+40 > mouse[1] > 500:
            highscoreIcon = py.image.load("restart_icon.png")
            gameDisplay.blit(highscoreIcon, (370,430))
        else:
            highscoreIcon = py.image.load("restart_icon.png")
            gameDisplay.blit(highscoreIcon, (370,430))

        HS = py.font.SysFont("times", 50)
        HStext = py.font.Font.render(HS, "Restart", 0, green, None)
        gameDisplay.blit(HStext, (420, 420))

        #This displays the Resume Icon
        if 370+40 > mouse[0] > 370 and 230+40 > mouse[1] > 230:
            playIcon = py.image.load("resume_icon_trans.jpg")
            gameDisplay.blit(playIcon, (370, 230))
        else:
            playIcon = py.image.load("resume_icon.jpg")
            gameDisplay.blit(playIcon, (370, 230))
        play = py.font.SysFont("times", 50)
        Playtext = py.font.Font.render(play, "Resume", 0, green, None)
        gameDisplay.blit(Playtext, (420, 220))


 

        py.display.update()
        clock = py.time.Clock()
        clock.tick(15)

pause()