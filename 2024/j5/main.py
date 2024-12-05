with open("../Input/j5.txt","r",encoding="utf8") as file :
	lignes = [line.strip() for line in file.readlines()]


def check_order(pages, regles):
        for reg in regles:
            liste = reg.split("|")
            if liste[0] in pages and liste[1] in pages:
                index1 = pages.index(liste[0])
                index2 = pages.index(liste[1])
                if index1 > index2:
                    pages[index1], pages[index2] = pages[index2], pages[index1]
                    check_order(pages, regles)
        return pages


def partie1():
	answer = 0
	regles = []
	mises_a_jour = []
	good_maj = []

	for ligne in lignes:
		if "|" in ligne:
			regles.append(ligne)
		if "," in ligne:
			mises_a_jour.append(ligne)

	for mise in mises_a_jour:
		valide = True
		pages = mise.split(",")
		for reg in regles:
			liste = reg.split("|")
			if liste[0] in pages and liste[1] in pages:
				if pages.index(liste[0]) > pages.index(liste[1]):
					valide = False
					break
		if valide:
			good_maj.append(mise)

	for good in good_maj:
		nbr = good.split(",")
		answer += int(nbr[len(nbr) // 2])

	print(f"La réponse de la partie 1 est {answer}")


def partie2():
    answer = 0
    regles = []
    mises_a_jour = []

    for ligne in lignes:
        if "|" in ligne:
            regles.append(ligne)
        if "," in ligne:
            mises_a_jour.append(ligne)

    for mise in mises_a_jour:
        pages = mise.split(",")
        original_pages = list(pages)
        corrected_pages = check_order(pages, regles)

        if corrected_pages != original_pages:
            middle_index = len(corrected_pages) // 2
            answer += int(corrected_pages[middle_index])

    print(f"La réponse de la partie 2 est {answer}")


if __name__ == "__main__":
	partie1()
	partie2()
