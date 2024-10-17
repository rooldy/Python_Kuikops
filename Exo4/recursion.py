## Question 4 - Récursion

##import logging

def recur_sum(n):
    # Cas de base : si n est égal à 1, retourne 1 (car 1 / 1 = 1)
    if n == 1:
        return 1
    # Appel récursif : additionner 1/n au résultat de harmonic_sum(n-1)
    else:
        return 1 / n + recur_sum(n - 1)

# Exemple d'utilisation
n = 4
resultat = recur_sum(n)
print(f"La somme harmonique jusqu'au terme {n} est : {resultat}")