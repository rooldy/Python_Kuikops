## Exo 3 Fizz Buzz

import logging

# Configuration du logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def fizz_buzz(valeur):
    if valeur % 3 == 0 and valeur % 5 == 0:
        logging.info(f"Valeur {valeur} : fizz buzz")
        return "fizz buzz"
    elif valeur % 3 == 0:
        logging.info(f"Valeur {valeur} : fizz")
        return "fizz"
    elif valeur % 5 == 0:
        logging.info(f"Valeur {valeur} : buzz")
        return "buzz"
    else:
        logging.debug(f"Valeur {valeur} : {valeur}")
        return str(valeur)

# Exemple d'utilisation
for i in range(1, 51):
    print(fizz_buzz(i))
