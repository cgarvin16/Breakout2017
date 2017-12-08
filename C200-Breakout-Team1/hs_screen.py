import pygame as py
import sys

py.init()
py.font.init()
py.init()

gameDisplay = py.display.set_mode((800, 700))

def addScore1(score):
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
    print("final high scores: {0}".format(finalHighScores))

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

def hs_screen():

    print("final high score after functions: {0}".format(finalHighScores))
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,200,0)
    blue = (0,0,255)

    gameDisplay.fill(black)

    largeText = py.font.SysFont("times", 100)
    text = py.font.Font.render(largeText, "Higscores:", 0, white, None)
    gameDisplay.blit(text, (150, 0))

    instr = py.font.SysFont("calibri",40)
    placeCounter = 1
    y = 150
    for i in range(0, 10):
        instrText = py.font.Font.render(instr, "{0}) {1}        {2}".format(placeCounter, finalHighScores[i][0], finalHighScores[i][1]), 0, white, None)
        gameDisplay.blit(instrText, (200, y))
        y += 50
        placeCounter += 1

    py.display.update()


finalHighScores = []
print(finalHighScores)
addScore1(200)
topTenScores()
overWriteScores()
while 1:        
    paused = True
    for e in py.event.get():
        if py.key.get_pressed()[py.K_p]:
            paused == True
        elif e.type == py.QUIT:
            sys.exit()
        elif py.key.get_pressed()[py.K_ESCAPE]:
            sys.exit()
    hs_screen()

