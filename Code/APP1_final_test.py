# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:00:00 2018

@author: alexaucalme
"""

import random

# Fonction d'Hanoî

def test_2(silo_initial, silo_final, detail):
    if silo_initial != []:
        if detail == True:
            print("Le premier conteneur du silot " + str(silo_initial) + " se deplace vers le silot " + str(silo_final))
        a = silo_initial.pop()
        silo_final.append(a)

def hanoi_2(X, silo_initial, silo_final, silo_intermediaire, detail):
    if X == 1:
        test_2(silo_initial, silo_final, detail)
    else:
        hanoi_2(X-1, silo_initial, silo_intermediaire, silo_final, detail)
        test_2(silo_initial, silo_final,detail)
        hanoi_2(X-1, silo_intermediaire, silo_final, silo_initial, detail)

def hanoi(X, silo_initial, silo_final, silo_intermediaire, detail):
    hanoi_2(X, silo_initial, silo_final, silo_intermediaire, detail)
    print( "\nÉtat du silo final : " + str(silo_final))


# On demande si les étapes intermédiaires doivent être détaillés ou non

def detail():
    detail = False
    demande_detail = input('Doit-on détailler les étapes de transferts ? (Oui/Non) : ')
    if demande_detail == 'Oui':
        detail = True
    return detail

# Remplissage du  silo initial par le réacteur

def remplissage(conteneurs, valeur_accident):
    tube=[]
    accident = False
    if conteneurs >= valeur_accident:
        for i in range(conteneurs, 0, -1):
            tube.append(i)
        accident = True
    return tube, accident

# Transfert vers le silo temporaire

def transfert(conteneurs, tube, detail):
    temporaire = []
    for i in range(1, conteneurs + 1):
        del tube[-1]
        temporaire.append(i)
        if detail == True:
            print("Le conteneur de radioactivité ", i, " a été transféré du tube au silo temporaire\n")
    return tube, temporaire

# Détermination du nombre de silo à utiliser, et création de ceux-ci sous forme de listes

def silos():
    nombre_de_silo = int(input('Combien de silos doit-on utiliser ? (3 minimum) : '))
    while nombre_de_silo < 3 :
        nombre_de_silo = int(input('Combien de silos doit-on utiliser ? Le nombre de silos doit être supérieur à 3 !!!'))
    silos = []
    for a in range(1, nombre_de_silo + 1):
        silos.append([])
    return nombre_de_silo, silos

# Répartition aléatoire dans les silos, avec respect de la contrainte

def repartition(conteneurs, nombre_de_silo, silos, temporaire, detail):
    silo_precedent = 0
    essais_de_distribution = conteneurs
    while essais_de_distribution > 0:
        silo_actuel = random.randint(1, nombre_de_silo)
        if silo_actuel != silo_precedent:
            silo_precedent = silo_actuel
            silos[silo_actuel-1].append(essais_de_distribution)
            del temporaire[-1]
            if detail == True:
                print("\nLe conteneur de radioactivité", essais_de_distribution, "a été transféré dans le silo ", silo_actuel)
                essais_de_distribution -= 1
    return silo_actuel, silos, temporaire

# Recherche de la pile d'arrivée en fonction de la pile de départ

def recherche(silos, silo_actuel):
    found = False
    silo_compteur = 0
    conteneur_cible = 2
    depart = silo_actuel - 1
    nombre_a_deplacer = 1
    while not found:
        if len(silos[silo_compteur]) != 0:
            if silos[silo_compteur][-1] == conteneur_cible:
                arrivee = silo_compteur
                conteneur_cible += 1
                found = True
            else:
                silo_compteur += 1
        else:
            silo_compteur += 1
    return silos, arrivee, depart, nombre_a_deplacer, conteneur_cible

# Détermination d'un silo intermediaire

def silo_intermediaire_aleat(nombre_de_silo, depart, arrivee):
    inter = random.randint(1, nombre_de_silo) - 1
    while inter == depart or inter == arrivee:
        inter = random.randint(1, nombre_de_silo) - 1
    return inter

# Algorithme de Hanoï répeté jusqu'à la résolution

def lancement_hanoi(nombre_a_deplacer, conteneurs, silos, depart, arrivee, inter, conteneur_cible, detail):
    while nombre_a_deplacer < conteneurs:
        hanoi(nombre_a_deplacer, silos[depart], silos[arrivee], silos[inter], detail)
        if len(silos[arrivee]) == conteneurs:
            break
            nombre_a_deplacer += 1
            depart = arrivee
            silo_compteur = 0
            found = False
            while not found:
                if len(silos[silo_compteur]) != 0:
                    if silos[silo_compteur][-1] == conteneur_cible:
                        arrivee = silo_compteur
                        conteneur_cible += 1
                        found = True
                    else:
                        silo_compteur += 1
                else:
                    silo_compteur += 1
        inter = random.randint(1, nombre_de_silo) - 1
        while inter == depart or inter == arrivee:
            inter = random.randint(1, nombre_de_silo) - 1
    return nombre_a_deplacer, conteneurs, silos, depart, arrivee, inter

# Déplacement du tout dans le Nième silo si nécessaire

def nieme_silo(arrivee, nombre_de_silo, silos, inter, conteneurs, detail):
    if arrivee != nombre_de_silo - 1:
        inter = random.randint(1, nombre_de_silo) - 1
        while inter == arrivee or inter == nombre_de_silo - 1:
            inter = random.randint(1, nombre_de_silo) - 1
        hanoi(conteneurs, silos[arrivee], silos[nombre_de_silo - 1], silos[inter], detail)
    return arrivee, nombre_de_silo, silos, inter, conteneurs


#On appelle detail pour demander si l'utilisateur souhaite afficher les détails
detail = detail()

conteneurs = int(input('\nCombien de conteneurs sont dans le réacteur ? '))
valeur_accident = int(input("Quel est le niveau d'accident ? "))

tube, accident = remplissage(conteneurs, valeur_accident)

if accident:
    tube, temporaire = transfert(conteneurs, tube, detail)
    nombre_de_silo, silos = silos()
    silo_actuel, silos, temporaire = repartition(conteneurs, nombre_de_silo, silos, temporaire, detail)
    silos, arrivee, depart, nombre_a_deplacer, conteneur_cible = recherche(silos, silo_actuel)
    inter = silo_intermediaire_aleat(nombre_de_silo, depart, arrivee)
    nombre_a_deplacer, conteneurs, silos, depart, arrivee, inter = lancement_hanoi(nombre_a_deplacer, conteneurs, silos, depart, arrivee, inter, conteneur_cible, detail)
    arrivee, nombre_de_silo, silos, inter, conteneurs = nieme_silo(arrivee, nombre_de_silo, silos, inter, conteneurs, detail)

else:
    print("Pas d'accident, merci de réessayer !")
