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
    global finalScore
    if levelCount == 1:
        if bricksBroken >= 4 and bricksBroken <= 8:
            finalScore += 250
        elif bricksBroken > 8 and bricksBroken <= 12:
            finalScore = finalScore + 200
        elif bricksBroken > 12 and bricksBroken <= 16:
            finalScore = finalScore + 150
        elif bricksBroken > 16 and bricksBroken <= 10:
            finalScore = finalScore + 100
        elif bricksBroken > 20 and bricksBroken <= 24:
            finalScore = finalScore + 50
        elif bricksBroken > 24:
            finalScore = finalScore + 0

        if timeTaken >= 25:
            finalScore = finalScore + 250
        elif timeTaken > 25 and timeTaken <= 35:
            finalScore = finalScore + 200
        elif timeTaken > 35 and timeTaken <= 45:
            finalScore = finalScore + 150
        elif timeTaken > 45 and timeTaken <= 55:
            finalScore = finalScore + 100
        elif timeTaken > 55 and timeTaken <= 65:
            finalScore = finalScore + 50
        elif timeTaken > 65:
            finalScore = finalScore + 0
        return finalScore

    elif levelCount == 2:
        finalScore = score
        if bricksBroken >= 4 and bricksBroken <= 8:
            finalScore = finalScore + 300
        elif bricksBroken > 8 and bricksBroken <= 12:
            finalScore = finalScore + 240
        elif bricksBroken > 12 and bricksBroken <= 16:
            finalScore = finalScore + 180
        elif bricksBroken > 16 and bricksBroken <= 10:
            finalScore = finalScore + 120
        elif bricksBroken > 20 and bricksBroken <= 24:
            finalScore = finalScore + 60
        elif bricksBroken > 24:
            finalScore = finalScore + 0
        
        if timeTaken >= 35:
            finalScore = finalScore + 300
        elif timeTaken > 35 and timeTaken <= 50:
            finalScore = finalScore + 240
        elif timeTaken > 50 and timeTaken <= 65:
            finalScore = finalScore + 180
        elif timeTaken > 65 and timeTaken <= 80:
            finalScore = finalScore + 120
        elif timeTaken > 80 and timeTaken <= 95:
            finalScore = finalScore + 60
        elif timeTaken > 65:
            finalScore = finalScore + 0
        return finalScore

    elif levelCount == 3:
        finalScore = score
        if bricksBroken >= 4 and bricksBroken <= 8:
            finalScore = finalScore + 350
        elif bricksBroken > 8 and bricksBroken <= 12:
            finalScore = finalScore + 280
        elif bricksBroken > 12 and bricksBroken <= 16:
            finalScore = finalScore + 210
        elif bricksBroken > 16 and bricksBroken <= 10:
            finalScore = finalScore + 140
        elif bricksBroken > 20 and bricksBroken <= 24:
            finalScore = finalScore + 70
        elif bricksBroken > 24:
            finalScore = finalScore + 0
        
        if timeTaken >= 35:
            finalScore = finalScore + 350
        elif timeTaken > 35 and timeTaken <= 50:
            finalScore = finalScore + 280
        elif timeTaken > 50 and timeTaken <= 65:
            finalScore = finalScore + 210
        elif timeTaken > 65 and timeTaken <= 80:
            finalScore = finalScore + 140
        elif timeTaken > 80 and timeTaken <= 95:
            finalScore = finalScore + 70
        elif finalScore > 65:
            finalScore = finalScore + 0
        return finalScore

    elif levelCount == 4:
        finalScore = score
        if bricksBroken >= 4 and bricksBroken <= 8:
            finalScore = finalScore + 400
        elif bricksBroken > 8 and bricksBroken <= 12:
            finalScore = finalScore + 320
        elif bricksBroken > 12 and bricksBroken <= 16:
            finalScore = finalScore + 240
        elif bricksBroken > 16 and bricksBroken <= 10:
            finalScore = finalScore + 160
        elif bricksBroken > 20 and bricksBroken <= 24:
            finalScore = finalScore + 80
        elif bricksBroken > 24:
            finalScore = finalScore + 0
        
        if timeTaken >= 35:
            finalScore = finalScore + 400
        elif timeTaken > 35 and timeTaken <= 50:
            finalScore = finalScore + 320
        elif timeTaken > 50 and timeTaken <= 65:
            finalScore = finalScore + 240
        elif timeTaken > 65 and timeTaken <= 80:
            finalScore = finalScore + 160
        elif timeTaken > 80 and timeTaken <= 95:
            finalScore = finalScore + 80
        elif timeTaken > 65:
            finalScore = finalScore + 0
        return finalScore

    elif levelCount == 5:
        finalScore = score
        if bricksBroken >= 4 and bricksBroken <= 10:
            finalScore = finalScore + 450
        elif bricksBroken > 10 and bricksBroken <= 16:
            finalScore = finalScore + 360
        elif bricksBroken > 16 and bricksBroken <= 22:
            finalScore = finalScore + 270
        elif bricksBroken > 22 and bricksBroken <= 28:
            finalScore = finalScore + 180
        elif bricksBroken > 28 and bricksBroken <= 32:
            finalScore = finalScore + 90
        elif bricksBroken > 24:
            finalScore = finalScore + 0
        
        if timeTaken >= 35:
            finalScore = finalScore + 450
        elif timeTaken > 35 and timeTaken <= 50:
            finalScore = finalScore + 360
        elif timeTaken > 50 and timeTaken <= 65:
            finalScore = finalScore + 270
        elif timeTaken > 65 and timeTaken <= 80:
            finalScore = finalScore + 180
        elif timeTaken > 80 and timeTaken <= 95:
            finalScore = finalScore + 90
        elif timeTaken > 65:
            finalScore = finalScore + 0
        return finalScore

