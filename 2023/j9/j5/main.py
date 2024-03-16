import re
import sys
from utils import *

sys.setrecursionlimit(999999)

def j5():
    filename = "../Input/inputj5.txt"
    with open(filename, 'r') as f:
        input = f.read()
        
    def partie1():
        segments = input.split('\n\n')
        seeds = re.findall(r'\d+', segments[0])

        min_location = float('inf')
        for x in map(int, seeds):
            for seg in segments[1:]:
                for conversion in re.findall(r'(\d+) (\d+) (\d+)', seg):
                    destination, start, delta = map(int, conversion)
                    if x in range(start, start + delta):
                        x += destination - start
                        break

            min_location = min(x, min_location)
        print(f"Réponse jour 5 partie 1 : {min_location}")
    
    def partie2():
        segments = input.split('\n\n')
        intervals = []

        for seed in re.findall(r'(\d+) (\d+)', segments[0]):
            x1, dx = map(int, seed)
            x2 = x1 + dx
            intervals.append((x1, x2, 1))

        min_location = float('inf')
        while intervals:
            x1, x2, level = intervals.pop()
            if level == 8:
                min_location = min(x1, min_location)
                continue

            for conversion in re.findall(r'(\d+) (\d+) (\d+)', segments[level]):
                z, y1, dy = map(int, conversion)
                y2 = y1 + dy
                diff = z - y1
                if x2 <= y1 or y2 <= x1:    # no overlap
                    continue
                if x1 < y1:                 # split original interval at y1
                    intervals.append((x1, y1, level))
                    x1 = y1
                if y2 < x2:                 # split original interval at y2
                    intervals.append((y2, x2, level))
                    x2 = y2
                intervals.append((x1 + diff, x2 + diff, level + 1)) # perfect overlap -> make conversion and let pass to next nevel 
                break

            else:
                intervals.append((x1, x2, level + 1))
        print(f"Réponse jour 5 partie 2 : {min_location}")
    
    partie1()
    partie2()
    
j5()
