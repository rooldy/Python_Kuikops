#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[25]:


# Chargement des fichiers
cities = pd.read_csv("Data/cities.csv")
population = pd.read_csv("Data/Population_data.csv")


# In[26]:


cities.head(10)


# In[27]:


population.head(10)


# In[28]:


cities.dtypes


# In[29]:


population.dtypes


# In[30]:


cities.info()


# In[31]:


population.info()


# In[36]:


print(cities.columns)


# In[37]:


print(population.columns)


# In[38]:


# Nettoyer les noms de colonnes en enlevant les espaces et les guillemets
cities.columns = cities.columns.str.strip().str.replace('"', '')

# Nettoyer les noms de colonnes
population.columns = population.columns.str.strip().str.replace('"', '')


# In[39]:


## Question 1 - Ajouter une colonne "Latitude totale" et "Longitude totale" dans cities.csv

cities["Latitude totale"] = cities["LatD"] + (cities["LatM"] / 60) + (cities["LatS"] / 3600)

# Calcul de la longitude en degrés décimaux
cities["Longitude totale"] = cities["LonD"] + (cities["LonM"] / 60) + (cities["LonS"] / 3600)

# Affichage des résultats
print(cities[['City', 'Latitude totale', 'Longitude totale']])


# In[42]:


## Question 2- Filtrer les villes situées dans l'hémisphère Nord (NS == 'N')
df_hemisphere_nord = cities[cities['NS'] == 'N']
print(df_hemisphere_nord)


# In[43]:


cities['City']


# In[44]:


population['City']


# In[45]:


# Nettoyer les noms de colonnes pour enlever les espaces
cities.columns = cities.columns.str.strip()
population.columns = population.columns.str.strip()


# In[46]:


## Question 3 - Fusion des deux DataFrames sur "City"
combine_data = pd.merge(cities, population, on='City', how='left')
print(combine_data)


# In[50]:


population.columns = population.columns.str.strip()


# In[52]:


## Question 4 - Calcul de la population projetée pour 2025
combine_data['Population_2025'] = combine_data['Population_2020'] * (1 + combine_data['Growth_rate'] / 100) ** 5
print(combine_data[['City', 'Population_2020', 'Growth_rate', 'Population_2025']])


# In[58]:


print(population.columns)


# In[62]:


## Question 5 - Afficher les villes dont la population projetée en 2025 dépasse 1 million
valeur = 1000000
population_sup_1_million = combine_data[combine_data['Population_2025'] > valeur]
print(population_sup_1_million[['City', 'Population_2025']])


# In[53]:


## Question 6 - Créer un graphique à barres des 10 villes avec la population projetée la plus élevée
top_10_villes = combine_data.sort_values(by='Population_2025', ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.bar(top_10_villes['City'], top_10_villes['Population_2025'], color='skyblue')
plt.title('Top 10 des villes avec la population projetée la plus élevée en 2025', fontsize=14)
plt.xlabel('Villes', fontsize=12)
plt.ylabel('Population projetée en 2025', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[60]:


print(combine_data.columns)


# In[69]:


## Question 7 - Calculer la densité de population (habitants/km²)

# Générer des valeurs aléatoires pour les colonnes 'Population' et 'Area'
combine_data['Population'] = np.random.uniform(100000, 10000000, size=len(combine_data))  # Population entre 100,000 et 10,000,000
combine_data['Area'] = np.random.uniform(10, 5000, size=len(combine_data))  # Superficie entre 10 km² et 5000 km²

# Calculer la densité de population (habitants/km²)
combine_data['Densité_population'] = combine_data['Population_2025'] / combine_data['Area']

# Afficher les premières lignes du DataFrame avec les nouvelles colonnes
print(combine_data[['City', 'Population', 'Area', 'Densité_population']].head())


# In[78]:


## Question 8 - Trouver la ville la plus grande et la plus petite population

# Trouver la ville avec la population maximale
max_population = combine_data.loc[combine_data['Population'].idxmax()]

# Trouver la ville avec la population minimale
min_population = combine_data.loc[combine_data['Population'].idxmin()]

# Afficher les résultats
print("La ville avec la plus grande population est : {}".format(cities_max_population['City']))
print("La ville avec la plus petite population est : {}".format(cities_min_population['City']))


# In[79]:


## Question 9 - Filtrer les villes avec une densité de population supérieure à 5000 habitants/km2

# Calcul de la densité de population (habitants/km²)
combine_data['Densité_population'] = combine_data['Population'] / combine_data['Area']

# Filtrer et afficher les villes avec une densité > 5000 habitants/km²
villes_densite_superieure_5000 = combine_data[combine_data['Densité_population'] > 5000]

# Affichage des résultats
print("Villes avec une densité de population supérieure à 5000 habitants/km² est :{}")
print(villes_densite_superieure_5000[['City', 'Densité_population']])


# In[80]:


## Question 10 - Trouver la moyenne et la médiane de la population des villes

moyenne_population = combine_data['Population'].mean

mediane_population = combine_data['Population'].median

# Affichage des résultats
print("Moyenne de la population des villes : {}".format(moyenne_population))
print("Médiane de la population des villes : {}".format(mediane_population))


# In[88]:


## Question 11 - Créer une nouvelle colonne de la population normalisée

Population_normalisee = (combine_data['Population'] - min_population.Population) / (max_population.Population - min_population.Population)
#print(min_population)
# Affichage du DataFrame avec la nouvelle colonne
print(combine_data)


# In[90]:


## Question 12 - Utiliser Numpy pour créer un tableau de statistiques descriptives


# Calcul des statistiques descriptives pour la colonne 'Population'
mean_population = np.mean(combine_data['Population'])      # Moyenne
std_population = np.std(combine_data['Population'], ddof=0)  # Écart-type
min_population = np.min(combine_data['Population'])         # Minimum
max_population = np.max(combine_data['Population'])         # Maximum

# Création d'un tableau des résultats
stats = {
    'Moyenne': mean_population,
    'Écart-type': std_population,
    'Minimum': min_population,
    'Maximum': max_population
}

# Afficher les statistiques
print("Statistiques descriptives pour la colonne 'Population':")
print(stats)

