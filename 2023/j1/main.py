import re
import sys

sys.setrecursionlimit(999999)

def j1():
    filename = "../Input/inputj1.txt"
    input = []
    with open(filename) as file:
        input = [line.strip() for line in file.readlines()]
        
    def partie1():
        total = 0
        for line in input:
            print(line)

        print(f"Réponse jour 1 partie 1 : {total}")
    
    def partie2():
        values = {
            "one": "1", 
            "two": "2", 
            "three": "3", 
            "four": "4", 
            "five": "5", 
            "six": "6", 
            "seven": "7", 
            "eight": "8", 
            "nine": "9"
            }
        pairs = []
        for line in input:
            digits = []
            for i,c in enumerate(line):
                if line[i].isdigit():
                    digits.append(line[i])
                else:
                    for k in values.keys():
                        if line[i:].startswith(k):
                            digits.append(values[k])
            pairs.append(int(f"{digits[0]}{digits[-1]}"))
        
        print(f"Réponse jour 1 partie 2 : {sum(pairs)}")
    
    partie1()
    # partie2()

j1()
