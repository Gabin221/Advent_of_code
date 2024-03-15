import sys
from utils import *
import numpy as np

sys.setrecursionlimit(999999)

def j9():
    filename = "../Input/inputj9.txt"
        
    def partie1():
        def read_input(puzzle):
            with open(filename, 'r') as f:
                data = f.read().splitlines()
            return data

        data = []
        for line in read_input('9'):
            int_list = [int(i) for i in line.split()]
            data.append(int_list)

        def first_part(int_list):
            pattern = np.array(int_list, dtype=int).reshape(1, -1)

            final_number = 0

            while not np.all(np.diff(pattern) == 0):

                final_number += pattern[-1, -1]
                pattern = np.diff(pattern)

            else:
                final_number += pattern[-1, -1]

            return final_number

        result_1 = 0
        for i in data:
            result_1 += first_part(i)
        print(f"Réponse jour 9 partie 1 : {result_1}")
    
    def partie2():
        def read_input(puzzle):
            with open(filename, 'r') as f:
                data = f.read().splitlines()
            return data

        data = []
        for line in read_input('9'):
            int_list = [int(i) for i in line.split()]
            data.append(int_list)
            
        def second_part(int_list):
            pattern = np.array(int_list, dtype=int).reshape(1, -1)

            final_number = 0 
            sign = 1

            while not np.all(np.diff(pattern) == 0):

                final_number += pattern[0, 0] * sign
                sign *= -1
                pattern = np.diff(pattern)

            else:
                # still add the first number
                final_number += pattern[0, 0] * sign
                sign *= -1

            return final_number

        result_2 = 0
        for i in data:
            result_2 += second_part(i)
        print(f"Réponse jour 9 partie 2 : {result_2}")
    
    partie1()
    partie2()
    
j9()