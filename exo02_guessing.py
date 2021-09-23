import random
int_min = int(input("Choisissez l'intervalle min: "))
int_max = int(input("Choisissez l'intervalle max: "))
nombre_aleatoire = random.randint(int_min,int_max)

choix_user = int(input("Choisissez entre "+ str(int_min) + " et " +str(int_max) +" : "))
essai = 0
while choix_user != nombre_aleatoire:
    if (choix_user < nombre_aleatoire):
        print("C'est plus")
    else :
        print("c'est moins")
        
    essai +=1
    choix_user = int(input("Choisissez entre 1 et 100: "))

print("VICTOIRE ! le nombre_aleatoire : "+ str(nombre_aleatoire) + " après "+str(essai)+ "essais")