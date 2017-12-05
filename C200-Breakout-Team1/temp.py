#menu/pause/instructions integration testing

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

#function to add scores to a scores text file for saving
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
        ballRect.y = r.randrange(206, 610) #6 rows of bricks in level 5, ends at 206px, paddle begin at 620px
    else:
        ballRect.y = r.randrange(146, 610) #4 rows of bricks ending at 146px, paddle begin at 620px

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

    #resetBall()

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

    py.display.flip()

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

    py.display.flip()
    
    state = 'play'

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

    py.display.flip()
    state = 'play'

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

    py.display.flip()
    state = 'play'

def game_intro():
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
                elif py.key.get_pressed()[py.K_p]:
                    pause = False
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

state = 'play'
#beginning of the required pygame skeleton
#initializes the pygame module
py.init()
py.font.init()

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
#resetBall()
state2 = 'play'
pause = False
while 1:
    if levelCount == 1:
        newGame()
        resetBall()
    elif levelCount == 2:
        levelTwo()
    elif levelCount == 3:
        levelThree()
    elif levelCount == 4:
        levelFour()
    elif levelCount == 5:
        levelFive()
  
    while state == 'play':
        while state2 == 'intro':
            for event in py.event.get():

                if event.type == py.QUIT:
                    sys.exit()
                elif py.key.get_pressed()[py.K_p]:
                    game_intro()
                elif py.key.get_pressed()[py.K_s]:
                    game_intro()
            game_intro()
        while state2 == 'pause':
            for event in py.event.get():
                if event.type == py.QUIT:
                    sys.exit()
                elif py.key.get_pressed()[py.K_p]:
                    state = 'play'
            game_intro()
        #code for the game
        #how to react to events like key presses or mouse movement
        while state2 == 'play':
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
            if ballRect.y == 0: 
                #creates image object to be put to the screen 
                passMessage= py.image.load("editedLevelPassed.png")

                #paints over the previous screen
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(passMessage, (100,100))

                #moves and pauses ball to prevent if loop from repeating
                ballRect.x = 300
                ballRect.y = 400
                ballDirection[0] = 0
                ballDirection[1] = 0

                #updates the screen
                py.display.flip()

                #pauses while loop to make image visible
                py.time.wait(3000)

                #adds one to the level indicator for use later
                levelCount += 1

                #prints level value to console for testing purposes
                print(levelCount)

                resetBall()
            
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
                ballRect.y = 400
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