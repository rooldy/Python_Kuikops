## Question 4 - Récursion

import logging

# Configurer le logging pour afficher les messages dans la console
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Demander à l'utilisateur d'entrer un nombre
    n = int(input("Entrer un nombre:"))
    logging.info(f"Nombre saisi : {n}")

    # Tant que le nombre est inférieur à 1, redemander un nombre
    while n < 1:
        logging.warning("Le nombre doit être supérieur ou égal à 1.")
        n = int(input("Entrer un nombre:"))
        logging.info(f"Nombre mis à jour : {n}")

    # Initialisation de variables
    i = 1
    s = 0
    logging.debug(f"Initialisation de i={i}, s={s}")

    # Boucle pour calculer la somme harmonique
    while i <= n:
        s += 1 / i
        logging.debug(f"i={i}, somme partielle={s:.2f}")
        i += 1

    # Affichage du résultat
    logging.info(f"La somme harmonique est : {s:.2f}")
    print(f"La somme est : {s:.2f}")

except ValueError as e:
    logging.error(f"Erreur de saisie : {e}")