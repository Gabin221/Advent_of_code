with open("../Input/j4.txt","r",encoding="utf8") as file :
	lignes = [line.strip() for line in file.readlines()]

sequences = ["XMAS", "SAMX"]


def lignes_matrice(matrice):
    compteur = 0
    for ligne in matrice:
        for seq in sequences:
            compteur += sum(1 for i in range(len(ligne) - 3) if ligne[i:i+4] == seq)
    return compteur


def colonnes_matrice(matrice):
    compteur = 0
    lignes, colonnes = len(matrice), len(matrice[0])

    for j in range(colonnes):
        colonne = [matrice[i][j] for i in range(lignes)]
        for seq in sequences:
            compteur += sum(1 for i in range(len(colonne) - 3) if "".join(colonne[i:i+4]) == seq)
    return compteur


def diagonales_matrice(matrice):
    compteur = 0
    lignes, colonnes = len(matrice), len(matrice[0])

    for i in range(lignes - 3):
        for j in range(colonnes - 3):
            diagonale = "".join([matrice[i + k][j + k] for k in range(4)])
            for seq in sequences:
                if diagonale == seq:
                    compteur += 1

    for i in range(3, lignes):
        for j in range(colonnes - 3):
            diagonale = "".join([matrice[i - k][j + k] for k in range(4)])
            for seq in sequences:
                if diagonale == seq:
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
    answer = 0

    print(f"La réponse de la partie 2 est {answer}")


if __name__ == "__main__":
    partie1()
    partie2()
