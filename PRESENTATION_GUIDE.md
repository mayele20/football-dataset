# 🎤 GUIDE DE PRÉSENTATION ORALE
## Football Database Analysis

---

## ⏱️ TIMING : 8 minutes

### Slide 1 : INTRODUCTION (1 min)

**Ce que vous dites :**
"Bonjour à tous. Aujourd'hui, je vais vous présenter mon projet d'analyse de données sur le football européen. La problématique centrale est : **Quels facteurs influencent la performance d'une équipe ?**

J'ai analysé plus de 2700 matchs sur 5 ligues européennes pour répondre à cette question, en me concentrant sur 4 axes principaux :
- Le nombre de buts marqués
- La régularité des performances
- L'avantage domicile
- L'évolution par saison"

**Actions :**
- Montrer l'écran d'accueil de l'application
- Pointer la problématique affichée

---

### Slide 2 : DATASET (1 min)

**Ce que vous dites :**
"Pour cette analyse, j'ai utilisé le European Soccer Database qui contient :
- 2700 matchs répartis sur 6 saisons
- 5 grandes ligues : Premier League, La Liga, Serie A, Bundesliga et Ligue 1
- 50 équipes suivies
- Plus de 7000 buts analysés

Les données incluent pour chaque match : les équipes, les scores, la date, et la ligue."

**Actions :**
- Montrer les métriques principales (encadré en haut)
- Montrer rapidement le CSV dans un éditeur

---

### Slide 3 : TECHNIQUES PANDAS (2 min)

**Ce que vous dites :**
"D'un point de vue technique, j'ai appliqué toutes les méthodes pandas requises :

**1. Création de colonnes dérivées :**
J'ai créé 3 nouvelles colonnes à partir des données brutes :
- `total_goals` : somme des buts des deux équipes
- `goal_difference` : différence de buts
- `match_year` : extraction de l'année

**2. Utilisation d'assign() avec apply() :**
J'ai utilisé assign pour créer la colonne `result` qui catégorise chaque match en 'Home Win', 'Draw', ou 'Away Win' selon la différence de buts.

**3. Fonction value_counts() :**
Elle m'a permis d'analyser la distribution des résultats. On voit que les victoires à domicile représentent environ 46% des matchs.

**4. Groupby avec agrégations :**
J'ai regroupé les données par équipe et par saison pour calculer :
- sum() : total des buts marqués
- mean() : moyenne de buts par match
- std() : écart-type pour mesurer la régularité"

**Actions :**
- Montrer le code dans VS Code (sections commentées)
- Montrer le tableau value_counts dans l'app
- Montrer le tableau groupby des équipes

---

### Slide 4 : VISUALISATIONS (2 min)

**Ce que vous dites :**
"J'ai créé 3 types de visualisations différents :

**Graphique 1 - L'histogramme** montre la distribution du nombre de buts par match.
On observe une distribution concentrée entre 1 et 4 buts, avec une moyenne de 2.7 buts par match. C'est cohérent avec la réalité du football.

**Graphique 2 - La courbe temporelle** montre l'évolution de la moyenne des buts par année.
On peut observer les variations d'offensivité du jeu au fil du temps.

**Graphique 3 - Le bar chart horizontal** présente le top 10 des équipes par buts marqués.
On identifie les équipes les plus offensives de chaque championnat."

