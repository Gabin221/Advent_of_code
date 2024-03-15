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

def j20():
    filename = "../Input/inputj20.txt"

    class Module:
        def __init__(self, l) -> None:
            p = l.split(" -> ")
            self.name = p[0]
            if p[0][0] in "%&":
                self.type = p[0][0]
                self.name = "".join(p[0][1:])
            else:
                self.type = ""
                self.name = p[0]
            self.next = p[1].split(", ")
            self.state = False
        
    def partie1():
        modules = {}
        for l in open(filename).read().splitlines():
            m = Module(l)

            modules[m.name] = m

        for m in modules:
            if modules[m].type == "&":
                modules[m].input = {}
                for d in modules:
                    if m in modules[d].next:
                        modules[m].input[d] = False

        high = 0
        lows = 0

        for _ in range(1000):
            to_send = [("broadcaster", False)]

            while to_send:
                src, sig = to_send.pop(0)

                dst = []
                output = sig

                if sig:
                    high += 1
                else:
                    lows += 1


                if src in modules and modules[src].type == "":
                    dst = modules[src].next
                elif src in modules and modules[src].type == "%" and not sig:
                    output = modules[src].state = not modules[src].state
                    dst = modules[src].next
                elif src in modules and modules[src].type == "&":
                    output = not all(modules[src].input.values())
                    dst = modules[src].next

                for m in dst:
                    to_send.append((m, output))
                    if m in modules and modules[m].type == "&":
                        modules[m].input[src] = output

        print(f"Réponse jour 20 partie 1 : {high * lows}")
    
    def partie2():
        modules = {}
        for l in open(filename).read().splitlines():
            m = Module(l)

            modules[m.name] = m
            if "rx" in m.next:
                main_module = m.name

        for m in modules:
            if modules[m].type == "&":
                modules[m].input = {}
                for d in modules:
                    if m in modules[d].next:
                        modules[m].input[d] = False

        cycles = {m:0 for m in modules[main_module].input}

        cycle_cnt = 0
        while not all(cycles.values()):
            cycle_cnt += 1
            to_send = [("broadcaster", False)]

            while to_send:
                src, sig = to_send.pop(0)

                dst = []
                output = sig


                if src in modules and modules[src].type == "":
                    dst = modules[src].next
                elif src in modules and modules[src].type == "%" and not sig:
                    output = modules[src].state = not modules[src].state
                    dst = modules[src].next
                elif src in modules and modules[src].type == "&":
                    output = not all(modules[src].input.values())
                    dst = modules[src].next

                    if src == main_module and any(modules[src].input.values()):
                        for m in modules[src].input:
                            if modules[src].input[m]:
                                cycles[m] = cycle_cnt

                for m in dst:
                    to_send.append((m, output))
                    if m in modules and modules[m].type == "&":
                        modules[m].input[src] = output

        print(f"Réponse jour 20 partie 2 : {prod(cycles.values())}")
    
    partie1()
    partie2()
    
j20()
