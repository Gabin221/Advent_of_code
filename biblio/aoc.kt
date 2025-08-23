package biblio

import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.Paths

fun readInput(fileName: String): List<String> {
    val path: Path = Paths.get("").resolve(fileName)
    return Files.readAllLines(path)
}
