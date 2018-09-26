# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:36:41 2018

@author: antoi
"""

import random

#fonction HanoÃ®

def test_2(silo_initial, silo_final):
    if silo_initial != []:
         print(" le premier conteneur du silot " + str(silo_initial) + " se dÃ©place vers le silot " + str(silo_final))
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
    print( " Ã©tat du silo final : " + str(silo_final))

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
    print("Le conteneur de radioactivitÃ©",i,"a Ã©tÃ© transfÃ©rÃ© du tube au silo temporaire")

#DÃ©termination du nombre de silo Ã  utiliser, et crÃ©ation de ceux ci sous forme de listes

print("\nCombien de silos doit-on utiliser? Le minimum de silo requis est 3")
nombre_de_silo = int(input())
while (nombre_de_silo < 3) :
    print("Combien de silos doit-on utiliser? Le minimum de silo requis est 3")
    nombre_de_silo = int(input())
silos=[]
for a in range(1,nombre_de_silo+1):
    silos.append([])

#RÃ©partition alÃ©atoire dans les silos, avec respect de la contrainte

silo_precedent=0
essais_de_distribution=conteneurs
while essais_de_distribution>0:
    silo_actuel=random.randint(1,nombre_de_silo)
    if silo_actuel!=silo_precedent:
        silo_precedent=silo_actuel
        silos[silo_actuel-1].append(essais_de_distribution)
        del temporaire[-1]
        print("Le conteneur de radioactivitÃ©",essais_de_distribution,"a Ã©tÃ© transfÃ©rÃ© dans le silo",silo_actuel)
        essais_de_distribution-=1

#Recherche de la pile d'arrivÃ©e en fonction de la pile de dÃ©part

found=False
silo_compteur=0
conteneur_cible=2
dÃ©part=silo_actuel-1
nombre_a_dÃ©placer =1
while not found:
    if len(silos[silo_compteur])!=0:
        if silos[silo_compteur][-1]==conteneur_cible:
            arrivÃ©e=silo_compteur
            conteneur_cible+=1
            found = True
        else:
            silo_compteur+=1
    else:
        silo_compteur+=1
#DÃ©termination d'un silo intÃ©rmÃ©diaire, qui n'est ni le silo de dÃ©part, ni celui d'arrivÃ©e

inter=random.randint(1,nombre_de_silo)-1
while inter == dÃ©part or inter == arrivÃ©e:
    inter=random.randint(1,nombre_de_silo)-1

#Algorithme de HanoÃ¯ rÃ©pÃ©tÃ© jusqu'Ã  rÃ©solution

while nombre_a_dÃ©placer<conteneurs:
    hanoi(nombre_a_dÃ©placer, silos[dÃ©part], silos[arrivÃ©e], silos[inter])
    if len(silos[arrivÃ©e])==conteneurs:
        break
    nombre_a_dÃ©placer+=1
    dÃ©part=arrivÃ©e
    silo_compteur=0
    found=False
    while not found:
        if len(silos[silo_compteur])!=0:
            if silos[silo_compteur][-1]==conteneur_cible:
                arrivÃ©e=silo_compteur
                conteneur_cible+=1
                found=True
            else:
                silo_compteur+=1
        else:
            silo_compteur+=1
    inter=random.randint(1,nombre_de_silo)-1
    while inter == dÃ©part or inter == arrivÃ©e:
        inter=random.randint(1,nombre_de_silo)-1

#DÃ©placement du tout dans le NiÃ¨me silo si nÃ©cessaire

if arrivÃ©e != nombre_de_silo-1:
    inter=random.randint(1,nombre_de_silo)-1
    while inter == arrivÃ©e or inter == nombre_de_silo-1:
        inter=random.randint(1,nombre_de_silo)-1
    hanoi(conteneurs,silos[arrivÃ©e],silos[nombre_de_silo-1],silos[inter])
