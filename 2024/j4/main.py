with open("../Input/j4.txt","r",encoding="utf8") as file :
	lignes = [line.strip() for line in file.readlines()]


def lignes_matrice(matrice):
	compteur = 0

	for ligne in matrice:
		compteur += ligne.count("XMAS")
		compteur += ligne.count("SAMX")

	return compteur


def colonnes_matrice(matrice):
	compteur = 0

	for i in range(len(matrice) - 3):
		for j in range(len(matrice[i])):
			if matrice[i][j] == "X":
				if matrice[i + 1][j] == "M" and matrice[i + 2][j] == "A" and matrice[i + 3][j] == "S":
					compteur += 1
			
			if matrice[i][j] == "S":
				if matrice[i + 1][j] == "A" and matrice[i + 2][j] == "M" and matrice[i + 3][j] == "X":
					compteur += 1
	
	return compteur


def diagonales_matrice(matrice):
	compteur = 0
	
	for i in range(len(matrice) - 3):
		for j in range(len(matrice[i]) - 3):
			if matrice[i][j] == "X" and matrice[i + 1][j + 1] == "M" and matrice[i + 2][j + 2] == "A" and matrice[i + 3][j + 3] == "S":
					compteur += 1

			if matrice[i][j] == "S" and matrice[i + 1][j + 1] == "A" and matrice[i + 2][j + 2] == "M" and matrice[i + 3][j + 3] == "X":
					compteur += 1

	for i in range(3, len(matrice)):
		for j in range(len(matrice[i]) - 3):
			if matrice[i][j] == "X" and matrice[i - 1][j + 1] == "M" and matrice[i - 2][j + 2] == "A" and matrice[i - 3][j + 3] == "S":
					compteur += 1

			if matrice[i][j] == "S" and matrice[i - 1][j + 1] == "A" and matrice[i - 2][j + 2] == "M" and matrice[i - 3][j + 3] == "X":
					compteur += 1

	return compteur


def nbr_x():
	matrice = [ligne for ligne in lignes]
	compteur = 0
	
	for i in range(1, len(matrice) - 1):
		for j in range(1, len(matrice[i]) - 1):
			if matrice[i][j] == "A":
				if matrice[i - 1][j - 1] == "M" and matrice[i + 1][j + 1] == "S" and matrice[i + 1][j - 1] == "M" and matrice[i - 1][j + 1] == "S":
					compteur += 1
				if matrice[i - 1][j - 1] == "M" and matrice[i + 1][j + 1] == "S" and matrice[i + 1][j - 1] == "S" and matrice[i - 1][j + 1] == "M":
					compteur += 1
				if matrice[i - 1][j - 1] == "S" and matrice[i + 1][j + 1] == "M" and matrice[i + 1][j - 1] == "S" and matrice[i - 1][j + 1] == "M":
					compteur += 1
				if matrice[i - 1][j - 1] == "S" and matrice[i + 1][j + 1] == "M" and matrice[i + 1][j - 1] == "M" and matrice[i - 1][j + 1] == "S":
					compteur += 1
	
	return compteur


def partie1():
	answer = 0
	matrice = [ligne for ligne in lignes]

	answer += lignes_matrice(matrice)
	answer += colonnes_matrice(matrice)
	answer += diagonales_matrice(matrice)

	print(f"La réponse de la partie 1 est {answer}")


def partie2():
	answer = nbr_x()

	print(f"La réponse de la partie 2 est {answer}")


if __name__ == "__main__":
	partie1()
	partie2()
