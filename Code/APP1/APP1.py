# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:00:00 2018

@author: alexaucalme
"""

import random

# Fonction d'Hanoî

def test_2(silo_initial, silo_final):
    if silo_initial != []:
        if detail == True:
            print("Le premier conteneur du silot " + str(silo_initial) + " se deplace vers le silot " + str(silo_final))
        a = silo_initial.pop()
        silo_final.append(a)

def hanoi_2(X, silo_initial, silo_final, silo_intermediaire):
    if X == 1:
        test_2(silo_initial, silo_final)
    else:
        hanoi_2(X-1, silo_initial, silo_intermediaire, silo_final)
        test_2(silo_initial, silo_final)
        hanoi_2(X-1, silo_intermediaire, silo_final, silo_initial)

def hanoi(X, silo_initial, silo_final, silo_intermediaire):
    hanoi_2(X, silo_initial, silo_final, silo_intermediaire)
    print( "\nÉtat du silo final : " + str(silo_final))

# On demande si les étapes intermédiaires doivent être détaillés ou non

detail = False
demande_detail = input('Doit-on détailler les étapes de transferts ? (Oui/Non) : ')
if demande_detail == 'Oui':
    detail = True

# Remplissage du  silo initial par le réacteur

tube=[]
conteneurs = int(input('\nCombien de conteneurs sont évacués ? '))
for i in range(conteneurs, 0, -1):
    tube.append(i)

# Transfert vers le silo temporaire

temporaire = []
for i in range(1, conteneurs + 1):
    del tube[-1]
    temporaire.append(i)
    if detail == True:
        print("Le conteneur de radioactivité ", i, " a été transféré du tube au silo temporaire\n")

# Détermination du nombre de silo à utiliser, et création de ceux-ci sous forme de listes

nombre_de_silo = int(input('Combien de silos doit-on utiliser ? (3 minimum) : '))
while (nombre_de_silo < 3) :
    nombre_de_silo = int(input('Combien de silos doit-on utiliser ? Le nombre de silos doit être supérieur à 3 !!!'))
silos = []
for a in range(1, nombre_de_silo + 1):
    silos.append([])

# Répartition aléatoire dans les silos, avec respect de la contrainte

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

# Recherche de la pile d'arrivée en fonction de la pile de départ

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

# Détermination d'un silo intermediaire

inter = random.randint(1, nombre_de_silo) - 1
while inter == depart or inter == arrivee:
    inter = random.randint(1, nombre_de_silo) - 1

# Algorithme de Hanoï répeté jusqu'à la résolution

while nombre_a_deplacer < conteneurs:
    hanoi(nombre_a_deplacer, silos[depart], silos[arrivee], silos[inter])
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

# Déplacement du tout dans le Nième silo si nécessaire

if arrivee != nombre_de_silo - 1:
    inter = random.randint(1, nombre_de_silo) - 1
    while inter == arrivee or inter == nombre_de_silo - 1:
        inter = random.randint(1, nombre_de_silo) - 1
    hanoi(conteneurs, silos[arrivee], silos[nombre_de_silo - 1], silos[inter])
