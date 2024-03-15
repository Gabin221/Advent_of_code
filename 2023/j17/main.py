import re
from operator import mul
from queue import Queue
import numpy as np 
from collections import Counter, defaultdict
from math import prod
import sys
from typing import List
from time import perf_counter
from matplotlib.path import Path
from time import perf_counter
from itertools import combinations
from tqdm import tqdm
from pprint import pprint
from copy import deepcopy
import heapq
from utils import *
from cProfile import run
from functools import cache
from sympy import var, Eq, solve
import networkx
import random

sys.setrecursionlimit(999999)

def j17():
    filename = "../Input/inputj17.txt"
    
    def get_min(grid, min_l=1, max_l=3):
        s = (0, 0)
        e = (len(grid[0]) - 1, len(grid) - 1)

        max_x = len(grid[0])
        max_y = len(grid)

        dirs = {">": (1, 0), "v": (0, 1), "^": (0, -1), "<": (-1, 0)}
        opposite = {"<": ">", ">": "<", "v": "^", "^": "v"}

        to_visit = [(0, ">", s), (0, "v", s)]

        seen = set()

        while to_visit:
            cl, cd, cp = heapq.heappop(to_visit)
            if (cp, cd) in seen:
                continue

            seen.add((cp, cd))
            path_len = len(cd)

            for d in dirs:
                n_p = (cp[0] + dirs[d][0], cp[1] + dirs[d][1])
                if (
                    not 0 <= n_p[0] < max_x  # out of grid range
                    or not 0 <= n_p[1] < max_y
                    or (d == cd[-1] and path_len == max_l)  # path longer
                    or (d != cd[-1] and path_len < min_l)  # path shorter
                    or cd[-1] == opposite[d]  # turning back
                ):
                    continue
                if d == cd[-1]:
                    nd = cd + d
                else:
                    nd = d
                if (n_p, nd) in seen:
                    continue
                if n_p == e and len(nd) >= min_l:
                    return cl + grid[n_p[1]][n_p[0]]
                heapq.heappush(to_visit, (cl + grid[n_p[1]][n_p[0]], nd, n_p))
        
    def partie1():
        grid = [list(map(int, l.strip())) for l in open(filename)]

        print(f"Réponse jour 17 partie 1 : {get_min(grid)}")
    
    def partie2():
        grid = [list(map(int, l.strip())) for l in open(filename)]

        print(f"Réponse jour 17 partie 2 : {get_min(grid, 4, 10)}")
    
    partie1()
    partie2()
    
j17()
