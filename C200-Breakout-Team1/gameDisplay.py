#                                    Breakout Beta Version 0.1
#                                    Milestone 1 Complete
#                                    Done By:
#                                           Logan Fields
#                                           Charles Brooks
#                                           Carolyn Garvin
#                                    For:
#                                        CSCI-C200 Fall 2017

#imports to allow use of other modules
from Wall import Wall
from Paddle import Paddle 
import pygame as py
import sys
import random as r 
import time

#function to add scores to a scores text file for saving
def calculateScore(bricksBroken, timeTaken, score, levelCount):
    if levelCount == 1:
        finalScore = 0
        if bricksBroken >= 4 and bricksBroken <= 8:
            finalScore += 250
        elif bricksBroken > 8 and bricksBroken <= 12:
            finalScore += 200
        elif bricksBroken > 12 and bricksBroken <= 16:
            finalScore += 150
        elif bricksBroken > 16 and bricksBroken <= 10:
            finalScore += 100
        elif bricksBroken > 20 and bricksBroken <= 24:
            finalScore += 50
        elif bricksBroken > 24:
            finalScore += 0

        if timeTaken >= 25:
            finalScore += 250
        elif timeTaken > 25 and timeTaken <= 35:
            finalScore += 200
        elif timeTaken > 35 and timeTaken <= 45:
            finalScore += 150
        elif timeTaken > 45 and timeTaken <= 55:
            finalScore += 100
        elif timeTaken > 55 and timeTaken <= 65:
            finalScore += 50
        elif timeTaken > 65:
            finalScore += 0
        return finalScore

    elif levelCount == 2:
        if bricksBroken >= 4 and bricksBroken <= 8:
            finalScore += 300
        elif bricksBroken > 8 and bricksBroken <= 12:
            finalScore += 240
        elif bricksBroken > 12 and bricksBroken <= 16:
            finalScore += 180
        elif bricksBroken > 16 and bricksBroken <= 10:
            finalScore += 120
        elif bricksBroken > 20 and bricksBroken <= 24:
            finalScore += 60
        elif bricksBroken > 24:
            finalScore += 0
        
        if timeTaken >= 35:
            finalScore += 300
        elif timeTaken > 35 and timeTaken <= 50:
            finalScore += 240
        elif timeTaken > 50 and timeTaken <= 65:
            finalScore += 180
        elif timeTaken > 65 and timeTaken <= 80:
            finalScore += 120
        elif timeTaken > 80 and timeTaken <= 95:
            finalScore += 60
        elif timeTaken > 65:
            finalScore += 0
        return finalScore

    elif levelCount == 3:
        if bricksBroken >= 4 and bricksBroken <= 8:
            finalScore += 350
        elif bricksBroken > 8 and bricksBroken <= 12:
            finalScore += 280
        elif bricksBroken > 12 and bricksBroken <= 16:
            finalScore += 210
        elif bricksBroken > 16 and bricksBroken <= 10:
            finalScore += 140
        elif bricksBroken > 20 and bricksBroken <= 24:
            finalScore += 70
        elif bricksBroken > 24:
            finalScore += 0
        
        if timeTaken >= 35:
            finalScore += 350
        elif timeTaken > 35 and timeTaken <= 50:
            finalScore += 280
        elif timeTaken > 50 and timeTaken <= 65:
            finalScore += 210
        elif timeTaken > 65 and timeTaken <= 80:
            finalScore += 140
        elif timeTaken > 80 and timeTaken <= 95:
            finalScore += 70
        elif finalScore > 65:
            finalScore += 0
        return finalScore

    elif levelCount == 4:
        if bricksBroken >= 4 and bricksBroken <= 8:
            finalScore += 400
        elif bricksBroken > 8 and bricksBroken <= 12:
            finalScore += 320
        elif bricksBroken > 12 and bricksBroken <= 16:
            finalScore += 240
        elif bricksBroken > 16 and bricksBroken <= 10:
            finalScore += 160
        elif bricksBroken > 20 and bricksBroken <= 24:
            finalScore += 80
        elif bricksBroken > 24:
            finalScore += 0
        
        if timeTaken >= 35:
            finalScore += 400
        elif timeTaken > 35 and timeTaken <= 50:
            finalScore += 320
        elif timeTaken > 50 and timeTaken <= 65:
            finalScore += 240
        elif timeTaken > 65 and timeTaken <= 80:
            finalScore += 160
        elif timeTaken > 80 and timeTaken <= 95:
            finalScore += 80
        elif timeTaken > 65:
            finalScore += 0
        return finalScore

    elif levelCount == 5:
        if bricksBroken >= 4 and bricksBroken <= 10:
            finalScore += 450
        elif bricksBroken > 10 and bricksBroken <= 16:
            finalScore += 360
        elif bricksBroken > 16 and bricksBroken <= 22:
            finalScore += 270
        elif bricksBroken > 22 and bricksBroken <= 28:
            finalScore += 180
        elif bricksBroken > 28 and bricksBroken <= 32:
            finalScore += 90
        elif bricksBroken > 24:
            finalScore += 0
        
        if timeTaken >= 35:
            finalScore += 450
        elif timeTaken > 35 and timeTaken <= 50:
            finalScore += 360
        elif timeTaken > 50 and timeTaken <= 65:
            finalScore += 270
        elif timeTaken > 65 and timeTaken <= 80:
            finalScore += 180
        elif timeTaken > 80 and timeTaken <= 95:
            finalScore += 90
        elif timeTaken > 65:
            finalScore += 0
        return finalScore

