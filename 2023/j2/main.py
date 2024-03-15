import re
import sys

sys.setrecursionlimit(999999)

def j2():
    filename = "../Input/inputj2.txt"
    input = []
    with open(filename) as file:
        input = [line.strip() for line in file.readlines()]
        
    def partie1():
        gameID = 0
        gameIDSum = 0
        reds = 12
        greens = 13
        blues = 14
        gameIDRegex = "(\\d+(?=:))"
        setsRegex = "(?<=:)(.*)"
        redsRegex = "(\\d+)(?=\\sred)"
        greensRegex = "(\\d+)(?=\\sgreen)"
        bluesRegex = "(\\d+)(?=\\sblue)"

        for line in input:
            valid = True
            gameID = int(re.search(gameIDRegex, line).group(0))
            sets = re.search(setsRegex, line).group(0)
            sets = re.split(";", sets)
            for set in sets:
                currRed = re.search(redsRegex, set)
                if(currRed):
                    currRed = int(currRed.group(0))
                    if(currRed > reds): valid = False

                currGreen = re.search(greensRegex, set)
                if(currGreen):
                    currGreen = int(currGreen.group(0))
                    if(currGreen > greens): valid = False


                currBlue = re.search(bluesRegex, set)
                if(currBlue):
                    currBlue = int(currBlue.group(0))
                    if(currBlue > blues): valid = False
                    
            if(valid): gameIDSum += gameID

        print(f"Réponse jour 2 partie 1 : {str(gameIDSum)}")
    
    def partie2():
        sumOfPowers = 0
        setsRegex = "(?<=:)(.*)"
        redsRegex = "(\\d+)(?=\\sred)"
        greensRegex = "(\\d+)(?=\\sgreen)"
        bluesRegex = "(\\d+)(?=\\sblue)"

        for line in input:
            redMax = 0
            greenMax = 0
            blueMax = 0
            sets = re.search(setsRegex, line).group(0)
            sets = re.split(";", sets)
            for set in sets:
                currRed = re.search(redsRegex, set)
                if(currRed):
                    currRed = int(currRed.group(0))
                    if(currRed > redMax): redMax = currRed

                currGreen = re.search(greensRegex, set)
                if(currGreen):
                    currGreen = int(currGreen.group(0))
                    if(currGreen > greenMax): greenMax = currGreen

                currBlue = re.search(bluesRegex, set)
                if(currBlue):
                    currBlue = int(currBlue.group(0))
                    if(currBlue > blueMax): blueMax = currBlue
            power = redMax * greenMax * blueMax
            sumOfPowers += power

        print(f"Réponse jour 2 partie 2 : {str(sumOfPowers)}")
    
    partie1()
    partie2()
    
j2()