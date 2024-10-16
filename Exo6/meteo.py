import requests

def get_weather_data(city, api_key):
    """Récupère les données météo de la ville en utilisant l'API d'OpenWeatherMap"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lève une exception si le statut n'est pas 200 (OK)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données : {e}")
        return None

def display_weather_info(weather_data):
    """Affiche les informations météo extraites des données récupérées"""
    if weather_data:
        city_name = weather_data.get('name')
        main_data = weather_data.get('main')
        wind_data = weather_data.get('wind')

        if main_data and wind_data:
            temp = main_data.get('temp')
            humidity = main_data.get('humidity')
            wind_speed = wind_data.get('speed')

            print(f"\nMétéo à {city_name}:")
            print(f"Température : {temp}°C")
            print(f"Humidité : {humidity}%")
            print(f"Vitesse du vent : {wind_speed} m/s")
        else:
            print("Impossible d'afficher les informations météo complètes.")
    else:
        print("Les données météo ne sont pas disponibles.")

def main():
    api_key = "votre_api_key"  # Remplacez par votre clé API

    while True:
        city = input("Entrez le nom de la ville (ou 'q' pour quitter) : ")
        if city.lower() == 'q':
            print("Fin du programme.")
            break

        weather_data = get_weather_data(city, api_key)

        if weather_data:
            display_weather_info(weather_data)
        else:
            print("La récupération des données a échoué. Veuillez réessayer plus tard.")

if __name__ == '__main__':
    main()
