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

def j25():
    filename = "Input/inputj25.txt"
    input = []
    with open(filename) as file:
        input = [line.strip() for line in file.readlines()]
        
    def partie1():
        graph = networkx.Graph()

        for l in open(filename):
            src, dst = l.strip().split(": ")

            for n in dst.split():
                graph.add_edge(src, n)

        _, partitions = networkx.stoer_wagner(graph)

        print(f"Réponse jour 25 partie 1 : {len(partitions[0]) * len(partitions[1])}")
    
    def partie2():
        print("Réponse jour 25 partie 2 : il n'y a eu qu'une seule partie le 25")
    
    partie1()
    partie2()
    
j25()
