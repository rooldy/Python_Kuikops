## Exo 2 Compter les mots

import logging

# Configuration du logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def count_python():
    essai = 0
    max_essai = 3

    while essai < max_essai:
        try:
            # Demande le nom du fichier à l'utilisateur
            file_name = input("Entrez le nom du fichier (ex: test.txt) : ")

            # Ouvre et lit le fichier
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()

            # Compte le nombre d'occurrences de "python"
            compter = content.lower().count('python')
            print(f"Le mot 'python' apparaît {compter} fois dans le fichier.")
            logging.info(f"Le mot 'python' apparaît {compter} fois dans le fichier '{file_name}'.")
            break

        except FileNotFoundError:
            essai += 1  # Correction : incrémenter essai au lieu de attempts
            logging.error(f"Erreur : le fichier '{file_name}' n'a pas été trouvé.")
            print(f"Erreur : le fichier '{file_name}' n'a pas été trouvé. Tentative {essai}/{max_essai}.")
        
        if essai == max_essai:  # Correction : utiliser essai pour la condition
            logging.error("Erreur : le fichier n'a pas pu être trouvé après 3 tentatives.")
            print("Erreur : le fichier n'a pas pu être trouvé après 3 tentatives. Fin du programme.")

# Appeler la fonction
count_python()