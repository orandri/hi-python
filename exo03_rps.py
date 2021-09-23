
from random import *
choix = ("Rock","Paper","Scissors")

def choix_joueur():
    print("Rock:  0")
    print("Paper:  1")
    print("Scissors: 2")
    joueur = int(input("Choice ? "))
    while joueur not in [0,1,2]:
        joueur = int(input("Choice ? "))
    return joueur

def choix_ordinateur():
    return choice([0,1,2])



playeur = choix_joueur()
ordi = choix_ordinateur()
print("Playeur:",choix[playeur])
print("Ordi:",choix[ordi])
print(("EGALITE","L'Ordinateur gagne","Le Joueur gagne")[(playeur<ordi)-(playeur>ordi)])