def addScore():
    variable = open("highScores.txt", "a")
    name = input("Add 3 initials: ")
    score = 0 #default until we get a scoring mechanism set up
    variable.write("{0}. . . . .{1}\n".format(name, score))
    variable.close()

def resetBall():
    #randomizes initial location between bricks and paddle
    global levelCount
    ballRect.x = r.randrange(10, 790) #width is 800, above 10 and bellow 790 so not on edge of screen
    if levelCount == 5:
        ballRect.y = r.randrange(246, 610) #6 rows of bricks in level 5, ends at 206px, paddle begin at 620px, + 40 for toolbar
    else:
        ballRect.y = r.randrange(186, 610) #4 rows of bricks ending at 146px, paddle begin at 620px, + 40 for toolbar

    #variable to change ball direction; begins in random direction
    #tried using trig to calculate better angle options, but move() function only takes int
    global ballDirection
    ballDirection = [r.choice([2, -2]), r.choice([2, -2])]

def newGame():
    #holds initial level value
    global levelCount
    levelCount = 1

    wall = Wall()
    #builds wall of bricks
    wall.buildWall(gameDisplay, ballRect, ballDirection, levelCount)

    #creates new lists to avoid bugs
    global newBrickList
    global newRecList
    global newColorList
    global newHitList
    newBrickList = wall.brickList
    newRecList = wall.recList
    newColorList = wall.colorList
    newHitList = wall.hitList

    #resets intial life value
    lifeCount = 3

    #resets bricksBroken
    global bricksBroken
    bricksBroken = 0

    #resets startTime
    global startTime
    startTime = time.time()

    resetBall()

    py.display.flip()

def levelTwo():
    wall = Wall()
    gameDisplay.fill((0,0,0))
    #builds wall of bricks
    global levelCount
    wall.buildWall(gameDisplay, ballRect, ballDirection, 2)

    #creates new lists to avoid bugs
    global newBrickList
    global newRecList
    global newColorList
    global newHitList
    newBrickList = wall.brickList
    newRecList = wall.recList
    newColorList = wall.colorList
    newHitList = wall.hitList

    resetBall()

    #resets bricksBroken
    global bricksBroken
    bricksBroken = 0

    #resets startTime
    global startTime
    startTime = time.time()

    py.display.flip()
    global play
    play = True

