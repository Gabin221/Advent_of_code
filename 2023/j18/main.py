import sys
from utils import *

sys.setrecursionlimit(999999)

def j18():
    filename = "../Input/inputj18.txt"
    
    def shoe_lace(points):
        res = sum(points[i - 1][0] * points[i][1] - points[i - 1][1] * points[i][0] for i in range(len(points)))
        return res // 2
        
    def partie1():
        polygon = [(0, 0)]

        deltas = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}

        p_cnt = 0

        for l in open(filename):
            ps = l.split()
            d = deltas[ps[0]]
            lp = polygon[-1]
            steps = int(ps[1])
            p_cnt += steps
            polygon.append((lp[0] + d[0] * steps, lp[1] + d[1] * steps))

        print(f"Réponse jour 18 partie 1 : {shoe_lace(polygon) + p_cnt // 2 + 1}")
    
    def partie2():
        polygon = [(0, 0)]

        deltas = {"0": (1, 0), "2": (-1, 0), "3": (0, -1), "1": (0, 1)}

        p_cnt = 0

        for l in open(filename):
            ps = l.split()

            d = deltas[ps[2][-2]]
            lp = polygon[-1]
            steps = int(ps[2][2:-2], 16)

            p_cnt += steps
            polygon.append((lp[0] + d[0] * steps, lp[1] + d[1] * steps))

        print(f"Réponse jour 18 partie 2 : {shoe_lace(polygon) + (p_cnt + 1) // 2 + 1}")
    
    partie1()
    partie2()
    
j18()
