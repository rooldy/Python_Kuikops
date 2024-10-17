## Exo 1 Devine nombre

import random
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
            logging.info(f"L'utilisateur a proposé {proposition}: trop petit.")
        elif proposition > nombre_aleatoire:
            print("C'est trop grand !")
            logging.info(f"L'utilisateur a proposé {proposition}: trop grand.")
        else:
            print("Bravo ! Vous avez deviné le bon nombre.")
            logging.info(f"L'utilisateur a deviné le nombre: {nombre_aleatoire}.")
            break  # Fin de la boucle et du jeu si le nombre est trouvé
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        logging.error("Tentative de saisie invalide.")
