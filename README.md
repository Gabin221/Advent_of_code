# Advent-of-code

Ce dépôt contient mes solutions aux différents **Advent of Code**, implémentées en **Python**, **C++** et **Kotlin**.  
Chaque année/jour est organisé dans une arborescence claire avec des fichiers d’entrée (`input_part1.txt`, `input_part2.txt`) et un squelette de code identique dans chaque langage.

---

## Structure du projet

Advent_of_code/
├── data/ # script copier chaque jour
│ ├── main.py
│ └── Main.kt
├── 2015/
│ └── j1/ # Jour 1 - Année 2015
│ ├── main.py
│ ├── Main.kt
│ ├── input_part1.txt
│ └── input_part2.txt
│ └── j2/ # Jour 2 - Année 2015
│ ├── main.py
│ ├── Main.kt
│ ├── input_part1.txt
│ └── input_part2.txt

## Utilisation

### Python

```bash
cd 2015/j1
python3 main.py
```

### Kotlin

```bash
cd 2015/j1
kotlinc Main.kt -include-runtime -d main.jar && java -jar main.jar
```

### Langages utilisés : Python, Kotlin
