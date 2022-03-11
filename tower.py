import math
filename = "input-tower-2b94.txt"
output = open("output.txt","w")
file = open(filename,"r")
lines = file.readlines()
iterator = int(lines.pop(0).rstrip())
for test in range(iterator):
    line1 = (lines.pop(0)).rstrip().split(" ")
    floors = int(line1[0])
    level = int(line1[1])
    steps = int(line1[2])
    outputString = ""
    for floor in range(floors):
        floorInfo = lines.pop(0).rstrip().split(" ")
        floorNum = int(floorInfo[0])
        floorLength = int(floorInfo[1])
        enemyLV = int(floorInfo[2])
        levelMatrix = [0]*floorLength
        enter = []
        out = []
        monsterCount = 0
        for i in range(floorLength):
            floorRow = ((lines.pop(0)).rstrip()).split(" ")
            monsterCount += floorRow.count("M")
            if "I" in floorRow:
                enter.append(i)
                enter.append(floorRow.index("I"))
            if "O" in floorRow:
                out.append(i)
                out.append(floorRow.index("O"))
            levelMatrix[i] = floorRow
        pointerIndex = enter
        while monsterCount > 7:
            closestMonster = [-1, -1, -1]
            for i in range(floorLength):
                for j in range(floorLength):
                    if levelMatrix[i][j] == "M":
                        dist = math.sqrt((pointerIndex[0] - i) ** 2 + (pointerIndex[1] - j) ** 2)
                        if closestMonster[2] == -1:
                            closestMonster = [i, j, dist]
                        else:
                            if dist < closestMonster[2]:
                                closestMonster = [i, j, dist]
            if closestMonster[0] > pointerIndex[0]:
                yStep = 1
                yMove = "D"
            else:
                yStep = -1
                yMove = "U"
            if closestMonster[1] > pointerIndex[1]:
                xStep = 1
                xMove = "R"
            else:
                xStep = -1
                xMove = "L"
            while pointerIndex[0] != closestMonster[0]:
                pointerIndex[0] += yStep
                steps -= 1
                outputString += yMove
                if levelMatrix[pointerIndex[0]][pointerIndex[1]] == "M":
                    monsterCount -= 1
                    level -= enemyLV
                    levelMatrix[pointerIndex[0]][pointerIndex[1]] = "*"
            while pointerIndex[1] != closestMonster[1]:
                pointerIndex[1] += xStep
                outputString += xMove
                steps -= 1
                if levelMatrix[pointerIndex[0]][pointerIndex[1]] == "M":
                    monsterCount -= 1
                    level -= enemyLV
                    levelMatrix[pointerIndex[0]][pointerIndex[1]] = "*"

        if out[0] > pointerIndex[0]:
            yStep = 1
            yMove = "D"
        else:
            yStep = -1
            yMove = "U"
        if out[1] > pointerIndex[1]:
            xStep = 1
            xMove = "R"
        else:
            xStep = -1
            xMove = "L"
        while pointerIndex[0] != out[0]:
            pointerIndex[0] += yStep
            outputString += yMove
            steps -= 1
        while pointerIndex[1] != out[1]:
            pointerIndex[1] += xStep
            outputString += xMove
            steps -= 1
    print(steps)
    print(level)





    output.write("Case #" + str(test+1)+": "+outputString+"\n")
