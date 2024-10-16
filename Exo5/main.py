# main.py
from game import play_round, ask_replay

def main():
    balance = 100  # Le joueur commence avec 100€
    print("Bienvenue au ZCasino ! Vous commencez avec 100€.")

    while balance > 0:
        net_change = play_round(balance)
        balance += net_change
        print(f"Votre nouveau solde est de {balance}€.")
        
        if balance <= 0:
            print("Vous n'avez plus d'argent. Fin de la partie.")
            break
        
        if not ask_replay():
            print(f"Merci d'avoir joué ! Vous repartez avec {balance}€.")
            break

if __name__ == '__main__':
    main()