def addScore(score):
    #opens static file to read scores and check against current score
    #also opens for appending, not overwriting 
    highScores1 = open("highScores.txt", "r+")
    
    #empty lists to hold stuff for later
    noLineScoreList1 = []
    readyScoreList1 = []
    finalScoreList1 = []

    #reads in all of the scores from highScores.txt
    scoreList1 = highScores1.readlines()

    #removes the new line characters from each string in scoreList
    for i in range(len(scoreList1)):
        noLineScoreList1.append(scoreList1[i].strip("\n"))

    #splits the initials from the scores in scoreList
    for i in range(len(noLineScoreList1)):
        readyScoreList1.append(noLineScoreList1[i].split(". . . . ."))

    #sorts readyScoreList in reverse (highest is index 0) by the 2nd sub-item (the score) in each list 
    sortedList1 = sorted(readyScoreList1, key = lambda x: int(x[1]), reverse=True)
    print(scoreList1)
    print("*"*20)
    print(sortedList1)

    #if there are less than 10 scores on the list, add this score to the list 
    if len(sortedList1) <= 10:
        name = input("Add 3 initials: ")
        highScores1.write("{0}. . . . .{1}\n".format(name, score))
    #if there are more than 10 scores on the list, check to see if this score is greater than any of them
    #if it is higher than any of the 10 scores, add it to the list
    elif len(sortedList1) > 10:
        for i in range(len(sortedList1)):
            if int(sortedList1[i][1]) < score:
                name = input("Add 3 initials: ")
                highScores1.write("{0}. . . . .{1}\n".format(name, score))
                break
    highScores1.close()
   
    #print(scoreList1)
    #print(sortedList1)
    print("-"*30)
    
def topTenScores():
    #opens static file to read scores 
    highScores2 = open("highScores.txt", "r")

    #empty lists to hold stuff for later
    noLineScoreList2 = []
    readyScoreList2 = []
    finalScoreList2 = []

    #reads each line of the file into the list scoreList2
    scoreList2 = highScores2.readlines()

    #removes the new line characters from each string in scoreList
    for i in range(len(scoreList2)):
        noLineScoreList2.append(scoreList2[i].strip("\n"))

    #splits the initials from the scores in scoreList
    for i in range(len(noLineScoreList2)):
        readyScoreList2.append(noLineScoreList2[i].split(". . . . ."))

    #sorts readyScoreList in reverse (highest is index 0) by the 2nd sub-item (the score) in each list
    sortedList2 = sorted(readyScoreList2, key = lambda x: int(x[1]), reverse=True)

    #sets the top 10 stores of the sorted list to finalHighScores
    global finalHighScores
    finalHighScores = sortedList2[:10]

    #printing for testing
    print(scoreList2)
    print(noLineScoreList2)
    print(readyScoreList2)
    print(sortedList2)
    print(finalHighScores)

    #closes file
    highScores2.close()

