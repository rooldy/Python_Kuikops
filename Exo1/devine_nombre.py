## Exo 1 Devine nombre

import random

# L'ordinateur choisit un nombre aléatoire entre 1 et 100
nombre_aleatoire = random.randint(1, 100)

print("Bienvenue dans le jeu 'Devine le nombre' !")
print("J'ai choisi un nombre entre 1 et 100. À vous de le deviner !")

# Boucle de jeu
while True:
    # L'utilisateur propose un nombre
    try:
        proposition = int(input("Entrez votre proposition : "))

        # Vérifier si la proposition est correcte
        if proposition < nombre_aleatoire:
            print("C'est trop petit !")
        elif proposition > nombre_aleatoire:
            print("C'est trop grand !")
        else:
            print("Bravo ! Vous avez deviné le bon nombre.")
            break  # Fin de la boucle et du jeu si le nombre est trouvé
    except ValueError:
        print("Veuillez entrer un nombre valide.")
