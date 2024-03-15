from queue import Queue
import re
import sys
from utils import *

sys.setrecursionlimit(999999)

def j4():
    filename = "../Input/inputj4.txt"
    with open(filename, 'r') as f:
        input = f.read()
        
    def partie1():
        regex = r':(.*)\|(.*)'
        points = 0
        for win_nums, true_nums in re.findall(regex, input):
            overlap = set(win_nums.split()) & set(true_nums.split())
            if overlap:
                points += 2 ** (len(overlap) - 1)

        print(f"Réponse jour 4 partie 1 : {points}")
    
    def partie2():
        lines = []
        with open(filename) as file:
            lines = [line.strip() for line in file.readlines()]
        ans = 0
        d = {}
        q = Queue()

        for line in lines:
            cid, numbers = line.split(':')
            cid = int(cid[4:])
            winner, ours = numbers.split('|')
            ws = set(winner.split())
            os = set(ours.split())
            matches = ws & os

            # for each card, we just need to know how many new cards we add to the queue
            d[cid] = len(matches)
            # and fill the queue with the initial cards
            q.put(cid)


        # we proccess the queue until it's empty
        while not q.empty():
            ans += 1
            k = q.get()
            # and for each card, we add how many matches it had
            # starting from it's id (k) + 1
            for i in range(k + 1, k + d[k] + 1):
                q.put(i)
        
        print(f"Réponse jour 4 partie 2 : {ans}")
    
    partie1()
    partie2()
    
j4()
