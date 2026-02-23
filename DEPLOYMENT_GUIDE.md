# 🚀 GUIDE DE DÉPLOIEMENT STREAMLIT CLOUD
## Étape par étape - Football Database Analysis

---

## 📋 PRÉREQUIS

Avant de commencer, assurez-vous d'avoir :
- ✅ Un compte GitHub (gratuit) - https://github.com
- ✅ Tous les fichiers du projet prêts
- ✅ L'application testée en local et fonctionnelle

---

## 📂 ÉTAPE 1 : PRÉPARER LES FICHIERS

### Structure finale à vérifier :
```
football_project/
│
├── app.py                    # Application Streamlit principale
├── matches.csv               # Dataset
├── requirements.txt          # Dépendances Python
├── README.md                 # Documentation
├── .gitignore               # Fichiers à ignorer
├── PRESENTATION_GUIDE.md    # Guide de présentation (optionnel)
└── AUTO_EVALUATION.md       # Auto-évaluation (optionnel)
```

### ⚠️ FICHIERS OBLIGATOIRES :
1. **app.py** - Doit être exactement nommé ainsi
2. **matches.csv** - Dataset
3. **requirements.txt** - Liste des packages

---

## 🔧 ÉTAPE 2 : VÉRIFIER requirements.txt

Ouvrez `requirements.txt` et vérifiez qu'il contient :

```
streamlit==1.31.0
pandas==2.2.0
matplotlib==3.8.2
numpy==1.26.3
```

**⚠️ Important :** 
- Pas d'espaces autour du `==`
- Pas de ligne vide à la fin
- Versions compatibles

---

## 🌐 ÉTAPE 3 : CRÉER UN REPOSITORY GITHUB

### 3.1 Créer le repository
1. Allez sur https://github.com
2. Cliquez sur le bouton vert **"New"** (en haut à droite)
3. Remplissez :
   - **Repository name :** `football-database-analysis`
   - **Description :** "Analyse des performances footballistiques européennes"
   - **Visibilité :** Public ✅ (obligatoire pour Streamlit gratuit)
   - **Initialize :** Ne cochez RIEN (ni README, ni .gitignore, ni licence)
4. Cliquez sur **"Create repository"**

### 3.2 Prendre note de l'URL
Vous verrez une page avec une URL du type :
```
https://github.com/VOTRE-USERNAME/football-database-analysis.git
```

**Copiez cette URL**, vous en aurez besoin.

---

## 💻 ÉTAPE 4 : POUSSER LE CODE SUR GITHUB

### Option A : Via l'interface GitHub (plus simple)

1. Sur la page de votre nouveau repository, cliquez sur **"uploading an existing file"**

2. Glissez-déposez TOUS les fichiers :
   - app.py
   - matches.csv
   - requirements.txt
   - README.md
   - .gitignore

3. En bas de la page :
   - Commit message : "Initial commit - Football Database"
   - Cliquez sur **"Commit changes"**

✅ Vos fichiers sont maintenant sur GitHub !

---

### Option B : Via Git en ligne de commande (plus pro)

**Sur Windows :**
1. Ouvrir Git Bash (ou PowerShell)
2. Naviguer vers le dossier :
```bash
cd chemin/vers/football_project
```

**Sur Mac/Linux :**
1. Ouvrir Terminal
2. Naviguer vers le dossier :
```bash
cd /chemin/vers/football_project
```

**Ensuite (pour tous) :**

```bash
# Initialiser Git
git init

# Ajouter tous les fichiers
git add .

# Vérifier les fichiers ajoutés
git status

# Créer le premier commit
git commit -m "Initial commit - Football Database"

# Connecter au repository GitHub (remplacez VOTRE-USERNAME)
git remote add origin https://github.com/VOTRE-USERNAME/football-database-analysis.git

# Pousser le code
git push -u origin main
```

**Si erreur "branch master" au lieu de "main" :**
```bash
git branch -M main
git push -u origin main
```

**Si demande d'authentification :**
- Username : votre nom d'utilisateur GitHub
- Password : utilisez un Personal Access Token (pas votre mot de passe)
  - Créer un token : GitHub → Settings → Developer settings → Personal access tokens

✅ Vos fichiers sont maintenant sur GitHub !