def overWriteScores():
    #opens highScores.txt in overwrite mode
    highScores = open("highScores.txt", "w")

    #retrieves finalHighScores results from topTenScores()
    global finalHighScores

    #writes each index of finalHighScores into highScores.txt in the proper format
    for i in range(len(finalHighScores)):
        highScores.write(str(finalHighScores[i][0]) + ". . . . ." + str(finalHighScores[i][1]) + "\n")

    #closes highScores.txt
    highScores.close()

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
    ballDirection = [r.choice([3, -3]), r.choice([3, -3])]

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

def button_i(x,y,w,h,ib,ab, action=None):
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,200,0)
    blue = (0,0,255)
    pink = (255,150,150)

    #displays mouse
    mouse = py.mouse.get_pos()

    click = py.mouse.get_pressed()
    global pause

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
            instructionIcon = py.image.load(ab)
            gameDisplay.blit(instructionIcon, (x,y))
            if click[0] == 1 and action != None:
                if action == "play":
                    pause = False
                    play = True
                    newGame()
                elif action == "scores":
                    pass
                elif action == "instr":
                    pass
    else:
        instructionIcon = py.image.load(ib)
        gameDisplay.blit(instructionIcon, (x,y))
        
    #This displays the Title on the Main Menu screen
    largeText = py.font.SysFont("times", 100)
    text = py.font.Font.render(largeText, "Christmas Breakout", 0, pink, None)
    gameDisplay.blit(text, (0, 0))

    menu = py.font.SysFont("calibri",60)
    menuText = py.font.Font.render(menu, "Main Menu", 0, blue, None)
    gameDisplay.blit(menuText, (250,180))

def game_intro():
    white = (255,255,255)
    black = (0,0,0)
    green = (50,200,50)
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

        background = py.image.load("menu_background.png") #adds an image background
        gameDisplay.blit(background, (0,0))

        santa = py.image.load('santa_icon.png')
        gameDisplay.blit(santa, (0,150))


        #displays mouse
        mouse = py.mouse.get_pos()

         #this displays the icons from buttons
        button_i(370,400,40,40,"instr_icon.jpg","instr_icon.jpg", "instr")
        button_i(370,500,40,40,"highScore_icon.jpg","highScore_icon.jpg", "scores")
        button_i(370,300,40,40,"resume_icon.jpg","resume_icon.jpg", "play")


        #this displays the texts on the screen
        instr = py.font.SysFont("times", 50)
        Instrtext = py.font.Font.render(instr, "Instructions", 0, green, None)
        gameDisplay.blit(Instrtext, (420, 390))

        HS = py.font.SysFont("times", 50)
        HStext = py.font.Font.render(HS, "Highscores", 0, green, None)
        gameDisplay.blit(HStext, (420, 490))
        
        play = py.font.SysFont("times", 50)
        Playtext = py.font.Font.render(play, "Play!", 0, green, None)
        gameDisplay.blit(Playtext, (420, 290))

        py.display.update()
        
def button_p(x,y,w,h,ib,ab, action=None):
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,200,0)
    blue = (0,0,255)

    #displays mouse
    mouse = py.mouse.get_pos()

    click = py.mouse.get_pressed()
    global pause

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
            instructionIcon = py.image.load(ab)
            gameDisplay.blit(instructionIcon, (x,y))
            if click[0] == 1 and action != None:
                if action == "resume":
                    pause = False
                elif action == "quit":
                    py.quit()
                    quit()
                elif action == "restart":
                    pause = False
                    play = True
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

