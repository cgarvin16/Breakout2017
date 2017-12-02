import pygame as py
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,200,0)
blue = (0,0,255)

py.init()
py.font.init()
gameDisplay = py.display.set_mode((800, 700))
def game_intro():
    intro = True
    while intro:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
        gameDisplay.fill(black)
        #This displays the Title on the Main Menu screen
        largeText = py.font.SysFont("times", 100)
        text = py.font.Font.render(largeText, "Christmas Breakout", 0, white, None)
        gameDisplay.blit(text, (0, 0))

        menu = py.font.SysFont("calibri",60)
        menuText = py.font.Font.render(menu, "Main Menu", 0, blue, None)
        gameDisplay.blit(menuText, (250,180))

        #displays mouse
        mouse = py.mouse.get_pos()

        #This displays the instructions icon
        if 370+40 > mouse[0] > 370 and 400+40 > mouse[1] > 400:
            instructionIcon = py.image.load("instr_icon_trans.png")
            gameDisplay.blit(instructionIcon, (370,400))
        else:
            instructionIcon = py.image.load("instr_icon.png")
            gameDisplay.blit(instructionIcon, (370,400))

        instr = py.font.SysFont("times", 50)
        Instrtext = py.font.Font.render(instr, "Instructions", 0, green, None)
        gameDisplay.blit(Instrtext, (420, 390))

        #This displays the highscore icon
        if 370+40 > mouse[0] > 370 and 500+40 > mouse[1] > 500:
            highscoreIcon = py.image.load("highScore_icon_trans.png")
            gameDisplay.blit(highscoreIcon, (370,500))
        else:
            highscoreIcon = py.image.load("highScore_icon.png")
            gameDisplay.blit(highscoreIcon, (370,500))

        HS = py.font.SysFont("times", 50)
        HStext = py.font.Font.render(HS, "Highscores", 0, green, None)
        gameDisplay.blit(HStext, (420, 490))

        #This displays the Play Icon
        if 370+40 > mouse[0] > 370 and 300+40 > mouse[1] > 300:
            playIcon = py.image.load("resume_icon_trans.png")
            gameDisplay.blit(playIcon, (370, 300))
        else:
            playIcon = py.image.load("resume_icon.png")
            gameDisplay.blit(playIcon, (370, 300))
        
        play = py.font.SysFont("times", 50)
        Playtext = py.font.Font.render(play, "Play!", 0, green, None)
        gameDisplay.blit(Playtext, (420, 290))


        py.display.update()
        clock = py.time.Clock()
        clock.tick(15)

game_intro()


