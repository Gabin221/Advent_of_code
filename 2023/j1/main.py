import re

def j1():
    filename = "../Input/inputj1.txt"
    input = []
    with open(filename) as file:
        input = [line.strip() for line in file.readlines()]
    
    # Dictionnaire pour convertir les chiffres en lettres en chiffres numériques
    chiffres_lettres = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", 
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    # Expression régulière pour rechercher les mots représentant des chiffres en lettres
    regex = re.compile("|".join(chiffres_lettres.keys()))

    # Fonction pour trouver et remplacer le premier et le dernier chiffre en lettres
    def remplacer_premier_et_dernier_chiffre(chaine):
        # Trouver toutes les occurrences de chiffres en lettres
        occurences = list(regex.finditer(chaine))
        
        if occurences:
            # Remplacer uniquement la première et la dernière occurrence
            if len(occurences) > 0:
                premier_chiffre = occurences[0]
                chaine = chaine[:premier_chiffre.start()] + chiffres_lettres[premier_chiffre.group(0)] + chaine[premier_chiffre.end():]
            
            if len(occurences) > 1:
                dernier_chiffre = occurences[-1]
                chaine = chaine[:dernier_chiffre.start()] + chiffres_lettres[dernier_chiffre.group(0)] + chaine[dernier_chiffre.end():]
        
        return chaine

    def partie1():
        total = 0
        for line in input:
            chaine = ""
            for i in line:
                if i.isdigit():
                    chaine += i
            if chaine:
                total += int(chaine[0] + chaine[-1])

        print(f"Réponse jour 1 partie 1 : {total}")
    
    def partie2():
        total = 0
        for line in input:
            # Remplacer le premier et le dernier chiffre en lettres par des chiffres
            line = remplacer_premier_et_dernier_chiffre(line)
            
            # Récupérer tous les chiffres de la ligne après remplacement
            chaine = ""
            for i in line:
                if i.isdigit():
                    chaine += i
            
            if chaine:  # S'assurer que la chaîne contient des chiffres
                total += int(chaine[0] + chaine[-1])
        
        print(f"Réponse jour 1 partie 2 : {total}")
    
    partie1()
    partie2()

j1()