def pause_screen():
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

        background = py.image.load("pause_background.png") #adds an image background
        gameDisplay.blit(background, (0,0))

        sleigh = py.image.load('sleigh_icon.png')
        gameDisplay.blit(sleigh, (0,400))

        #This displays the Title on the Main Menu screen
        largeText = py.font.SysFont("times", 100)
        text = py.font.Font.render(largeText, "Paused", 0, red, None)
        gameDisplay.blit(text, (290, 0))

        mouse = py.mouse.get_pos()
        #print(mouse)

         #this displays the icons from buttons
        button_p(370,330,40,40,"mainMenu_icon.jpg","mainMenu_icon.jpg", "menu")
        button_p(370,530,40,40,"quit_icon.jpg","quit_icon.jpg", "quit")
        button_p(370,430,40,40,"restart_icon.jpg","restart_icon.jpg", "restart")
        button_p(370,230,40,40,"resume_icon.jpg","resume_icon.jpg", "resume")

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

def updateToolbar():
    #default font and size for the toolbar
    font = py.font.SysFont("times", 30)

    #display score, but don't recaluclate it because it can only be calculated at the end of a level
    global score
    currentScore = py.font.Font.render(font, "Score: {0}".format(score), 0, (255, 255, 255), None)
    gameDisplay.blit(currentScore, (10, 5))

    #displays time on current level
    timer = time.time() - startTime
    runningTime = py.font.Font.render(font, "Time: {0}".format(int(timer)), 0, (255, 255, 255), None)
    gameDisplay.blit(runningTime, (180, 5))

    #displays title of level based on if statement
    global levelCount
    if levelCount == 1:
        levelTitle = "Level 1"
    elif levelCount == 2:
        levelTitle = "Level 2"
    elif levelCount == 3:
        levelTitle = "Level 3"
    elif levelCount == 4:
        levelTitle = "Level 4"
    elif levelCount == 5: 
        levelTitle = "Level 5"
    title = py.font.Font.render(font, levelTitle, 0, (255,255,255), None)
    gameDisplay.blit(title, (350, 5))

    global lifeCount
    life = py.font.Font.render(font, "Life: ", 0, (255, 255, 255), None)
    gameDisplay.blit(life, (600, 5))
    if lifeCount == 3:
        #display 3 hearts
        gameDisplay.blit(heart, (670, 18))
        gameDisplay.blit(heart, (700, 18))
        gameDisplay.blit(heart, (730, 18))
    elif lifeCount == 2:
        #display 2 hearts
        gameDisplay.blit(heart, (670, 18))
        gameDisplay.blit(heart, (700, 18))
    elif lifeCount == 1:
        #display 1 heart
        gameDisplay.blit(heart, (670, 18))

    #print("Timer: {0}".format(int(timer)))

    py.display.flip()

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

EwCracked= py.image.load("wBrick_Ecracked.png")
EbCracked = py.image.load("bBrick_Ecracked.png")
EgCracked = py.image.load("gBrick_Ecracked.png")
ErCracked = py.image.load("rBrick_Ecracked.png")
EmCracked = py.image.load("mBrick_Ecracked.png")
EzCracked = py.image.load("zBrick_Ecracked.png")


heart = py.image.load("new_heart_icon.png")