---

## 🎯 ÉTAPE 5 : DÉPLOYER SUR STREAMLIT CLOUD

### 5.1 Créer un compte Streamlit Cloud

1. Allez sur https://streamlit.io/cloud
2. Cliquez sur **"Sign up"**
3. Choisissez **"Continue with GitHub"**
4. Autorisez Streamlit à accéder à vos repositories GitHub
5. Suivez les instructions de connexion

### 5.2 Déployer l'application

1. Une fois connecté, cliquez sur **"New app"**

2. Remplissez le formulaire :
   
   **Repository :**
   - Sélectionnez `VOTRE-USERNAME/football-database-analysis`
   
   **Branch :**
   - Laissez `main` (ou `master` selon votre config)
   
   **Main file path :**
   - Tapez exactement : `app.py`
   
   **App URL (optionnel) :**
   - Vous pouvez personnaliser : `football-analysis-VOTRENOM`
   - Sinon, une URL auto sera générée

3. Cliquez sur **"Deploy!"**

### 5.3 Attendre le déploiement

Vous verrez une page avec :
- Des logs qui défilent
- Un indicateur de progression
- Messages du type "Building", "Installing dependencies", "Running app"

⏱️ **Temps estimé : 2-5 minutes**

---

## ✅ ÉTAPE 6 : VÉRIFIER LE DÉPLOIEMENT

### 6.1 Indicateurs de succès

Quand c'est prêt, vous verrez :
- ✅ Statut : "Your app is live!"
- ✅ Une URL : `https://VOTRE-APP.streamlit.app`
- ✅ L'application s'affiche

### 6.2 Tests à faire

1. **Test des filtres :**
   - Changez la saison → Les chiffres doivent changer
   - Changez la ligue → Les graphiques doivent se mettre à jour
   - Sélectionnez une équipe → L'analyse détaillée doit apparaître

2. **Test des graphiques :**
   - Vérifiez que les 3 graphiques s'affichent
   - Vérifiez qu'ils sont interactifs (survoler avec la souris)

3. **Test des données :**
   - Vérifiez que les métriques sont cohérentes
   - Vérifiez que le tableau value_counts() s'affiche

### 6.3 Si tout fonctionne

🎉 **FÉLICITATIONS !** Votre application est en ligne !

**Notez l'URL finale :** `https://votre-app.streamlit.app`

Vous pouvez la partager avec :
- Votre professeur
- Vos camarades
- Sur votre CV !

---

## 🐛 ÉTAPE 7 : DÉPANNAGE (SI PROBLÈMES)

### Problème 1 : "Module not found"

**Cause :** Package manquant dans requirements.txt

**Solution :**
1. Ajoutez le package manquant dans `requirements.txt`
2. Commitez et poussez :
```bash
git add requirements.txt
git commit -m "Fix: ajout du package manquant"
git push
```
3. L'app se redéploiera automatiquement

---

### Problème 2 : "File not found: matches.csv"

**Cause :** Le fichier CSV n'est pas dans le repository

**Solution :**
1. Vérifiez sur GitHub que `matches.csv` est bien présent
2. Si absent, ajoutez-le :
```bash
git add matches.csv
git commit -m "Add dataset"
git push
```

---

### Problème 3 : L'app se relance en boucle

**Cause :** Erreur dans le code

**Solution :**
1. Regardez les logs sur Streamlit Cloud
2. Identifiez l'erreur
3. Corrigez dans `app.py`
4. Poussez la correction :
```bash
git add app.py
git commit -m "Fix: correction de l'erreur"
git push
```

---

### Problème 4 : Les graphiques ne s'affichent pas

**Cause :** Problème d'import matplotlib

**Solution :**
Vérifiez dans `requirements.txt` :
```
matplotlib==3.8.2
```

Si absent, ajoutez-le et poussez.

---

### Problème 5 : "Your app has exceeded its resource limits"

**Cause :** Dataset trop volumineux ou calculs trop lourds

**Solution :**
1. Utilisez `@st.cache_data` (déjà implémenté)
2. Réduisez la taille du dataset si nécessaire

---

## 🔄 ÉTAPE 8 : METTRE À JOUR L'APPLICATION

Si vous voulez modifier quelque chose après le déploiement :

