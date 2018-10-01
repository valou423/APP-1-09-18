# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:36:41 2018

@author: antoi
"""

import random

#fonction HanoÃ®

def test_2(silo_initial, silo_final):
    if silo_initial != []:
         print(" le premier conteneur du silot " + str(silo_initial) + " se deplace vers le silot " + str(silo_final))
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
    print( " etat du silo final : " + str(silo_final))

#Remplissage du tube initial

tube=[]
print("Combien de conteneurs?")
conteneurs=int(input())
for i in range(conteneurs,0,-1):
    tube.append(i)

#Transfert dans le silo temporaire

temporaire=[]
for i in range(1,conteneurs+1):
    del tube[-1]
    temporaire.append(i)
    print("Le conteneur de radioactivite",i,"a ete transfere du tube au silo temporaire")

#Determination du nombre de silo Ã  utiliser, et creation de ceux ci sous forme de listes

print("\nCombien de silos doit-on utiliser? Le minimum de silo requis est 3")
nombre_de_silo = int(input())
while (nombre_de_silo < 3) :
    print("Combien de silos doit-on utiliser? Le minimum de silo requis est 3")
    nombre_de_silo = int(input())
silos=[]
for a in range(1,nombre_de_silo+1):
    silos.append([])

#Repartition aleatoire dans les silos, avec respect de la contrainte

silo_precedent=0
essais_de_distribution=conteneurs
while essais_de_distribution>0:
    silo_actuel=random.randint(1,nombre_de_silo)
    if silo_actuel!=silo_precedent:
        silo_precedent=silo_actuel
        silos[silo_actuel-1].append(essais_de_distribution)
        del temporaire[-1]
        print("Le conteneur de radioactivite",essais_de_distribution,"a ete transfere dans le silo",silo_actuel)
        essais_de_distribution-=1

#Recherche de la pile d'arrivee en fonction de la pile de depart

found=False
silo_compteur=0
conteneur_cible=2
depart=silo_actuel-1
nombre_a_deplacer =1
while not found:
    if len(silos[silo_compteur])!=0:
        if silos[silo_compteur][-1]==conteneur_cible:
            arrivee=silo_compteur
            conteneur_cible+=1
            found = True
        else:
            silo_compteur+=1
    else:
        silo_compteur+=1
#Determination d'un silo intermediaire, qui n'est ni le silo de depart, ni celui d'arrivee

inter=random.randint(1,nombre_de_silo)-1
while inter == depart or inter == arrivee:
    inter=random.randint(1,nombre_de_silo)-1

#Algorithme de HanoÃ¯ repete jusqu'Ã  resolution

while nombre_a_deplacer<conteneurs:
    hanoi(nombre_a_deplacer, silos[depart], silos[arrivee], silos[inter])
    if len(silos[arrivee])==conteneurs:
        break
    nombre_a_deplacer+=1
    depart=arrivee
    silo_compteur=0
    found=False
    while not found:
        if len(silos[silo_compteur])!=0:
            if silos[silo_compteur][-1]==conteneur_cible:
                arrivee=silo_compteur
                conteneur_cible+=1
                found=True
            else:
                silo_compteur+=1
        else:
            silo_compteur+=1
    inter=random.randint(1,nombre_de_silo)-1
    while inter == depart or inter == arrivee:
        inter=random.randint(1,nombre_de_silo)-1

#Deplacement du tout dans le NiÃ¨me silo si necessaire

if arrivee != nombre_de_silo-1:
    inter=random.randint(1,nombre_de_silo)-1
    while inter == arrivee or inter == nombre_de_silo-1:
        inter=random.randint(1,nombre_de_silo)-1
    hanoi(conteneurs,silos[arrivee],silos[nombre_de_silo-1],silos[inter])