#initializes brick hit, time, and score
bricksBroken = 0
score = 0
timeTaken = 0
startTime = 0
finalScore = 0
finalHighScores = []
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
                pause_screen()
            elif py.key.get_pressed()[py.K_i]:
                game_intro()
            elif py.key.get_pressed()[py.K_s]:
                state2 = 'pause'
     
        #check if ball is at the top of the screen 
        if ballRect.y <= 42: 

            #paints over the previous screen
            background = py.image.load("menu_background.png") #adds an image background
            gameDisplay.blit(background, (0,0))

            #creates image object to be put to the screen 
            passMessage= py.image.load("editedLevelPassed.png")
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

            #updates score
            score = calculateScore(bricksBroken, timeTaken, score, levelCount)

            #adds one to the level indicator for use later
            levelCount += 1

            #prints level value to console for testing purposes
            #print(levelCount)

            #prints bricksBroken to console for testing purposes
            print("Bricks Broken: " + str(bricksBroken))

            resetBall()

            #prints break line for console 
            print('-'*20)

            #prints times to console for testing
            print("start time: {0}".format(startTime))
            print("current time: {0}".format(time.time()))
            timeTaken = time.time()-startTime
            print("time taken: {0}".format(timeTaken))
            

            if levelCount == 2:
                pause = True
                pause_screen()
                levelTwo()
            elif levelCount == 3:
                pause = True
                pause_screen()
                levelThree()
            elif levelCount == 4:
                pause = True
                pause_screen()
                levelFour()
            elif levelCount == 5:
                pause = True
                pause_screen()
                levelFive()
            elif levelCount == 6:
                addScore(score)
                topTenScores()
                overWriteScores()
            #exits the game
            #quit()

        #check if ball is at bottom
        if ballRect.y > 700: 
            #creates image object to be put to the screen 
            background = py.image.load("failed_background.png") #adds an image background
            gameDisplay.blit(background, (0,0))
            failMessage= py.image.load("editedLevelFailed.png")
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

            lifeCount -= 1
            
            #console printing for testing
            print("LifeCount: " + str(lifeCount))

            #if lifeCount is over 3, it pauses to prepare for new ball
            #if lifeCount is 0, it prints 'game over' to console (which is for testing) and goes back to the main menu
            if lifeCount > 0:
                pause = True
                pause_screen()
            elif lifeCount < 1:
                print('game over')
                addScore(score)
                topTenScores()
                overWriteScores()
                pause = True
                game_intro()
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
                ballDirection[0] = 3
                ballDirection[1] = -3
            elif offset < 21 and offset > -21: #middle of paddle, sends up 
                ballDirection[0] = 0
                ballDirection[1] = -3
            elif offset <= -21: #left side of paddle, neg x and neg y, sends up to left 
                ballDirection[0] = -3
                ballDirection[1] = -3
       
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
            elif ballRect.colliderect(newRecList[i]) and newHitList[i] == 2:
                if newColorList[i] == "wBrick.png" or newColorList[i] == "wCracked":
                    newBrickList[i] = EwCracked
                elif newColorList[i] == "rBrick.png" or newColorList[i] == "rCracked":
                    newBrickList[i] = ErCracked
                elif newColorList[i] == "gBrick.png" or newColorList[i] == "gCracked":
                    newBrickList[i] = EgCracked
                elif newColorList[i] == "bBrick.png" or newColorList[i] == "bCracked":
                    newBrickList[i] = EbCracked
                elif newColorList[i] == "mBrick.png" or newColorList[i] == "mCracked":
                    newBrickList[i] = EmCracked
                elif newColorList[i] == "zBrick.png" or newColorList[i] == "zCracked":
                    newBrickList[i] = EzCracked
                py.display.flip()
                newHitList[i] -= 1
                break

            elif ballRect.colliderect(newRecList[i]) and newHitList[i] == 3:
                #colors = ["wBrick.png", "rBrick.png", "gBrick.png", "bBrick.png"]
                #newBrickList[i] = testBrick
                
                if newColorList[i] == "wBrick.png":
                    newBrickList[i] = wCracked
                    newColorList[i] = "wCracked"
                elif newColorList[i] == "rBrick.png":
                    newBrickList[i] = rCracked
                    newColorList[i] = "rCracked"
                elif newColorList[i] == "gBrick.png":
                    newBrickList[i] = gCracked
                    newColorList[i] = "gCracked"
                elif newColorList[i] == "bBrick.png":
                    newBrickList[i] = bCracked
                    newColorList[i] = "bCracked"
                elif newColorList[i] == "mBrick.png":
                    newBrickList[i] = mCracked
                    newColorList[i] = "mCracked"
                elif newColorList[i] == "zBrick.png":
                    newBrickList[i] = zCracked
                    newColorList[i] = "zCracked"
                py.display.flip()
                newHitList[i] -= 1
                break
        
        updateToolbar()
        #updates screen
        py.display.flip()

    #exits python
    quit()