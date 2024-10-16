## Exo 3 Fizz Buzz

def fizz_buzz(valeur):
    if valeur % 3 == 0 and valeur % 5 == 0:
        return "fizz buzz"
    elif valeur % 3 == 0:
        return "fizz"
    elif valeur % 5 == 0:
        return "buzz"
    else:
        return str(valeur)

# Exemple d'utilisation
for i in range(1, 51):
    print(fizz_buzz(i))