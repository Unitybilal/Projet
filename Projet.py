# Créé par Bilal Charkani élève de Terminale Lycée Paul langevin en Python 3.7 !
#Tuto : Grâce aux '#' cela va vous permettre de comprendre le code et de savoir de quoi il s'agit.

#Calculatrice


def calculatrice():
    operation = input("Choisissez une opération (+, -, *, /): ")
    nombre1 = float(input("Entrez le premier nombre: "))
    nombre2 = float(input("Entrez le deuxième nombre: "))

    if operation == '+':
        print(nombre1 + nombre2)
    elif operation == '-':
        print(nombre1 - nombre2)
    elif operation == '*':
        print(nombre1 * nombre2)
    elif operation == '/':
        if nombre2 != 0:
            print(nombre1 / nombre2)
        else:
            print("Division par zéro!")
    else:
        print("Opération non valide.")

calculatrice()

#Jeu de pendu

import random

def pendu():
    mots = ['python', 'programmation', 'ordinateur', 'intelligence', 'algorithmique']
    mot_a_deviner = random.choice(mots)
    lettre_trouvee = ['_'] * len(mot_a_deviner)
    essais = 7

    while essais > 0 and '_' in lettre_trouvee:
        print(" ".join(lettre_trouvee))
        lettre = input("Devinez une lettre: ").lower()

        if lettre in mot_a_deviner:
            for i in range(len(mot_a_deviner)):
                if mot_a_deviner[i] == lettre:
                    lettre_trouvee[i] = lettre
        else:
            essais -= 1
            print(f"Il vous reste {essais} essais.")

    if '_' not in lettre_trouvee:
        print("Félicitations! Vous avez deviné le mot.")
    else:
        print(f"Dommage! Le mot était {mot_a_deviner}.")

pendu()




#chiffrement et déchiffrement de César

def chiffrement_cesar(texte, decalage):
    texte_chiffre = ''
    for char in texte:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            texte_chiffre += chr((ord(char) - offset + decalage) % 26 + offset)
        else:
            texte_chiffre += char
    return texte_chiffre

def dechiffrement_cesar(texte_chiffre, decalage):
    return chiffrement_cesar(texte_chiffre, -decalage)

texte = input("Entrez le texte à chiffrer: ")
decalage = int(input("Entrez le décalage: "))

texte_chiffre = chiffrement_cesar(texte, decalage)
print("Texte chiffré:", texte_chiffre)

texte_dechiffre = dechiffrement_cesar(texte_chiffre, decalage)
print("Texte déchiffré:", texte_dechiffre)





#Jeu de devinette de nombre

import random

def devinette_nombre():
    nombre_a_deviner = random.randint(1, 100)
    essais_restants = 5

    print("Devinez le nombre entre 1 et 100. Vous avez 5 essais.")

    while essais_restants > 0:
        essai = int(input("Entrez votre devinette: "))

        if essai == nombre_a_deviner:
            print("Félicitations! Vous avez deviné le nombre.")
            return
        elif essai < nombre_a_deviner:
            print("Le nombre est plus grand.")
        else:
            print("Le nombre est plus petit.")

        essais_restants -= 1
        print(f"Il vous reste {essais_restants} essais.")

    print(f"Dommage! Le nombre était {nombre_a_deviner}.")

devinette_nombre()





#Convertisseur de devises

def convertisseur_devises(montant, taux_change):
    montant_converti = montant * taux_change
    return montant_converti

montant = float(input("Entrez le montant en devise d'origine: "))
taux = float(input("Entrez le taux de change: "))

montant_converti = convertisseur_devises(montant, taux)
print("Montant converti:", montant_converti)





#Jeu du Morpion

def afficher_plateau(plateau):
    for ligne in plateau:
        print("|".join(ligne))
        print("-" * 5)

def verifier_victoire(plateau, joueur):
    for ligne in plateau:
        if all(case == joueur for case in ligne):
            return True
    for colonne in range(3):
        if all(plateau[i][colonne] == joueur for i in range(3)):
            return True
    if all(plateau[i][i] == joueur for i in range(3)) or all(plateau[i][2 - i] == joueur for i in range(3)):
        return True
    return False

def morpion():
    plateau = [[" "]*3 for _ in range(3)]
    joueurs = ["X", "O"]
    tour = 0

    while True:
        afficher_plateau(plateau)
        joueur = joueurs[tour % 2]
        print(f"C'est au tour du joueur {joueur}")

        ligne = int(input("Entrez le numéro de ligne (0, 1, 2): "))
        colonne = int(input("Entrez le numéro de colonne (0, 1, 2): "))

        if plateau[ligne][colonne] != " ":
            print("Case déjà occupée. Choisissez une autre case.")
            continue

        plateau[ligne][colonne] = joueur
        if verifier_victoire(plateau, joueur):
            afficher_plateau(plateau)
            print(f"Le joueur {joueur} a gagné!")
            break

        tour += 1

morpion()





#Un jeu de type "Space Invaders"

import os
import time
import random
import keyboard

#Fonction pour afficher le plateau de jeu
def afficher_plateau(joueur_x, ennemis, largeur):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(largeur):
        if i == joueur_x:
            print("V", end="")
        elif (i, 0) in ennemis:
            print("X", end="")
        else:
            print(" ", end="")
    print("")

#Fonction principale du jeu
def space_invaders(largeur, vitesse):
    joueur_x = largeur // 2
    ennemis = set()

    while True:
        afficher_plateau(joueur_x, ennemis, largeur)
        if keyboard.is_pressed('q') and joueur_x > 0:
            joueur_x -= 1
        elif keyboard.is_pressed('d') and joueur_x < largeur - 1:
            joueur_x += 1

        if random.random() < 0.1:
            ennemis.add((random.randint(0, largeur - 1), 0))

        ennemis_a_supprimer = set()
        for ennemi in ennemis:
            x, y = ennemi
            if y == 0:
                ennemis_a_supprimer.add(ennemi)
            else:
                ennemis_a_supprimer.add(ennemi)
                ennemis.add((x, y - 1))
        ennemis -= ennemis_a_supprimer

        if (joueur_x, 0) in ennemis:
            print("Game Over!")
            break

        time.sleep(vitesse)

#Appel de la fonction principale pour démarrer le jeu
space_invaders(30, 0.1)
