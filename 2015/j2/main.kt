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

    var foot = 0

    for (i in inputName) {
        val values = i.split("x").map { it.toInt() }.sorted()

        val additionnal = values[0].toInt()*values[1].toInt()
        val surfaces = 2*(values[0].toInt()*values[1].toInt() + values[0].toInt()*values[2].toInt() + values[1].toInt()*values[2].toInt())

        foot += additionnal + surfaces
    }

    return foot
}

fun part2(): Any {
    val inputName = readInput("input.txt")

    var foot = 0

    for (i in inputName) {
        val values = i.split("x").map { it.toInt() }.sorted()

        val shortest_distance = 2*(values[0].toInt() + values[1].toInt())
        val perfect_bow = values[0].toInt()*values[1].toInt()*values[2].toInt()

        foot += shortest_distance + perfect_bow
    }

    return foot
}

fun main() {
    println("Part 1: ${part1()}")
    println("Part 2: ${part2()}")
}

