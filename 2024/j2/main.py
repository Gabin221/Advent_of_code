with open("../Input/j2.txt","r",encoding="utf8") as file :
    lignes = [line.strip() for line in file.readlines()]


def croissant(liste):
    for i in range(len(liste)-1):
        if not liste[i] <= liste[i+1]:
            return False
    return True


def decroissant(liste):
    for i in range(len(liste)-1):
        if not liste[i] >= liste[i+1]:
            return False
    return True


def rapport_sur(liste):
	sur = False
	for i in range(1, len(liste)):
		if abs(liste[i] - liste[i - 1]) >= 1 and abs(liste[i] - liste[i - 1]) <= 3 and (decroissant(liste) or croissant(liste)):
			sur = True
		else:
			sur = False
			break
	
	return sur


def partie1():
	rapports_surs = 0
	rapports = []
	
	for ligne in lignes:
		rapport = ligne.split(" ")
		for i in range(len(rapport)):
			rapport[i] = int(rapport[i])

		rapports.append(rapport)

	for liste in rapports:
		if rapport_sur(liste):
			rapports_surs += 1

	print(f"La réponse de la partie 1 est {rapports_surs}")


def partie2():
	score = 0

	print(f"La réponse de la partie 2 est {score}")


if __name__ == "__main__":
	partie1()
	partie2()
