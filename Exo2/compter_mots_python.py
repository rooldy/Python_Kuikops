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
            break

        except FileNotFoundError:
            attempts += 1
            print(f"Erreur : le fichier '{file_name}' n'a pas été trouvé. Tentative {essai}/{max_essai}.")
        
        if attempts == max_essai:
            print("Erreur : le fichier n'a pas pu être trouvé après 3 tentatives. Fin du programme.")

# Appeler la fonction
count_python()
