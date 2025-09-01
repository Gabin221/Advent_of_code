package aoc

import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.Paths

fun readInput(fileName: String): List<String> {
    val path: Path = Paths.get("").resolve(fileName)
    return Files.readAllLines(path)
}

fun part1(): Any {
    val moves = readInput("input.txt")[0]

    var x = 0
    var y = 0
    val visited = mutableSetOf(Pair(x, y))

    for (move in moves) {
        when (move) {
            '^' -> y += 1
            'v' -> y -= 1
            '>' -> x += 1
            '<' -> x -= 1
        }
        visited.add(Pair(x, y))
    }

    return visited.size
}

fun part2(): Any {
    val moves = readInput("input.txt")[0]

    var santaX = 0
    var santaY = 0
    var roboX = 0
    var roboY = 0

    val visited = mutableSetOf(Pair(0, 0))

    for ((index, move) in moves.withIndex()) {
        if (index % 2 == 0) {
            when (move) {
                '^' -> santaY += 1
                'v' -> santaY -= 1
                '>' -> santaX += 1
                '<' -> santaX -= 1
            }
            visited.add(Pair(santaX, santaY))
        } else {
            when (move) {
                '^' -> roboY += 1
                'v' -> roboY -= 1
                '>' -> roboX += 1
                '<' -> roboX -= 1
            }
            visited.add(Pair(roboX, roboY))
        }
    }

    return visited.size
}

fun main() {
    println("Part 1: ${part1()}")
    println("Part 2: ${part2()}")
}