def levelThree():
    wall = Wall()
    gameDisplay.fill((0,0,0))
    #builds wall of bricks
    global levelCount
    wall.buildWall(gameDisplay, ballRect, ballDirection, 3)

    #creates new lists to avoid bugs
    global newBrickList
    global newRecList
    global newColorList
    global newHitList
    newBrickList = wall.brickList
    newRecList = wall.recList
    newColorList = wall.colorList
    newHitList = wall.hitList

    resetBall()

    #resets bricksBroken
    global bricksBroken
    bricksBroken = 0

    #resets startTime
    global startTime
    startTime = time.time()

    py.display.flip()
    global play
    play = True

def levelFour():
    wall = Wall()
    gameDisplay.fill((0,0,0))
    #builds wall of bricks
    global levelCount
    wall.buildWall(gameDisplay, ballRect, ballDirection, 4)

    #creates new lists to avoid bugs
    global newBrickList
    global newRecList
    global newColorList
    global newHitList
    newBrickList = wall.brickList
    newRecList = wall.recList
    newColorList = wall.colorList
    newHitList = wall.hitList

    resetBall()

    #resets bricksBroken
    global bricksBroken
    bricksBroken = 0

    #resets startTime
    global startTime
    startTime = time.time()

    py.display.flip()
    global play
    play = True

def levelFive():
    wall = Wall()
    gameDisplay.fill((0,0,0))
    #builds wall of bricks
    global levelCount
    wall.buildWall(gameDisplay, ballRect, ballDirection, 5)

    #creates new lists to avoid bugs
    global newBrickList
    global newRecList
    global newColorList
    global newHitList
    newBrickList = wall.brickList
    newRecList = wall.recList
    newColorList = wall.colorList
    newHitList = wall.hitList

    resetBall()

    #resets bricksBroken
    global bricksBroken
    bricksBroken = 0

    #resets startTime
    global startTime
    startTime = time.time()

    py.display.flip()
    global play
    play = True

def game_intro():
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,200,0)
    blue = (0,0,255)
    global pause
    while pause == True: #turn this into restartGame == True once we have a pause screen to use
        for event in py.event.get():
                if event.type == py.QUIT:
                    sys.exit()
                elif py.key.get_pressed()[py.K_p]:#remove this later; this is used for pausing implementation of game_intro since we don't have a pause screen yet; use this for pause screen later
                    pause = False
                elif py.key.get_pressed()[py.K_s]:#you start on the main menu, and when you hit 's' it starts level 1 from the begining; if you go back to the main menu and try and start again, it will reset 
                    pause = False
                    play = True
                    newGame()
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
            instructionIcon = py.image.load("instr_icon_trans.jpg")
            gameDisplay.blit(instructionIcon, (370,400))
        else:
            instructionIcon = py.image.load("instr_icon.jpg")
            gameDisplay.blit(instructionIcon, (370,400))

        instr = py.font.SysFont("times", 50)
        Instrtext = py.font.Font.render(instr, "Instructions", 0, green, None)
        gameDisplay.blit(Instrtext, (420, 390))

        #This displays the highscore icon
        if 370+40 > mouse[0] > 370 and 500+40 > mouse[1] > 500:
            highscoreIcon = py.image.load("highScore_icon_trans.jpg")
            gameDisplay.blit(highscoreIcon, (370,500))
        else:
            highscoreIcon = py.image.load("highScore_icon.jpg")
            gameDisplay.blit(highscoreIcon, (370,500))

        HS = py.font.SysFont("times", 50)
        HStext = py.font.Font.render(HS, "Highscores", 0, green, None)
        gameDisplay.blit(HStext, (420, 490))

        #This displays the Play Icon
        if 370+40 > mouse[0] > 370 and 300+40 > mouse[1] > 300:
            playIcon = py.image.load("resume_icon_trans.jpg")
            gameDisplay.blit(playIcon, (370, 300))
        else:
            playIcon = py.image.load("resume_icon.jpg")
            gameDisplay.blit(playIcon, (370, 300))
        
        play = py.font.SysFont("times", 50)
        Playtext = py.font.Font.render(play, "Play!", 0, green, None)
        gameDisplay.blit(Playtext, (420, 290))


        py.display.update()
        clock = py.time.Clock()
        clock.tick(15)


