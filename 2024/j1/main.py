with open("../Input/j1.txt","r",encoding="utf8") as file :
    lignes = [line.strip() for line in file.readlines()]


liste_gauche = []
liste_droite = []

for ligne in lignes:
	nombres = ligne.split("   ")
	liste_gauche.append(nombres[0])
	liste_droite.append(nombres[1])


def partie1():
	answer = 0

	liste_gauche.sort()
	liste_droite.sort()

	for i in range(len(liste_gauche)):
		answer += abs(int(liste_gauche[i]) - int(liste_droite[i]))

	print(f"La réponse de la partie 1 est {answer}")


def partie2():
	answer = 0

	for i in liste_gauche:
		frequence = 0
		for j in liste_droite:
			if int(i) == int(j):
				frequence += 1
		
		answer += frequence * int(i)

	print(f"La réponse de la partie 2 est {answer}")


if __name__ == "__main__":
	partie1()
	partie2()
