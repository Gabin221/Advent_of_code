import sys
from utils import *

sys.setrecursionlimit(999999)

def j22():
    filename = "../Input/inputj22.txt"
    
    def drop(bricks, eraly=False):
        dropped = set()
        seen = set()

        for i in range(len(bricks)):
            pts = bricks[i]

            while True:
                new_pts = {(p[0], p[1], p[2] - 1) for p in pts}
                if all(p not in seen and p[2] > 0 for p in new_pts):
                    bricks[i] = new_pts
                    pts = new_pts
                    dropped.add(i)
                    if eraly:
                        return 1
                else:
                    break

            seen.update(pts)

        return len(dropped)
        
    def partie1():
        bricks = []

        for l in open(filename):
            p = list(map(lambda x: tuple(map(int, x.split(","))), l.strip().split("~")))
            b = set([p[0], p[1]])

            idx_deltas = [c1 != c2 for c1, c2 in zip(p[0], p[1])]
            if any(idx_deltas):
                assert sum(idx_deltas) == 1
                idx = idx_deltas.index(True)
                for val in range(min(p[0][idx], p[1][idx]), max(p[0][idx], p[1][idx])):
                    b.add(tuple(val if i == idx else c for i, c in enumerate(p[0])))
            bricks.append(b)

        bricks.sort(key=lambda x: min(p[2] for p in x))

        drop(bricks)
        total = 0

        for i in range(len(bricks)):
            new_bricks = bricks.copy()
            del new_bricks[i]
            total += not drop(new_bricks, True)

        print(f"Réponse jour 22 partie 1 : {total}")
    
    def partie2():
        bricks = []

        for l in open(filename):
            p = list(map(lambda x: tuple(map(int, x.split(","))), l.strip().split("~")))
            b = set([p[0], p[1]])

            idx_deltas = [c1 != c2 for c1, c2 in zip(p[0], p[1])]
            if any(idx_deltas):
                assert sum(idx_deltas) == 1
                idx = idx_deltas.index(True)
                for val in range(min(p[0][idx], p[1][idx]), max(p[0][idx], p[1][idx])):
                    b.add(tuple(val if i == idx else c for i, c in enumerate(p[0])))
            bricks.append(b)

        bricks.sort(key=lambda x: min(p[2] for p in x))

        drop(bricks)
        total = 0

        for i in range(len(bricks)):
            new_bricks = bricks.copy()
            del new_bricks[i]
            total += drop(new_bricks)
            
        print(f"Réponse jour 22 partie 2 : {total}")
    
    partie1()
    partie2()
    
j22()