def pause():
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,200,0)
    blue = (0,0,255)
    global pause
    while pause == True:
        for event in py.event.get():
                if event.type == py.QUIT:
                    sys.exit()
                elif py.key.get_pressed()[py.K_p]:#remove this later; this is used for pausing implementation of game_intro since we don't have a pause screen yet; use this for pause screen later
                    pause = False 
                elif py.key.get_pressed()[py.K_s]:#you start on the main menu, and when you hit 's' it starts level 1 from the begining; if you go back to the main menu and try and start again, it will reset 
                    pause = False
                    play = True
                    newGame()

        gameDisplay.fill(black)
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

play = True
pause = False
#beginning of the required pygame skeleton
#initializes the pygame module
py.init()

#sets the game display size as 800px width and 700px height
gameDisplay = py.display.set_mode((800, 700))

#adds title to window top of game
py.display.set_caption("Breakout")

#updates the display
py.display.flip()

#creates ball image and gives it a rectangle to manipulate later
ball = py.image.load("ballNoBackground.png")
ballRect = ball.get_rect()

#initialized level count
global levelCount
levelCount = 1

#sets initial ball direction and location
resetBall()

#creates and places paddle with a rectangle
paddle = Paddle()
paddleRect = paddle.image.get_rect()
paddleRect.x = 300
paddleRect.y = 620

#allows for held down keys to continue movement
py.key.set_repeat(10, 10)

#holds initial life value
lifeCount = 3

#initialized ballDirection variable
ballDirection = [0,0]

newBrickList = []
newRecList = []
newColorList = []
newHitList = []
testBrick = py.image.load("testBrick.png")
wCracked = py.image.load("wBrick_cracked.png")
bCracked = py.image.load("bBrick_cracked.png")
gCracked = py.image.load("gBrick_cracked.png")
rCracked = py.image.load("rBrick_cracked.png")
mCracked = py.image.load("mBrick_cracked.png")
zCracked = py.image.load("zBrick_cracked.png")

