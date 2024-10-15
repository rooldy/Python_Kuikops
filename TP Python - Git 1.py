import pandas as pd
import matplotlib.pyplot as plt

# Chargement des fichiers
cities = pd.read_csv("C:/Users/RooldyALPHONSE/Desktop/Projet_Python_Kuikops/cities.csv", encoding='utf8')
population = pd.read_csv("C:/Users/RooldyALPHONSE/Desktop/Projet_Python_Kuikops/hw_200.csv", encoding='utf8')

## Question 1 - Ajouter une colonne "Latitude totale" et "Longitude totale" dans cities.csv
cities['Latitude totale'] = cities['LatD'] + (cities['LatM'] / 60) + (cities['LatS'] / 3600)
cities['Longitude totale'] = cities['LonD'] + (cities['LonM'] / 60) + (cities['LonS'] / 3600)

# Afficher un aperçu
print(cities[['City', 'Latitude totale', 'Longitude totale']].head())

## Question 2- Filtrer les villes situées dans l'hémisphère Nord (NS == 'N')
df_hemisphere_nord = cities[cities['NS'] == 'N']
print(df_hemisphere_nord)

## Question 3 - Fusion des deux DataFrames sur "City"
merged_data = pd.merge(cities, population, on='City', how='left')
print(merged_data.head())

## Question 4 - Calcul de la population projetée pour 2025
merged_data['Population_2025'] = merged_data['Population'] * (1 + merged_data['Growth_rate'] / 100) ** 5
print(merged_data[['City', 'Population', 'Growth_rate', 'Population_2025']])

## Question 5 - Afficher les villes dont la population projetée en 2025 dépasse 1 million
population_sup_1_million = merged_data[merged_data['Population_2025'] > 1_000_000]
print(population_sup_1_million[['City', 'Population_2025']])

## Question 6 - Créer un graphique à barres des 10 villes avec la population projetée la plus élevée
top_10_villes = merged_data.sort_values(by='Population_2025', ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.bar(top_10_villes['City'], top_10_villes['Population_2025'], color='skyblue')
plt.title('Top 10 des villes avec la population projetée la plus élevée en 2025', fontsize=14)
plt.xlabel('Villes', fontsize=12)
plt.ylabel('Population projetée en 2025', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

## Question 7 - Calculer la densité de population (habitants/km²)
merged_data['Densité_population'] = merged_data['Population'] / merged_data['Area']
print(merged_data[['City', 'Population', 'Area', 'Densité_population']].head())

## Question 8 - Trouver la ville avec la plus grande et la plus petite population


