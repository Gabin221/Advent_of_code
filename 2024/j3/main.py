import re

with open("../Input/j3.txt","r",encoding="utf8") as file :
    lignes = [line.strip() for line in file.readlines()]

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"


def partie1():
	answer = 0

	for ligne in lignes:
		matches = re.findall(pattern, ligne)

		for match in matches:
			answer += int(match[0])*int(match[1])

	print(f"La réponse de la partie 1 est {answer}")


def partie2():
	answer = 0
	fichier = ""

	for ligne in lignes:
		fichier += ligne

	elements = fichier.split("do()")

	for element in elements:
		element_reduit = element[:element.find("don't()")]

		matches = re.findall(pattern, element_reduit)

		for match in matches:
			answer += int(match[0])*int(match[1])


	print(f"La réponse de la partie 2 est {answer}")


if __name__ == "__main__":
	partie1()
	partie2()
