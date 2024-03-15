import re
from math import prod
import sys
from utils import *

sys.setrecursionlimit(999999)

def j8():
    filename = "../Input/inputj8.txt"
    instruction, network = open(filename).read().split('\n\n')
    network = network.split('\n')
    a = [i[0:3] for i in network]
    b = [i[7:10] for i in network]
    c = [i[12:15] for i in network]

    def partie1():
        start = 'AAA'
        count = 0
        while start!= 'ZZZ':
            for direction in instruction:
                if direction == 'L':
                    start = b[a.index(start)]
                else:
                    start = c[a.index(start)]
                count += 1
                if start == 'ZZZ':
                    print(f"Réponse jour 8 partie 1 : {count}")

    def partie2():
        def get_distance(maze, directions, start):
            state = start
            idx = 0

            while state[2] != "Z":
                match directions[idx % len(directions)]:
                    case "R":
                        state = maze[state][1]
                    case "L":
                        state = maze[state][0]

                idx += 1

            return idx
        
        input = open(filename).read().split("\n\n")

        directions = input[0]

        maze = {}

        As = []

        for l in input[1].splitlines():
            p = re.findall(r"\w{3}", l)
            maze[p[0]] = (p[1], p[2])
            if p[0][2] == "A":
                As.append(p[0])

        dist = [get_distance(maze, directions, a) // len(directions) for a in As]

        print(f"Réponse jour 8 partie 2 : {prod(dist) * len(directions)}")

    partie1()
    partie2()

j8()
