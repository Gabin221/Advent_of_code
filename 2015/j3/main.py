#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

def read_input(file_name: str):
    path = Path(__file__).resolve().parent / file_name
    with path.open("r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

def part1():
    with open("input.txt") as f:
        moves = f.read().strip()

    x, y = 0, 0
    visited = {(x, y)}

    for move in moves:
        if move == "^":
            y += 1
        elif move == "v":
            y -= 1
        elif move == ">":
            x += 1
        elif move == "<":
            x -= 1
        visited.add((x, y))

    return len(visited)

def part2():
    with open("input.txt") as f:
        moves = f.read().strip()

    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0

    visited = {(0, 0)}

    for idx, move in enumerate(moves):
        if idx % 2 == 0:
            if move == "^":
                santa_y += 1
            elif move == "v":
                santa_y -= 1
            elif move == ">":
                santa_x += 1
            elif move == "<":
                santa_x -= 1
            visited.add((santa_x, santa_y))
        else:
            if move == "^":
                robo_y += 1
            elif move == "v":
                robo_y -= 1
            elif move == ">":
                robo_x += 1
            elif move == "<":
                robo_x -= 1
            visited.add((robo_x, robo_y))

    return len(visited)

def main():
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

if __name__ == "__main__":
    main()
