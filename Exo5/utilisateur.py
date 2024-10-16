# utilisateurs.py
import random

def spin_roulette():
    """Simule un tour de roulette et retourne un numéro aléatoire entre 0 et 49."""
    return random.randint(0, 49)

def is_black(number):
    """Retourne True si le numéro est pair (noir), False s'il est impair (blanc)."""
    return number % 2 == 0

def calculate_winnings(player_number, roulette_number, bet):
    """Calcule les gains selon le numéro choisi et le numéro de la roulette."""
    if player_number == roulette_number:
        return bet * 3  # Le joueur gagne 3 fois sa mise s'il devine le numéro exact
    elif is_black(player_number) == is_black(roulette_number):
        return bet * 1.5  # Le joueur gagne 50% de sa mise s'il devine la couleur
    else:
        return 0  # Le joueur perd tout