#initializes brick hit, time, and score
bricksBroken = 0
score = 0
timeTaken = 0
startTime = 0
while 1:
    pause = True
    game_intro()
    while play == True:
        #code for the game
        #how to react to events like key presses or mouse movement
        for event in py.event.get():
            #exits game if you press close window
            if event.type == py.QUIT:
                sys.exit()
            #moves paddle based on left and right arrow keys
            elif py.key.get_pressed()[py.K_LEFT]:
                paddleRect.x -= 10
            elif py.key.get_pressed()[py.K_RIGHT]:
                paddleRect.x += 10
            elif py.key.get_pressed()[py.K_p]:
                pause = True
                game_intro()
            elif py.key.get_pressed()[py.K_i]:
                game_intro()
            elif py.key.get_pressed()[py.K_s]:
                state2 = 'pause'
     
        #check if ball is at the top of the screen 
        if ballRect.y <= 42: 
            #creates image object to be put to the screen 
            passMessage= py.image.load("editedLevelPassed.png")

            #paints over the previous screen
            gameDisplay.fill((0,0,0))
            gameDisplay.blit(passMessage, (100,100))

            #moves and pauses ball to prevent if loop from repeating
            ballRect.x = 300
            ballRect.y = 440
            ballDirection[0] = 0
            ballDirection[1] = 0

            #updates the screen
            py.display.flip()

            #pauses while loop to make image visible
            py.time.wait(3000)

            #prints break line for console
            print('*'*20)
            print(levelCount)

            #adds one to the level indicator for use later
            levelCount += 1

            #prints level value to console for testing purposes
            print(levelCount)

            #prints bricksBroken to console for testing purposes
            print(bricksBroken)

            resetBall()

            #prints break line for console 
            print('-'*20)

            #prints times to console for testing
            print("start time: {0}".format(startTime))
            print("current time: {0}".format(time.time()))
            timeTaken = time.time()-startTime
            print("time taken: {0}".format(timeTaken))

            if levelCount == 2:
                levelTwo()
            elif levelCount == 3:
                levelThree()
            elif levelCount == 4:
                levelFour()
            elif levelCount == 5:
                levelFive()
            #exits the game
            #quit()

        #check if ball is at bottom
        if ballRect.y > 700: 
            #creates image object to be put to the screen 
            failMessage= py.image.load("editedLevelFailed.png")
            gameDisplay.fill((0,0,0))
            gameDisplay.blit(failMessage, (100,100))

            #moves and pauses ball to prevent if loop from repeating
            ballRect.x = 300
            ballRect.y = 440
            ballDirection[0] = 0
            ballDirection[1] = 0

            #updates the screen
            py.display.flip()

            #pauses while loop to make image visible
            py.time.wait(3000)

            resetBall()
            #exits the game
            #quit()

        #if ball hits walls, send in opposite direction 
        if ballRect.x <= 0 or ballRect.x >= 800:
            ballDirection[0] = -ballDirection[0]
        
        #how ball reacting to paddle (paddle pixel ranges: -42 <- -21 = 21 -> 42)
        if ballRect.colliderect(paddleRect):
            ballDirection[1] = -ballDirection[1]

            #variable holds the x location of the differences between the centers of the ball and the paddle
            offset = ballRect.center[0] - paddleRect.center[0]

            #tried using trig to calculate better angle options, but move() function only takes int
            if offset >= 21: #right side of paddle, pos x and neg y, sends up to right 
                ballDirection[0] = 2
                ballDirection[1] = -2
            elif offset < 21 and offset > -21: #middle of paddle, sends up 
                ballDirection[0] = 0
                ballDirection[1] = -2
            elif offset <= -21: #left side of paddle, neg x and neg y, sends up to left 
                ballDirection[0] = -2
                ballDirection[1] = -2
       
        #using Clock object in pygame and setting frames per second
        clock = py.time.Clock()
        clock.tick(600000)

        #paints over last screen
        gameDisplay.fill((0,0,0))

         #checks level and changes things if needed
    
        
        #moves ball 
        ballRect = ballRect.move(ballDirection)

        #adds ball to screen 
        gameDisplay.blit(ball, ballRect)

        #adds paddle to screen
        gameDisplay.blit(paddle.image, paddleRect)

        #updates the remaining bricks to the screen and checks if a brick has been hit
        #if the brick has been hit, it removes it from the lists
        for i in range(len(newBrickList)):
            gameDisplay.blit(newBrickList[i], newRecList[i])
            if ballRect.colliderect(newRecList[i]):
                ballDirection[0] = -ballDirection[0] 
                ballDirection[1] = -ballDirection[1] 
            if ballRect.colliderect(newRecList[i]) and newHitList[i] == 1:
                del(newBrickList[i])
                del(newRecList[i])
                del(newColorList[i])
                del(newHitList[i])
                
                #updates screen
                py.display.flip()
                
                #adds 1 to bricksBroken for score calculation
                bricksBroken += 1

                #ends loop
                break
            elif ballRect.colliderect(newRecList[i]) and newHitList[i] >= 2:
                #colors = ["wBrick.png", "rBrick.png", "gBrick.png", "bBrick.png"]
                #newBrickList[i] = testBrick
                
                if newColorList[i] == "wBrick.png":
                    newBrickList[i] = wCracked
                elif newColorList[i] == "rBrick.png":
                    newBrickList[i] = rCracked
                elif newColorList[i] == "gBrick.png":
                    newBrickList[i] = gCracked
                elif newColorList[i] == "bBrick.png":
                    newBrickList[i] = bCracked
                elif newColorList[i] == "mBrick.png":
                    newBrickList[i] = mCracked
                elif newColorList[i] == "zBrick.png":
                    newBrickList[i] = zCracked
                py.display.flip()
                newHitList[i] -= 1
                break

        #updates screen
        py.display.flip()

    #exits python
    quit()