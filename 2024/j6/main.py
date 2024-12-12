with open("../Input/j6.txt", "r", encoding="utf8") as file:
	lignes = [line.strip() for line in file.readlines()]


def partie1():
	answer = 0
	matrice = [list(ligne) for ligne in lignes]
	directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
	tourne_droite = {"^": ">", ">": "v", "v": "<", "<": "^"}
	visited = set()

	for ligne in range(len(matrice)):
		for colonne in range(len(matrice[ligne])):
			if matrice[ligne][colonne] in directions:
				position = (ligne, colonne)
				direction = matrice[ligne][colonne]
				break

	while True:
		visited.add(position)
		matrice[position[0]][position[1]] = "X"

		delta = directions[direction]
		next_position = (position[0] + delta[0], position[1] + delta[1])

		if not (0 <= next_position[0] < len(matrice) and 0 <= next_position[1] < len(matrice[0])):
			break

		if matrice[next_position[0]][next_position[1]] == "#":
			direction = tourne_droite[direction]
		else:
			position = next_position

	answer += len(visited)
	print(f"La réponse de la partie 1 est {answer}")


def partie2():
    matrice = [list(ligne) for ligne in lignes]
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    tourne_droite = {"^": ">", ">": "v", "v": "<", "<": "^"}
    possible_positions = []

    # Trouver la position et direction initiales du garde
    for ligne in range(len(matrice)):
        for colonne in range(len(matrice[ligne])):
            if matrice[ligne][colonne] in directions:
                guard_start = (ligne, colonne)
                guard_direction = matrice[ligne][colonne]
                break

    # Tester toutes les positions accessibles (".") comme potentiel obstacle
    for ligne in range(len(matrice)):
        for colonne in range(len(matrice[ligne])):
            if matrice[ligne][colonne] != "." or (ligne, colonne) == guard_start:
                continue

            matrice[ligne][colonne] = "#"  # Ajouter une obstruction temporaire
            position = guard_start
            direction = guard_direction
            visited = {}
            loop_detected = False
            steps = 0  # Compteur pour éviter des boucles infinies

            while True:
                # Utiliser un tuple (position, direction) pour détecter les boucles
                state = (position, direction)
                if state in visited:
                    loop_detected = True
                    break

                visited[state] = steps
                delta = directions[direction]
                next_position = (position[0] + delta[0], position[1] + delta[1])

                # Si le garde sort des limites
                if not (0 <= next_position[0] < len(matrice) and 0 <= next_position[1] < len(matrice[0])):
                    break

                # Si le garde rencontre un obstacle, il tourne
                if matrice[next_position[0]][next_position[1]] == "#":
                    direction = tourne_droite[direction]
                else:
                    position = next_position

                steps += 1
                if steps > 10000:  # Limite de sécurité
                    break

            if loop_detected:
                possible_positions.append((ligne, colonne))

            matrice[ligne][colonne] = "."  # Restaurer l'état initial

    print(f"La réponse de la partie 2 est {len(possible_positions)}")


if __name__ == "__main__":
	partie1()
	partie2()
