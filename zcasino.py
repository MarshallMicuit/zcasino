# Définition des variables
import os
from random import randrange
from math import ceil
argent = 100
roulette = randrange(50)

# Proposer à l'utilisateur de miser sur un numéro entre 0 et 49 (pairs = noir, impairs = rouge)
# Si c'est gagné, le joueur gagne 3* sa mise
# Sinon, on vérifie si la couleur est bonne. Si oui, le joueur gagne mise / 2. Si non il perd tout
# On entend par là qu'il gagne mise + récompense, ajouté à son argent
print("Bienvenue dans le casino, le but du jeu est simple, faire péter la banque !")
print("Pour se faire vous disposez d'un montant initial de 100 jetons. Misez et choisissez une case et le croupier se chargera du reste.")
print("Si votre choix est correct, vous gagnez 3 fois la mise, sinon si votre votre chiffre est de la même couleur que la case,\nvous gagnez 1,5 fois votre mise.")
print("Votre objectif est d'obtenir 1000 jetons ou plus, bonne chance.")

while argent < 999 and argent > 1:
    print("Argent actuel :", ceil(argent))
    mise = -1
    while mise < 0 or mise > argent:
        mise = -1
        mise = input("Combien voulez vous miser ? ")
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas entré de nombre")
            mise = -1
            continue
        if mise < 0:
            print("Nombre négatif")
        if mise > argent:
            print("Vous n'avez pas autant d'argent (", argent,"jetons)")
    argent = argent - mise

    choisir_numero = -1
    while choisir_numero < 0 or choisir_numero > 49:
        choisir_numero = -1
        choisir_numero = input("Sur quel numéro entre 0 et 49 voulez-vous parier ? ")
        try:
            choisir_numero = int(choisir_numero)
        except ValueError:
            print("Vous n'avez pas entré de nombre")
            choisir_numero = -1
            continue
        if choisir_numero < 0:
            print("Nombre négatif")
        if choisir_numero > 49:
            print("Nombre trop élevé")  
  
    print("La roulette se lance et tombe sur", roulette)
    if roulette == choisir_numero:
        print("Vous avez gagné ! Vous recevez", ceil(mise*3), "jetons !")
        argent += mise*3
    elif choisir_numero % 2 == 0 and roulette % 2 == 0:
        print("Vous n'avez pas gagné mais votre chiffre est noir ! Vous recevez", ceil(mise + (mise/2)), "jetons !")
        argent += mise + (mise/2)
    elif choisir_numero % 2 != 0 and roulette % 2 != 0:
        print("Vous n'avez pas gagné mais votre chiffre est rouge ! Vous recevez", ceil(mise + (mise/2)), "jetons !")
        argent += mise + (mise/2)
    else:
        print("Vous avez perdu, vous ne gagnez rien !")

if argent > 999:
    print("Vous repartez riche du casino ! Bien joué !")
elif argent < 1:
    print("Le vigile vous met dehors, vous êtes sans le sou !")

os.system("pause")