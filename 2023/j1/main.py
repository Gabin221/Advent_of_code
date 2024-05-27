import re
import sys

# sys.setrecursionlimit(999999)

def transformChaine(ligne):
    listeEntier = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    liste = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    newLine = ligne

    for i in range(0, len(liste)):
        newLine.replace(liste[i], listeEntier[i])

    return newLine

def j1():
    filename = "../Input/inputj1.txt"
    input = []
    with open(filename) as file:
        input = [line.strip() for line in file.readlines()]
        
    def partie1():
        total = 0
        for line in input:
            chaine = ""
            for i in line:
                if i.isdigit():
                    chaine += i
            total += int(chaine[0] + chaine[-1])

        print(f"Réponse jour 1 partie 1 : {total}")
    
    def partie2():
        total = 0
        for line in input:
            chaine = ""
            for i in transformChaine(line):
                if i.isdigit():
                    chaine += i

            total += int(chaine[0] + chaine[-1])
        
        print(f"Réponse jour 1 partie 2 : {total}")
    
    # partie1()
    partie2()

j1()
