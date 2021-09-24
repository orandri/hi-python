import random

recommence = ""
while recommence != "n":
    int_min = input("Choisissez l'intervalle min: ")
    int_max = input("Choisissez l'intervalle max: ")

    while int_min.isnumeric() == False or int_max.isnumeric() == False:
        print("Veuillez saisir des nombres entiers seulement")
        int_min = input("Choisissez l'intervalle min: ")
        int_max = input("Choisissez l'intervalle max: ")
   
    int_min = int(int_min)
    int_max = int(int_max)

    while int_min>int_max:
        print("Attention l'intevalle min doit être inferieur à l'intervalle max :")
        int_min = input("Choisissez l'intervalle min: ")
        int_max = input("Choisissez l'intervalle max: ")
    
        
    nombre_aleatoire = random.randint(int_min,int_max)

    choix_user = input("Choisissez entre "+ str(int_min) + " et " +str(int_max) +" : ")
    
    while choix_user.isnumeric()== False:
        print("Saisir des nombres et non des lettres")
        choix_user = input("Choisissez entre "+ str(int_min) + " et " +str(int_max) +" : ")
    choix_user = int(choix_user)
    essai = 1
    while choix_user != nombre_aleatoire:
        if (choix_user < nombre_aleatoire):
           print("C'est plus")
        else :
             print("c'est moins")
        if choix_user < int_min or choix_user >int_max:
            print("Vous êtes hors de l'intervalle ATTENTION !")
        essai +=1
        choix_user = input("Choisissez entre "+str(int_min) +" et "+str(int_max)+ ": ")
        while choix_user.isnumeric()== False:
            print("Saisir des nombres et non des lettres")
            choix_user = input("Choisissez entre "+ str(int_min) + " et " +str(int_max) +" : ")
        choix_user=int(choix_user)

    print("VICTOIRE ! le nombre_aleatoire : "+ str(nombre_aleatoire) + " après "+str(essai)+ " essais")
    recommence = input("Voulez-vous recommencer ? o/n ").lower()
print("Fin de la partie.")

    

