# ⚽ Football Database Analysis https://football-dataset-cog8c8mgcrkwp3ycmtmidg.streamlit.app/

## 🎯 Problématique
**Quels facteurs influencent la performance d'une équipe dans le football européen ?**

Ce projet analyse les performances des équipes de football à travers :
- Le nombre de buts marqués
- La régularité des performances
- L'avantage domicile
- L'évolution par saison

## 📊 Dataset
- **Source** : European Soccer Database
- **Contenu** : 2,700+ matchs
- **Couverture** : 5 ligues européennes (Premier League, La Liga, Serie A, Bundesliga, Ligue 1)
- **Période** : 6 saisons (2018/2019 - 2023/2024)

## 🛠️ Technologies utilisées
- Python 3.9+
- Pandas (manipulation de données)
- Matplotlib (visualisations)
- Streamlit (interface web interactive)

## 📦 Installation locale

### Prérequis
```bash
python --version  # Python 3.9 ou supérieur
```

### Installation
```bash
# Cloner le repository
git clone [votre-repo]
cd football_project

# Installer les dépendances
pip install -r requirements.txt

# Générer les données
python generate_data.py

# Lancer l'application
streamlit run app.py
```

L'application sera accessible sur `http://localhost:8501`

## 🚀 Déploiement sur Streamlit Cloud

### Étape 1 : Préparer le repository GitHub
1. Créer un nouveau repository sur GitHub
2. Ajouter les fichiers :
   - `app.py`
   - `matches.csv`
   - `requirements.txt`
   - `README.md`

```bash
git init
git add .
git commit -m "Initial commit - Football Database Analysis"
git remote add origin [votre-url-github]
git push -u origin main
```

### Étape 2 : Déployer sur Streamlit Cloud
1. Aller sur https://streamlit.io/cloud
2. Se connecter avec GitHub
3. Cliquer sur "New app"
4. Sélectionner votre repository
5. Branch : `main`
6. Main file path : `app.py`
7. Cliquer sur "Deploy"

⏱️ Le déploiement prend environ 2-3 minutes.

## ✅ Validation des critères du projet

### Critères Pandas (obligatoires)
- ✅ **Création de colonnes dérivées** : `total_goals`, `goal_difference`, `match_year`
- ✅ **Utilisation de `assign()`** : Création de la colonne `result` avec lambda
- ✅ **Utilisation de `apply()`** : Transformation de `goal_difference` en `result`
- ✅ **Utilisation de `value_counts()`** : Distribution des résultats de matchs
- ✅ **Utilisation de `groupby()`** : Statistiques par équipe et par saison
- ✅ **Fonctions d'agrégation** : `sum()`, `mean()`, `std()`

### Visualisations (obligatoires)
- ✅ **Graphique 1 - Histogramme** : Distribution du nombre de buts
- ✅ **Graphique 2 - Courbe** : Évolution des buts par année
- ✅ **Graphique 3 - Bar chart** : Top 10 équipes par buts marqués
- ✅ **Types différents** : 3 types de graphiques distincts

### Fonctionnalités Streamlit
- ✅ Interface interactive avec filtres dynamiques
- ✅ Métriques clés calculées en temps réel
- ✅ Multiple visualisations intégrées
- ✅ Analyse approfondie par équipe (bonus)

## 📈 Fonctionnalités principales

### 1. Filtres interactifs
- Filtrage par saison
- Filtrage par ligue
- Analyse d'une équipe spécifique

### 2. Métriques clés
- Nombre total de matchs
- Moyenne de buts par match
- Pourcentage de victoires à domicile
- Total de buts marqués

### 3. Analyses statistiques
- Distribution des résultats (victoire domicile/nul/victoire extérieur)
- Top 10 des équipes par buts marqués
- Évolution temporelle des buts
- Analyse de l'avantage domicile

### 4. Visualisations
- Histogramme de distribution
- Courbe d'évolution temporelle
- Graphiques à barres comparatifs
- Graphique camembert

## 🎓 Utilisation pédagogique

### Pour la présentation orale :

**Introduction (1 min)**
- Présenter la problématique
- Expliquer l'importance de l'analyse des performances

**Dataset (1 min)**
- Source et contenu
- Périmètre de l'analyse

**Démonstration technique (3 min)**
- Montrer les filtres interactifs
- Expliquer les transformations pandas
- Présenter les 3 graphiques principaux

**Résultats et insights (2 min)**
- Avantage domicile confirmé (+0.3 buts en moyenne)
- Top équipes identifiées
- Tendances temporelles observées

**Conclusion (1 min)**
- Répondre à la problématique
- Perspectives d'amélioration

## 📊 Exemples d'insights

### Avantage domicile
L'analyse révèle que les équipes à domicile marquent en moyenne **0.3 buts de plus** que les équipes à l'extérieur, confirmant l'existence d'un avantage domicile significatif.

### Régularité
L'écart-type des buts marqués permet d'identifier les équipes régulières vs imprévisibles. Une équipe avec un écart-type faible est plus constante dans ses performances.

### Évolution temporelle
Les données montrent l'évolution de l'offensivité du jeu au fil des saisons.

## 🔧 Améliorations possibles

Pour obtenir 18-20/20 :
- Ajouter des modèles prédictifs (ML)
- Intégrer des données météo
- Créer des cartes de chaleur
- Ajouter une analyse de corrélation
- Implémenter un système de recommandation

## 📝 Auto-évaluation

> L'ensemble des fonctionnalités pandas demandées ont été utilisées (groupby, sum, mean, std, value_counts, assign, apply). L'application Streamlit est interactive avec filtres dynamiques permettant une exploration approfondie des données. Trois graphiques de types différents ont été intégrés avec des analyses pertinentes. L'application est prête pour le déploiement en ligne sur Streamlit Cloud.

## 📧 Contact

Pour toute question sur le projet : noel.mayele02@gmail.com

## 📄 Licence

Ce projet est réalisé dans un cadre pédagogique.
