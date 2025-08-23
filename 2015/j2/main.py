#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

def read_input(file_name: str):
    """Lit un fichier situé dans le même dossier que le script appelant"""
    path = Path(__file__).resolve().parent / file_name
    with path.open("r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

def part1():
    input_name = read_input("input.txt")

    foot = 0

    for i in input_name:
        values = list(map(int, i.split("x")))
        values.sort()

        additionnal = int(values[0])*int(values[1])
        surfaces = 2*(int(values[0])*int(values[1]) + int(values[0])*int(values[2]) + int(values[1])*int(values[2]))

        foot += additionnal + surfaces

    return foot

def part2():
    input_name = read_input("input.txt")

    foot = 0

    for i in input_name:
        values = list(map(int, i.split("x")))
        values.sort()

        shortest_distance = 2*(int(values[0]) + int(values[1]))
        perfect_bow = int(values[0])*int(values[1])*int(values[2])

        foot += shortest_distance + perfect_bow

    return foot

def main():
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

if __name__ == "__main__":
    main()
