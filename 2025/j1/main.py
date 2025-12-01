#!/usr/bin/env python3

from pathlib import Path

def read_input(file_name: str):
    path = Path(__file__).resolve().parent / file_name
    with path.open("r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]
    
def calculate_next_number(actual, rotate):
    return (actual + rotate)%100

def part1():
    input_name = read_input("input.txt")
    result = 0
    actual = 50

    for input in input_name:
        if "R" in input:
            rotate = int(str(input.split("R")[1]))
        else:
            rotate = - int(str(input.split("L")[1]))

        value = calculate_next_number(actual, rotate)
        actual = value
        if actual == 0:
            result += 1

    return result

def part2():
    input_name = read_input("input.txt")

    result = 0  
    actual = 50  

    for input in input_name:
        if "R" in input:
            rotate = int(input.split("R")[1])  
        else:
            rotate = -int(input.split("L")[1])  
        
        at_zero_before = (actual == 0)
        nombre_de_tours, actual = divmod(actual + rotate, 100)
        result += abs(nombre_de_tours)
        
        if rotate < 0: 
            at_zero_after = (actual == 0)
            result += at_zero_after - at_zero_before

    return result


def main():
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

if __name__ == "__main__":
    main()