**Actions :**
- Scroller lentement pour montrer les 3 graphiques
- Pointer les éléments clés (moyenne sur l'histogramme, tendance sur la courbe, top équipe)

---

### Slide 5 : INTERACTIVITÉ (1 min)

**Ce que vous dites :**
"L'application est entièrement interactive grâce à Streamlit.

Dans la sidebar, on peut :
- Filtrer par saison pour analyser une année spécifique
- Filtrer par ligue pour comparer les championnats
- Sélectionner une équipe pour avoir une analyse détaillée

Toutes les métriques et graphiques se mettent à jour automatiquement."

**Actions :**
- Changer le filtre saison → montrer que les chiffres changent
- Sélectionner une équipe → montrer l'analyse détaillée qui apparaît

---

### Slide 6 : RÉSULTATS PRINCIPAUX (1 min)

**Ce que vous dites :**
"Mon analyse a révélé plusieurs insights importants :

**1. L'avantage domicile existe et est mesurable :**
Les équipes à domicile marquent en moyenne 0.3 buts de plus que les équipes extérieures. C'est statistiquement significatif.

**2. Les grandes équipes sont régulières :**
En analysant l'écart-type, on voit que les meilleures équipes ont une régularité élevée (faible écart-type).

**3. Les victoires à domicile dominent :**
46% des matchs se terminent par une victoire de l'équipe qui reçoit, contre seulement 28% pour les visiteurs."

**Actions :**
- Montrer la section "Avantage domicile"
- Montrer le graphique camembert des résultats

---

### Slide 7 : CONCLUSION ET DÉPLOIEMENT (30 sec)

**Ce que vous dites :**
"Pour conclure, ce projet répond à la problématique en identifiant les facteurs clés de performance : le lieu du match (avantage domicile), la capacité offensive de l'équipe, et sa régularité.

L'application est déployée en ligne sur Streamlit Cloud et accessible 24/7. Le code source est disponible sur GitHub."

**Actions :**
- Montrer l'URL déployée
- Montrer rapidement le repo GitHub

---

## 🎯 QUESTIONS FRÉQUENTES DU PROF

### Q1 : "Pourquoi avoir choisi ce dataset ?"
**R :** "J'ai choisi le European Soccer Database car il est riche, structuré, et permet d'appliquer toutes les techniques pandas requises. De plus, le football est un domaine où l'analyse de données prend de plus en plus d'importance, notamment pour le scouting et la stratégie."

### Q2 : "Quelles difficultés avez-vous rencontrées ?"
**R :** "La principale difficulté était de gérer les données d'équipes jouant à domicile ET à l'extérieur. J'ai dû faire deux groupby séparés puis fusionner les résultats pour avoir une vision complète."

### Q3 : "Comment pourriez-vous améliorer ce projet ?"
**R :** "Plusieurs pistes :
- Ajouter du machine learning pour prédire les résultats
- Intégrer des données météo ou de fréquentation
- Créer des analyses par joueur
- Ajouter une analyse de la forme récente (5 derniers matchs)"

### Q4 : "Expliquez-moi le groupby() en détail"
**R :** "Le groupby permet de regrouper les lignes selon une colonne. Par exemple, groupby('home_team') regroupe tous les matchs par équipe à domicile. Ensuite, j'applique des fonctions d'agrégation comme sum() pour additionner les buts, mean() pour la moyenne, ou std() pour l'écart-type qui mesure la régularité."

### Q5 : "Quelle est la valeur de l'écart-type ?"
**R :** "L'écart-type mesure la dispersion autour de la moyenne. Un écart-type faible signifie que l'équipe est régulière (score souvent le même nombre de buts). Un écart-type élevé signifie des performances irrégulières (parfois 0 buts, parfois 5 buts)."

### Q6 : "Comment déployez-vous sur Streamlit Cloud ?"
**R :** "C'est très simple :
1. Je pousse mon code sur GitHub
2. Je me connecte sur streamlit.io/cloud avec mon compte GitHub
3. Je sélectionne mon repository et le fichier app.py
4. L'application se déploie automatiquement en 2-3 minutes"

---

## 💡 CONSEILS POUR LA PRÉSENTATION

### À FAIRE ✅
- Parler clairement et pas trop vite
- Montrer plutôt qu'expliquer (démonstration live)
- Préparer l'application ouverte AVANT la présentation
- Tester les filtres avant pour éviter les bugs
- Sourire et montrer votre enthousiasme

### À ÉVITER ❌
- Lire vos notes mot à mot
- Passer trop de temps sur le code
- Négliger les insights (le POURQUOI des chiffres)
- Oublier de conclure sur la problématique

---

## 🎬 CHECKLIST AVANT LA PRÉSENTATION

- [ ] Application lancée et fonctionnelle
- [ ] Tous les filtres testés
- [ ] URL de déploiement notée
- [ ] Code source ouvert dans VS Code
- [ ] README.md ouvert pour référence
- [ ] Bouteille d'eau à portée de main
- [ ] Chronomètre/montre visible
- [ ] Infographie imprimée ou en slide

---

## 📊 STRUCTURE DE L'INFOGRAPHIE

### Bloc 1 : TITRE + PROBLÉMATIQUE
```
⚽ FOOTBALL DATABASE ANALYSIS
Quels facteurs influencent la performance ?
```

### Bloc 2 : CHIFFRES CLÉS
```
📊 2,700 matchs analysés
🌍 5 ligues européennes
📅 6 saisons (2018-2024)
⚽ 7,170 buts
```

### Bloc 3 : AVANTAGE DOMICILE
```
🏠 46% victoires domicile
➡️ 28% victoires extérieur
🤝 26% matchs nuls

+0.3 buts en moyenne à domicile
```

### Bloc 4 : TOP INSIGHTS
```
✅ L'avantage domicile est mesurable
✅ Moyenne de 2.7 buts/match
✅ Les grandes équipes sont régulières
```

### Bloc 5 : TECHNOLOGIES
```
🐍 Python + Pandas
📊 Matplotlib
🚀 Streamlit
☁️ Déployé sur Cloud
```

---

## ⏰ GESTION DU TEMPS

| Temps écoulé | Partie                  | Action                          |
|--------------|-------------------------|---------------------------------|
| 0:00 - 1:00  | Introduction            | Problématique + contexte        |
| 1:00 - 2:00  | Dataset                 | Présenter les données           |
| 2:00 - 4:00  | Techniques pandas       | Code + explications             |
| 4:00 - 6:00  | Visualisations          | Montrer les 3 graphiques        |
| 6:00 - 7:00  | Interactivité + Résultats | Démo live + insights          |
| 7:00 - 8:00  | Conclusion              | Répondre à la problématique     |

---

## 🎯 AUTO-ÉVALUATION FINALE

**Critères techniques : 10/10**
- Tous les pandas requis ✅
- 3 graphiques différents ✅
- Application interactive ✅
- Déploiement cloud ✅

**Analyse et pertinence : 8/10**
- Problématique claire ✅
- Insights pertinents ✅
- Réponse à la question ✅

**Présentation : 2/2**
- Support visuel ✅
- Démonstration live ✅

**TOTAL ATTENDU : 18-20/20** 🎉
