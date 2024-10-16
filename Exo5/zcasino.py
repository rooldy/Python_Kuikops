def get_valid_number():
    """Demande à l'utilisateur de choisir un nombre valide entre 0 et 49."""
    while True:
        try:
            number = int(input("Choisissez un nombre entre 0 et 49 : "))
            if 0 <= number <= 49:
                return number
            else:
                print("Le nombre doit être entre 0 et 49.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def get_valid_bet(balance):
    """Demande à l'utilisateur de miser une somme valide en fonction de son solde."""
    while True:
        try:
            bet = int(input(f"Votre solde est de {balance}€. Combien voulez-vous miser ? "))
            if 0 < bet <= balance:
                return bet
            else:
                print(f"Votre mise doit être comprise entre 1 et {balance}€.")
        except ValueError:
            print("Veuillez entrer une mise valide.")