import sys
from utils import *
import networkx

sys.setrecursionlimit(999999)

def j25():
    filename = "../Input/inputj25.txt"
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