1. **Modifiez le fichier localement** (par exemple `app.py`)

2. **Poussez les changements :**
```bash
git add .
git commit -m "Update: description de la modification"
git push
```

3. **Attendez le redéploiement automatique** (1-2 minutes)

✅ Vos modifications sont en ligne !

---

## 📱 ÉTAPE 9 : PARTAGER VOTRE APPLICATION

### URL à partager
```
https://votre-app.streamlit.app
```

### Exemples d'utilisation

**Pour le rendu :**
Ajoutez l'URL dans votre README.md :
```markdown
## 🌐 Application en ligne
L'application est accessible à : https://votre-app.streamlit.app
```

**Pour la présentation :**
Affichez l'URL sur votre slide de conclusion.

**Pour votre portfolio :**
Ajoutez le lien sur votre CV ou LinkedIn.

---

## 🎓 ÉTAPE 10 : PRÉPARER LE RENDU

### 10.1 README.md à jour

Vérifiez que votre README contient :
```markdown
## 🌐 Déploiement

L'application est déployée et accessible en ligne :
👉 https://votre-app.streamlit.app

### Repository GitHub
Le code source est disponible sur :
👉 https://github.com/VOTRE-USERNAME/football-database-analysis
```

### 10.2 Document de rendu

Créez un document PDF avec :
1. **Page 1 :** Titre du projet + votre nom
2. **Page 2 :** Problématique
3. **Page 3 :** Dataset utilisé
4. **Page 4 :** Captures d'écran de l'app
5. **Page 5 :** URL de déploiement + URL GitHub
6. **Page 6 :** Auto-évaluation

### 10.3 Infographie

Créez une infographie (Canva, PowerPoint) avec :
- Chiffres clés du projet
- Graphiques principaux
- Insights principaux
- Technologies utilisées

---

## ✅ CHECKLIST FINALE AVANT RENDU

### GitHub
- [ ] Repository créé
- [ ] Tous les fichiers poussés
- [ ] README.md complet
- [ ] Repository public

### Streamlit Cloud
- [ ] Application déployée
- [ ] URL fonctionnelle
- [ ] Tous les filtres testés
- [ ] Graphiques s'affichent
- [ ] Aucune erreur dans les logs

### Documentation
- [ ] README.md à jour avec URL
- [ ] AUTO_EVALUATION.md complété
- [ ] PRESENTATION_GUIDE.md lu
- [ ] Infographie créée

### Tests
- [ ] App testée sur ordinateur
- [ ] App testée sur mobile
- [ ] Filtres fonctionnent
- [ ] Métriques correctes
- [ ] Graphiques lisibles

---

## 🎉 RÉSULTAT FINAL

Vous devez avoir :

1. ✅ **Application en ligne** : `https://votre-app.streamlit.app`
2. ✅ **Code source public** : `https://github.com/VOTRE-USERNAME/football-database-analysis`
3. ✅ **Documentation complète** : README + guides
4. ✅ **Application testée** : Tout fonctionne

---

## 💡 CONSEILS SUPPLÉMENTAIRES

### Pour la présentation
- Ouvrez l'URL en ligne (pas en local)
- Testez sur le réseau de l'école AVANT la présentation
- Préparez un plan B si Internet tombe (screenshots)

### Pour le professeur
- Ajoutez un fichier `CREDITS.md` mentionnant les sources
- Commentez bien votre code
- Ajoutez des docstrings aux fonctions

### Pour votre portfolio
- Faites un beau screenshot de l'app
- Rédigez un article Medium/LinkedIn sur le projet
- Ajoutez-le sur votre CV

---

## 📞 BESOIN D'AIDE ?

### Ressources officielles
- Documentation Streamlit : https://docs.streamlit.io
- Forum Streamlit : https://discuss.streamlit.io
- Documentation Pandas : https://pandas.pydata.org/docs/

### Problèmes courants
- Cherchez sur Stack Overflow
- Consultez les logs de déploiement
- Vérifiez le forum Streamlit

---

## 🎯 VOUS ÊTES PRÊT !

Suivez ce guide étape par étape et votre application sera en ligne en 20 minutes maximum !

**Bonne chance pour votre projet ! ⚽📊**
