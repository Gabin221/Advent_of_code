import re
import sys

# sys.setrecursionlimit(999999)

def premierNbr(ligne):
    liste = ["1", "one", "2", "two", "3", "three", "4", "four", "5", "five", "6", "six", "7", "seven", "8", "eight", "9", "nine"]
    premier = ""

    for i in range(0, len(liste)):
        if liste[i] in ligne:
            if i%2 == 0:
                premier += liste[i]
            else:
                premier += liste[i - 1]
            break
    return premier


def dernierNbr(ligne):
    liste = ["1", "one", "2", "two", "3", "three", "4", "four", "5", "five", "6", "six", "7", "seven", "8", "eight", "9", "nine"]
    positions = []

    for i in liste:
        if i in ligne:
            positions.append(liste.index(i))
        else:
            positions.append(19)

    dernier = int([i for i in positions if i != 19][-1])
    if dernier%2 == 0:
        return liste[dernier]
    else:
        return liste[dernier-1]


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
            total += int(premierNbr(line) + dernierNbr(line))
            print(f"{line}: {int(premierNbr(line) + dernierNbr(line))}")
        
        print(f"Réponse jour 1 partie 2 : {total}")
    
    # partie1()
    partie2()

j1()
