import random

nombre_aleatoire = random.randint(1,100)

choix_user = int(input("Choisissez entre 1 et 100: "))
essai = 0
while choix_user != nombre_aleatoire:
    if (choix_user < nombre_aleatoire):
        print("C'est plus")
    else :
        print("c'est moins")
        
    essai +=1
    choix_user = int(input("Choisissez entre 1 et 100: "))

print("VICTOIRE ! le nombre_aleatoire : "+ str(nombre_aleatoire) + "après "+str(essai)+ "essais")