with open("../Input/j1.txt","r",encoding="utf8") as file :
    lignes = [line.strip() for line in file.readlines()]


def partie1():
	liste_gauche = []
	liste_droite = []

	dist_totale = 0

	for ligne in lignes:
		nombres = ligne.split("   ")
		liste_gauche.append(nombres[0])
		liste_droite.append(nombres[1])

	liste_gauche.sort()
	liste_droite.sort()

	for i in range(len(liste_gauche)):
		dist_totale += abs(int(liste_gauche[i]) - int(liste_droite[i]))

	print(f"La réponse de la partie 1 est {dist_totale}")


def partie2():
	pass


if __name__ == "__main__":
	partie1()
	partie2()
