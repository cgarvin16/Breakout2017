def calculateScore(bricksBroken, timeTaken, score, levelCount):
    tempScore = score
    if levelCount == 1:
        if bricksBroken >= 4 and bricksBroken <= 8:
            tempScore += 250
            print(tempScore)
        elif bricksBroken > 8 and bricksBroken <= 12:
            tempScore = tempScore + 200
        elif bricksBroken > 12 and bricksBroken <= 16:
            tempScore = tempScore + 150
        elif bricksBroken > 16 and bricksBroken <= 10:
            tempScore = tempScore + 100
        elif bricksBroken > 20 and bricksBroken <= 24:
            tempScore = tempScore + 50
        elif bricksBroken > 24:
            tempScore = tempScore + 0

        if timeTaken <= 25:
            print(tempScore)
            tempScore = tempScore + 250
        elif timeTaken > 25 and timeTaken <= 35:
            tempScore = tempScore + 200
        elif timeTaken > 35 and timeTaken <= 45:
            tempScore = tempScore + 150
        elif timeTaken > 45 and timeTaken <= 55:
            tempScore = tempScore + 100
        elif timeTaken > 55 and timeTaken <= 65:
            tempScore = tempScore + 50
        elif timeTaken > 65:
            tempScore = tempScore + 0

        return tempScore

    elif levelCount == 2:
        tempScore = score
        if bricksBroken >= 4 and bricksBroken <= 8:
            tempScore = tempScore + 300
        elif bricksBroken > 8 and bricksBroken <= 12:
            tempScore = tempScore + 240
        elif bricksBroken > 12 and bricksBroken <= 16:
            tempScore = tempScore + 180
        elif bricksBroken > 16 and bricksBroken <= 10:
            tempScore = tempScore + 120
        elif bricksBroken > 20 and bricksBroken <= 24:
            tempScore = tempScore + 60
        elif bricksBroken > 24:
            tempScore = tempScore + 0
        
        if timeTaken <= 35:
            tempScore = tempScore + 300
        elif timeTaken > 35 and timeTaken <= 50:
            tempScore = tempScore + 240
        elif timeTaken > 50 and timeTaken <= 65:
            tempScore = tempScore + 180
        elif timeTaken > 65 and timeTaken <= 80:
            tempScore = tempScore + 120
        elif timeTaken > 80 and timeTaken <= 95:
            tempScore = tempScore + 60
        elif timeTaken > 65:
            tempScore = tempScore + 0
        return tempScore

    elif levelCount == 3:
        tempScore = score
        if bricksBroken >= 4 and bricksBroken <= 8:
            tempScore = tempScore + 350
        elif bricksBroken > 8 and bricksBroken <= 12:
            tempScore = tempScore + 280
        elif bricksBroken > 12 and bricksBroken <= 16:
            tempScore = tempScore + 210
        elif bricksBroken > 16 and bricksBroken <= 10:
            tempScore = tempScore + 140
        elif bricksBroken > 20 and bricksBroken <= 24:
            tempScore = tempScore + 70
        elif bricksBroken > 24:
            tempScore = tempScore + 0
        
        if timeTaken <= 35:
            tempScore = tempScore + 350
        elif timeTaken > 35 and timeTaken <= 50:
            tempScore = tempScore + 280
        elif timeTaken > 50 and timeTaken <= 65:
            tempScore = tempScore + 210
        elif timeTaken > 65 and timeTaken <= 80:
            tempScore = tempScore + 140
        elif timeTaken > 80 and timeTaken <= 95:
            tempScore = tempScore + 70
        elif tempScore > 65:
            tempScore = tempScore + 0
        return tempScore

    elif levelCount == 4:
        tempScore = score
        if bricksBroken >= 4 and bricksBroken <= 8:
            tempScore = tempScore + 400
        elif bricksBroken > 8 and bricksBroken <= 12:
            tempScore = tempScore + 320
        elif bricksBroken > 12 and bricksBroken <= 16:
            tempScore = tempScore + 240
        elif bricksBroken > 16 and bricksBroken <= 10:
            tempScore = tempScore + 160
        elif bricksBroken > 20 and bricksBroken <= 24:
            tempScore = tempScore + 80
        elif bricksBroken > 24:
            tempScore = tempScore + 0
        
        if timeTaken <= 35:
            tempScore = tempScore + 400
        elif timeTaken > 35 and timeTaken <= 50:
            tempScore = tempScore + 320
        elif timeTaken > 50 and timeTaken <= 65:
            tempScore = tempScore + 240
        elif timeTaken > 65 and timeTaken <= 80:
            tempScore = tempScore + 160
        elif timeTaken > 80 and timeTaken <= 95:
            tempScore = tempScore + 80
        elif timeTaken > 65:
            tempScore = tempScore + 0
        return tempScore

    elif levelCount == 5:
        tempScore = score
        if bricksBroken >= 4 and bricksBroken <= 10:
            tempScore = tempScore + 450
        elif bricksBroken > 10 and bricksBroken <= 16:
            tempScore = tempScore + 360
        elif bricksBroken > 16 and bricksBroken <= 22:
            tempScore = tempScore + 270
        elif bricksBroken > 22 and bricksBroken <= 28:
            tempScore = tempScore + 180
        elif bricksBroken > 28 and bricksBroken <= 32:
            tempScore = tempScore + 90
        elif bricksBroken > 24:
            tempScore = tempScore + 0
        
        if timeTaken <= 35:
            tempScore = tempScore + 450
        elif timeTaken > 35 and timeTaken <= 50:
            tempScore = tempScore + 360
        elif timeTaken > 50 and timeTaken <= 65:
            tempScore = tempScore + 270
        elif timeTaken > 65 and timeTaken <= 80:
            tempScore = tempScore + 180
        elif timeTaken > 80 and timeTaken <= 95:
            tempScore = tempScore + 90
        elif timeTaken > 65:
            tempScore = tempScore + 0
        return tempScore

print(calculateScore(4, int(23.3143252), 0, 1))