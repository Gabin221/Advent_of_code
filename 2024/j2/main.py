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


def rapport_sur_partie1(liste):
	sur = False
	for i in range(1, len(liste)):
		if abs(liste[i] - liste[i - 1]) >= 1 and abs(liste[i] - liste[i - 1]) <= 3 and (decroissant(liste) or croissant(liste)):
			sur = True
		else:
			sur = False
			break
	
	return sur


def rapport_sur_partie2(liste):
	sur = False
	for i in range(1, len(liste)):
		if abs(liste[i] - liste[i - 1]) < 1 or abs(liste[i] - liste[i - 1]) > 3:
			break
	else:
		if croissant(liste) or decroissant(liste):
			return True
	
	for i in range(len(liste)):
		new_liste = liste[:i] + liste[i+1:]
		sur = True
		for j in range(1, len(new_liste)):
			if abs(new_liste[j] - new_liste[j - 1]) < 1 or abs(new_liste[j] - new_liste[j - 1]) > 3:
				sur = False
				break
		if sur and (croissant(new_liste) or decroissant(new_liste)):
			return True

	return False


def partie1():
	answer = 0
	rapports = []
	
	for ligne in lignes:
		rapport = ligne.split(" ")
		for i in range(len(rapport)):
			rapport[i] = int(rapport[i])

		rapports.append(rapport)

	for liste in rapports:
		if rapport_sur_partie1(liste):
			answer += 1

	print(f"La réponse de la partie 1 est {answer}")


def partie2():
	answer = 0
	rapports = []
	
	for ligne in lignes:
		rapport = ligne.split(" ")
		for i in range(len(rapport)):
			rapport[i] = int(rapport[i])

		rapports.append(rapport)

	for liste in rapports:
		if rapport_sur_partie2(liste):
			answer += 1

	print(f"La réponse de la partie 2 est {answer}")


if __name__ == "__main__":
	partie1()
	partie2()
