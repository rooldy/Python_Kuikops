# game.py
from utilisateur import spin_roulette, calculate_winnings
from zcasino import get_valid_number, get_valid_bet

def play_round(balance):
    """Gère un tour de jeu : pari, tirage de la roulette, calcul des gains."""
    print("\n=== Nouveau tour ===")
    player_number = get_valid_number()
    bet = get_valid_bet(balance)
    
    roulette_number = spin_roulette()
    print(f"La roulette a choisi le numéro : {roulette_number}")

    winnings = calculate_winnings(player_number, roulette_number, bet)
    
    if winnings > 0:
        print(f"Félicitations ! Vous avez gagné {winnings}€.")
    else:
        print("Désolé, vous n'avez rien gagné cette fois.")
    
    return winnings - bet  # Retourne le solde net (gains - mise)

def ask_replay():
    """Demande au joueur s'il souhaite continuer à jouer."""
    while True:
        choice = input("Voulez-vous rejouer ? (o/n) : ").lower()
        if choice in ['o', 'n']:
            return choice == 'o'
        print("Réponse non valide. Veuillez entrer 'o' pour oui ou 'n' pour non.")
