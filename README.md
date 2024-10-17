<h1> Projet Python - TP Jeux et Scripts Python </h1>
Description du Projet
Ce projet contient plusieurs exercices pratiques en Python que j'ai réalisés dans le cadre d'un TP. Les exercices couvrent divers sujets, tels que la manipulation des boucles, les conditions, l'utilisation des bibliothèques Python comme logging, et la gestion des exceptions.

Liste des Exercices :

Exercice 1 - Deviner le Nombre

Description : Un jeu simple où l'utilisateur doit deviner un nombre choisi aléatoirement par l'ordinateur.
Fonctionnalité principale : L'utilisateur propose un nombre, et l'ordinateur indique si le nombre proposé est trop grand, trop petit ou correct.
Particularité : Gestion des erreurs pour s'assurer que l'utilisateur entre bien un nombre valide.

Exercice 2 - Compter les Mots

Description : Un programme qui demande à l'utilisateur d'entrer le nom d'un fichier texte. Le programme compte le nombre de fois où le mot "python" apparaît dans le fichier.
Fonctionnalité principale : Utilisation de la gestion des exceptions pour gérer le cas où le fichier n'existe pas. L'utilisateur a trois essais pour entrer le bon fichier.
Particularité : Utilisation du try-except pour capturer les erreurs de fichier non trouvé.

Exercice 3 - Fizz Buzz

Description : Un programme qui affiche "fizz" pour les multiples de 3, "buzz" pour les multiples de 5, et "fizz buzz" pour les multiples de 3 et 5.
Fonctionnalité principale : Boucle qui affiche les résultats pour les nombres de 1 à 50 avec enregistrement des événements dans un fichier de log grâce au module logging.
Particularité : Utilisation du module logging pour enregistrer les événements de type info et debug pendant l'exécution du programme.

Exercice 4 - ZCasino

Description : Un jeu de roulette où l'utilisateur peut miser sur un nombre et remporter des gains en fonction des règles du jeu.
Fonctionnalité principale : Le joueur choisit un nombre entre 0 et 49, et l'ordinateur détermine un numéro aléatoire sur la roulette. Les gains dépendent si le nombre exact est trouvé ou si la couleur du numéro (pair ou impair) correspond.
Particularité : Utilisation de plusieurs modules pour séparer les responsabilités du code : récupération des inputs, gestion des règles du jeu et exécution du jeu principal.

Exercice 5 - Météo

Description : Un programme qui récupère les informations météorologiques pour une ville donnée en utilisant l'API d'OpenWeatherMap.
Fonctionnalité principale : Récupération de la température, de l'humidité et de la vitesse du vent pour une ville donnée par l'utilisateur.
Particularité : Utilisation de l'API d'OpenWeatherMap avec des requêtes HTTP et gestion des erreurs en cas de problème de connexion ou d'erreur de ville.
