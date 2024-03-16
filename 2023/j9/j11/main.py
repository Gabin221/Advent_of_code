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

def j11():
    filename = "../Input/inputj11.txt"     
       
    def partie1():
        with open(filename) as fin:
            lines = fin.read().strip().split("\n")

        n, m = len(lines), len(lines[0])

        coords = []
        for i in range(n):
            for j in range(m):
                if lines[i][j] == "#":
                    coords.append((i, j))

        N = len(coords)

        empty_row = [all([lines[i][j] == "." for j in range(m)]) for i in range(n)]
        empty_col = [all([lines[i][j] == "." for i in range(n)]) for j in range(m)]


        def dist(a, b):
            i1, j1 = a
            i2, j2 = b

            i1, i2 = min(i1, i2), max(i1, i2)
            j1, j2 = min(j1, j2), max(j1, j2)

            ans = 0
            for i in range(i1, i2):
                ans += 1
                if empty_row[i]:
                    ans += 1
            for j in range(j1, j2):
                ans += 1
                if empty_col[j]:
                    ans += 1

            return ans


        ans = 0
        for idx1 in range(N):
            for idx2 in range(idx1+1, N):
                d = dist(coords[idx1], coords[idx2])
                ans += d

        print(f"Réponse jour 11 partie 1 : {ans}")
    
    def partie2():
        with open(filename) as fin:
            lines = fin.read().strip().split("\n")

        n, m = len(lines), len(lines[0])

        coords = []
        for i in range(n):
            for j in range(m):
                if lines[i][j] == "#":
                    coords.append((i, j))

        N = len(coords)

        empty_row = [all([lines[i][j] == "." for j in range(m)]) for i in range(n)]
        empty_col = [all([lines[i][j] == "." for i in range(n)]) for j in range(m)]


        def dist(a, b):
            i1, j1 = a
            i2, j2 = b

            i1, i2 = min(i1, i2), max(i1, i2)
            j1, j2 = min(j1, j2), max(j1, j2)

            ans = 0
            for i in range(i1, i2):
                ans += 1
                if empty_row[i]:
                    ans += 10**6 - 1
            for j in range(j1, j2):
                ans += 1
                if empty_col[j]:
                    ans += 10**6 - 1

            return ans


        ans = 0
        for idx1 in range(N):
            for idx2 in range(idx1+1, N):
                d = dist(coords[idx1], coords[idx2])
                ans += d

        print(f"Réponse jour 11 partie 2 : {ans}")
    
    partie1()
    partie2()
    
j11()
