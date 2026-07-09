# Pipeline de données — Analyse du trafic Web

Projet BI réalisé dans le cadre du Master 2 Génie Logiciel.  
Pipeline complet de collecte, traitement, stockage et analyse de données de trafic web.

---

## Équipe

| Membre | Rôle |
|--------|------|
| ndi-git | Chef de projet |
| sowlou | Collecte des données |
| gsidibeisidk-web | Traitement des données |
| AntaDiagne01 | Stockage des données |
| ahmadgueye | Analyse et Visualisation |

---

## Stack technique

| Couche | Outil |
|--------|-------|
| Langage | Python 3 |
| Traitement | Pandas, NumPy |
| Stockage | Amazon S3 (eu-west-3) |
| Analyse | Pandas, Matplotlib, Seaborn |
| Visualisation | Tableau Public |
| Versionning | Git + GitHub |
| Gestion projet | Trello |

---
## Structure du projet

```
pipeline-trafic-web/
├── data/
│   ├── raw/              # Données brutes (Kaggle)
│   └── processed/        # Données nettoyées et agrégées
├── notebooks/            # Analyse exploratoire (Jupyter)
├── scripts/
│   ├── traitement.py     # Nettoyage des données
│   └── stockage.py       # Upload vers Amazon S3
├── docs/                 # Rapport final
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone https://github.com/ndi-git/pipeline-trafic-web.git
cd pipeline-trafic-web
pip install -r requirements.txt
```

---

## Lancer le pipeline

```bash
# 1. Traitement des données
python scripts/traitement.py

# 2. Stockage sur S3
python scripts/stockage.py

# 3. Analyse (Jupyter)
jupyter notebook notebooks/analyse_trafic.ipynb
```

---

## Résultats clés

- **2 000 sessions** analysées
- **Organic** est le canal dominant (~40 % du trafic)
- **Referral** offre la meilleure qualité (rebond bas, conversion haute)
- Plus un visiteur revient, plus il convertit

---

## Source des données

Dataset public Kaggle — [Website Traffic](https://www.kaggle.com/datasets/anthonytherrien/website-traffic)  
Licence : CC BY-SA 4.0
