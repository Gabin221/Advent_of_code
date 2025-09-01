package aoc

import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.Paths

fun readInput(fileName: String): List<String> {
    val path: Path = Paths.get("").resolve(fileName)
    return Files.readAllLines(path)
}

fun part1(): Any {
    val inputName = readInput("input.txt")

    return 0
}

fun part2(): Any {
    val inputName = readInput("input.txt")

    return 0
}

fun main() {
    println("Part 1: ${part1()}")
    println("Part 2: ${part2()}")
}

