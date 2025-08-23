import sys
from utils import *

sys.setrecursionlimit(999999)

def j15():
    filename = "../Input/inputj15.txt"
        
    def partie1():
        with open(filename) as fin:
            line = fin.read().strip()


        def HASH(s):
            cur = 0
            for c in s:
                cur += ord(c)
                cur *= 17
                cur %= 256
            return cur


        parts = line.split(",")
        cur = 0
        ans = 0
        for part in parts:
            cur = HASH(part)
            ans += cur

        print(f"Réponse jour 15 partie 1 : {ans}")
    
    def partie2():
        with open(filename) as fin:
            line = fin.read().strip()


        def HASH(s):
            cur = 0
            for c in s:
                cur += ord(c)
                cur *= 17
                cur %= 256
            return cur


        boxes = [[] for _ in range(256)]

        parts = line.split(",")
        for part in parts:
            if "-" in part:
                label = part[:part.index("-")]
                box = HASH(label)
                lens = list(filter(lambda x: x[0] == label, boxes[box]))
                if len(lens) > 0:
                    idx = boxes[box].index(lens[0])
                    boxes[box].pop(idx)

            if "=" in part:
                label = part[:part.index("=")]
                box = HASH(label)
                focal_len = int(part[part.index("=")+1:])

                lens = list(filter(lambda x: x[0] == label, boxes[box]))
                if len(lens) > 0:
                    idx = boxes[box].index(lens[0])
                    boxes[box][idx] = [label, focal_len]
                else:
                    boxes[box].append([label, focal_len])

        ans = 0

        for i, box in enumerate(boxes):
            power = 0
            for j, lens in enumerate(box):
                power += (1 + i) * (j + 1) * lens[1]

            ans += power

        print(f"Réponse jour 15 partie 2 : {ans}")
    
    partie1()
    partie2()
    
j15()
