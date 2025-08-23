package aoc

import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.Paths

fun readInput(fileName: String): List<String> {
    val path: Path = Paths.get("").resolve(fileName)
    return Files.readAllLines(path)
}

fun part1(): Any {
    val inputName = readInput("input.txt")[0]

    var stair = 0

    for (i in inputName) {
        if (i.equals('(')) {
            stair += 1
        }
        if (i.equals(')')) {
            stair -= 1
        }
    }

    return stair
}

fun part2(): Any {
    val inputName = readInput("input.txt")[0]

    var stair = 0
    var position = 0

    for (i in inputName) {
        position += 1
        if (i.equals('(')) {
            stair += 1
        }
        if (i.equals(')')) {
            stair -= 1
        }

        if (stair.equals(-1)) {
            break
        }
    }

    return position
}

fun main() {
    println("Part 1: ${part1()}")
    println("Part 2: ${part2()}")
}

