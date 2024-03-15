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

def j19():
    filename = "../Input/inputj19.txt"
    
    def get_combs(state, rules, ranges={"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}):
        if state == "R":
            return 0
        elif state == "A":
            x_s = ranges["x"]
            m_s = ranges["m"]
            a_s = ranges["a"]
            s_s = ranges["s"]

            return (x_s[1] - x_s[0] + 1) * (m_s[1] - m_s[0] + 1) * (a_s[1] - a_s[0] + 1) * (s_s[1] - s_s[0] + 1)

        total = 0
        for pred in rules[state].split(","):
            if not ":" in pred:
                total += get_combs(pred, rules, ranges)
            else:
                p = pred.split(":")
                new_range = deepcopy(ranges)

                new_val = int(p[0][2:])
                c_range = ranges[p[0][0]]

                if c_range[0] < new_val < c_range[1]:
                    if p[0][1] == "<":
                        new_range[p[0][0]] = (c_range[0], new_val - 1)
                        ranges[p[0][0]] = (new_val, c_range[1])
                    else:
                        new_range[p[0][0]] = (new_val + 1, c_range[1])
                        ranges[p[0][0]] = (c_range[0], new_val)
                    total += get_combs(p[1], rules, new_range)
        return total
        
    def partie1():
        ps = open(filename).read().split("\n\n")

        rules = {}

        for l in ps[0].splitlines():
            p = l.split("{")
            rules[p[0]] = p[1][:-1]

        A = 0
        for p in ps[1].splitlines():
            state = "in"
            vals = {}
            for c in p[1:-1].split(","):
                vals[c.split("=")[0]] = int(c.split("=")[1])
            while state not in "AR":
                current_cond = rules[state].split(",")
                for pred in current_cond:
                    if ":" in pred:
                        evs = pred.split(":")
                        if eval('vals["' + evs[0][0] + '"]' + "".join(evs[0][1:])):
                            state = evs[1]
                            break
                    else:
                        state = pred

                if state == "A":
                    A += sum(vals.values())
                    break
                elif state == "R":
                    break

        print(f"Réponse jour 19 partie 1 : {A}")
    
    def partie2():
        ps = open(filename).read().split("\n\n")

        rules = {}

        for l in ps[0].splitlines():
            p = l.split("{")
            rules[p[0]] = p[1][:-1]

        print(f"Réponse jour 19 partie 2 : {get_combs('in', rules)}")
    
    partie1()
    partie2()
    
j19()
