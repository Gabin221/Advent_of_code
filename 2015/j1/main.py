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

    stair = 0

    for i in input_name[0]:
        if i == "(":
            stair += 1
        if i == ")":
            stair -=1

    return stair

def part2():
    input_name = read_input("input.txt")

    position = 0
    stair = 0

    for i in input_name[0]:
        position += 1
        if i == "(":
            stair += 1
        if i == ")":
            stair -=1

        if stair == -1:
            return position


def main():
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

if __name__ == "__main__":
    main()
