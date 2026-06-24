import pandas as pd
import os

# Chargement
df = pd.read_csv('data/raw/website_wata.csv')

print("=== APERÇU INITIAL ===")
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())

# Nettoyage
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Renommer les colonnes
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Sauvegarder
os.makedirs('data/processed', exist_ok=True)
df.to_csv('data/processed/trafic_nettoye.csv', index=False)

print("=== RÉSULTAT ===")
print(df.shape)
print("Fichier sauvegardé dans data/processed/")