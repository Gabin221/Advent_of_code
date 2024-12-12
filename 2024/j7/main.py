from itertools import product

with open("../Input/j7.txt","r",encoding="utf8") as file :
	lignes = [line.strip() for line in file.readlines()]


def evaluer_equation(nombres, operateurs):
	"""Évalue une équation donnée en appliquant les opérateurs dans l'ordre."""
	resultat = nombres[0]
	for i in range(len(operateurs)):
		if operateurs[i] == '+':
			resultat += nombres[i + 1]
		elif operateurs[i] == '*':
			resultat *= nombres[i + 1]
		elif operateurs[i] == '|':
			resultat = int(str(resultat) + str(nombres[i + 1]))
	return resultat


def partie1():
	answer = 0

	for ligne in lignes:
		resultat_attendu = int(ligne.split(":")[0])
		nombres = list(map(int, ligne.split(":")[1].strip().split()))
		
		nb_operateurs = len(nombres) - 1
		combinaisons_operateurs = product("+-*", repeat=nb_operateurs)
		
		equation_valide = False
		for operateurs in combinaisons_operateurs:
			if evaluer_equation(nombres, operateurs) == resultat_attendu:
				equation_valide = True
				break
		
		if equation_valide:
			answer += resultat_attendu

	print(f"La réponse de la partie 1 est {answer}")


def partie2():
	answer = 0
	compteur = 0

	for ligne in lignes:
		compteur += 1
		print(f"Progression: {round(compteur*100/len(lignes), 2)}%")
		resultat_attendu = int(ligne.split(":")[0])
		nombres = list(map(int, ligne.split(":")[1].strip().split()))
		
		nb_operateurs = len(nombres) - 1
		combinaisons_operateurs = product("+-*-|", repeat=nb_operateurs)
		
		equation_valide = False
		for operateurs in combinaisons_operateurs:
			try:
				if evaluer_equation(nombres, operateurs) == resultat_attendu:
					equation_valide = True
					break
			except ValueError:
	
				continue
		
		if equation_valide:
			answer += resultat_attendu

	print(f"La réponse de la partie 2 est {answer}")


if __name__ == "__main__":
	partie1()
	partie2()
