# 🧠 Alzheimer’s Disease Data Analysis & Prediction System

### 🚀 Un système interactif de visualisation et de prédiction des données lié à la maladie d'Alzheimer.

![Banner](https://user-images.githubusercontent.com/your_image_placeholder/banner.png) <!-- Remplacez par une image de bannière si disponible -->

## 📌 **Table des matières**
1. [Aperçu du projet](#aperçu-du-projet)
2. [Fonctionnalités](#fonctionnalités)
3. [Architecture](#architecture)
4. [Installation](#installation)
5. [Utilisation](#utilisation)
6. [Dataset](#dataset)
7. [Résultats](#résultats)
8. [Technologies utilisées](#technologies-utilisées)
9. [Améliorations futures](#améliorations-futures)
10. [Contact](#contact)

---

## 📖 **Aperçu du projet**
Ce projet propose une solution complète pour explorer, analyser, et modéliser les données liées à la maladie d'Alzheimer. À travers une interface conviviale développée avec **Streamlit**, les utilisateurs peuvent :
- Visualiser les données brutes ou prétraitées.
- Analyser les corrélations entre variables avec des graphiques interactifs.
- Générer et évaluer des modèles de prédiction avancés pour la détection précoce.

> Ce projet illustre des compétences en **Data Science**, **Machine Learning**, et **développement d'applications interactives**, tout en mettant l'accent sur la présentation de résultats clairs et exploitables.

---

## ✨ **Fonctionnalités**
- **Page d'accueil intuitive** :
  - Présentation des objectifs du projet.
  - Informations sur le dataset utilisé.
  - Menu latéral facilitant la navigation.

- **Exploration des données** :
  - Affichage des 10 premières lignes ou du dataset complet.
  - Résumé statistique des données.

- **Visualisation interactive** :
  - Création de graphiques personnalisés (corrélation, histogrammes, boxplots).
  - Choix des variables à explorer via une interface utilisateur dynamique.

- **Modélisation et prédiction** :
  - Implémentation d'algorithmes de Machine Learning.
  - Visualisation des performances des modèles (accuracy, confusion matrix).
  - Interprétation des résultats pour une meilleure compréhension.

---

## 🛠 **Architecture**
Le projet est organisé de manière modulaire pour assurer la lisibilité et la maintenabilité :
```bash
├── app.py                # Application Streamlit principale
├── data/
│   └── alzheimers_disease_data3.csv # Dataset utilisé
├── models/
│   ├── model_evaluation.py  # Scripts pour évaluer les modèles
│   └── model_training.py    # Scripts pour entraîner les modèles
├── utils/
│   ├── preprocessing.py      # Fonctions de prétraitement
│   ├── visualization.py      # Génération de graphiques
│   └── helpers.py            # Utilitaires divers
└── README.md             # Document de présentation
```

---

## 💻 **Installation**

### Prérequis
- **Python** : Version 3.8 ou supérieure.
- **pip** : Pour la gestion des dépendances Python.

### Étapes d'installation
1. Cloner le dépôt :
   ```bash
   https://github.com/DavidLUTALA/Systeme-d-analyse-et-de-prediction-des-donnees-sur-la-maladie-d-Alzheimer.git
   ```

2. Installer les dépendances :
   ```bash
   pip install pandas numpy streamlit matplotlib sklearn xgboost catboost seaborn numpy pillow
   ```

3. Lancer l'application :
   ```bash
   streamlit run app.py
   ```

---

## 🎯 **Utilisation**

### 1. Choisissez une option depuis le menu latéral :
- Introduction.
- Aperçu des Données.
- Prétraitement des Données.
- Modélisation
- Visualisations

### 2. Interagissez avec les graphiques et les options pour personnaliser vos analyses :
### 3. Obtenez des résultats des prédictions pour des différents modèles ou pour le jeu de données complet.

---

## 📊 **Ensemble de données**

### 1. Les Variables de notre jeu de données

Le projet utilise le jeu de données suivant :

### Informations des patients

- **PatientID :** Un identifiant unique attribué à chaque patient (4751 à 6900).

- **Âge :** L’âge des patients varie de 60 à 90 ans.

- **Gender :** Sexe des patients (Male ou Femelle).

- **Ethnicity :** L'origine ethnique des patients.

- **EducationLevel :** Le niveau d'éducation des patients.

### **Facteurs liés au mode de vie**

- **BMI :** Indice de Masse Corporelle des patients, allant de 15 à 40.

- **Smoking :** Statut de fumeur (Oui ou Non).

- **AlcoholConsumption :** Consommation hebdomadaire d'alcool en unités, allant de 0 à 20.

- **PhysicalActivity :** Activité physique hebdomadaire en heures, allant de 0 à 10.

- **DietQuality :** Score de qualité du régime alimentaire, allant de 0 à 10.

- **SleepQuality :** Score de qualité du sommeil, allant de 4 à 10.

##**Antécédents médicaux**

- **FamilyHistoryAlzheimers :** Antécédents familiaux de la maladie d'Alzheimer (Oui ou Non).

- **CardiovascularDisease :** Présence d’une maladie cardiovasculaire (Oui ou Non).

- **Diabetes :** Présence de diabète (Oui ou Non).

- **Depression :** Présence de dépression (Oui ou Non).

- **HeadInjury :** Antécédents de traumatisme crânien (Oui ou Non)i.

- **Hypertension :** Présence d’hypertension (Oui ou Non).

### Mesures cliniques

- **SystolicBP :** Pression artérielle systolique, comprise entre 90 et 180 mmHg.

- **DiastolicBP :** Pression artérielle diastolique, comprise entre 60 et 120 mmHg.

- **CholestérolTotal :** Taux de cholestérol total, compris entre 150 et 300 mg/dL.

- **CholestérolLDL :** Taux de cholestérol des lipoprotéines de basse densité, compris entre 50 et 200 mg/dL.

- **CholestérolHDL :** Taux de cholestérol des lipoprotéines de haute densité, compris entre 20 et 100 mg/dL.

- **CholestérolTriglycérides :** Taux de triglycérides, variant de 50 à 400 mg/dL.

### **Évaluations cognitives et fonctionnelles**
**MMSE :** score du Mini-Mental State Examination, compris entre 0 et 30. Des scores inférieurs indiquent une déficience cognitive.

- **FunctionalAssessment :** Score d’évaluation fonctionnelle, allant de 0 à 10. Des scores plus faibles indiquent une déficience plus importante.

- **MemoryComplaints :** Présence de plaintes de mémoire (Oui ou Non).

- **BehavioralProblems :** Présence de problèmes de comportement (Oui ou Non).

- **ADL :** Score des activités de la vie quotidienne, allant de 0 à 10. Les scores les plus bas indiquent une plus grande déficience.

### Symptômes

- **Confusion :** Présence de confusion (Oui ou Non).

- **Disorientation :** Présence de désorientation (Oui ou Non).

- **PersonalityChanges :** Présence de changements de personnalité (Oui ou Non).

- **DifficultyCompletingTasks :** Présence de difficulté à terminer les tâches (Oui ou Non).

- **Forgetfulness :** Présence d'oubli (Oui ou Non).

### Informations sur le diagnostic

- **Diagnostic :** Statut du diagnostic de la maladie d'Alzheimer (Oui ou Non).

### Informations confidentielles

- **DoctorInCharge :** Cette colonne contient des informations confidentielles sur le médecin responsable, avec « XXXConfid » comme valeur pour tous les patients.

### 2. La Variable cible de notre jeu de données

Dans notre étude, la variable cible est **Diagnostic**, Cette variable catégorielle nous permet de prédire les individus ayant la maladie d'Alzheimer ou pas.
- **0** est équivalent à **No**
- **1** est équivalent à **Yes**

---

## 📊 **Methodes et techniques d'anayse utilisées**
Les méthodes d'analyse utilisées dans votre projet incluent plusieurs approches pour explorer, visualiser et modéliser les données afin d'obtenir des insights significatifs et de prédire la probabilité de la maladie d'Alzheimer.
### 1. Analyse exploratoire des données (EDA)

- **Statistiques descriptives :** Moyenne, médiane, écart-type et distribution des données.
- **Analyse déscriptive univariée :** Tableau de fréquence des variables, catégorisation de nombres de patients par variable, Analyse de normalité.
- **Analyse déscriptive bivariée :** Analyse des relations entre les variables
- **Analyse déscriptive multiivariée :** Tableau de corrélation, Heatmap

### 2. Prétraitement des données

- **Encodage des variables catégoriques :** Conversion des colonnes textuelles en numériques avec LabelEncoder
- **Normalisation :** Normalisation des différentes variables pour assurer une échelle uniforme entre les fonctionnalités
- **Suppression des anomalies :** Identification et traitement des valeurs aberrantes dans des colonnes spécifiques

### 3. Modélisation prédictive

Plusieurs algorithmes de machine learning ont été testés pour prédire le diagnostic :

- Arbre de Décision
- Forêt Aléatoire
- K Plus Proche Voisins
- Regression Logistique
- SVM
- XGBoost
- CatBoost

### 4. Optimisation des modèles

- **Grid Search :** Nous l'avons utilisé pour optimiser les hyperparamètres des différents modèles implémentés. Cette méthode garantit que les modèles sont ajustés pour obtenir leurs performances maximales sur les données.
- **Validation croisée :** Nous avons utilisé la validation croisée k-fold (k=5) pour tester les modèles sur différents sous-ensembles de données et éviter les problèmes de surapprentissage.

### 5. Évaluation des modèles

Les modèles ont été évalués avec les métriques suivantes :
- **Précision :** Pourcentage de bonnes prédictions parmi l'ensemble des prédictions.
- **Rappel :** Proportion des cas positifs correctement identifiés.
- **F1-Score :** Moyenne harmonique entre précision et rappel, utile pour les données déséquilibrées.
- **Matrice de confusion :** Visualisation des prédictions correctes et des erreurs.

---

## 📈 **Résultats**

### 1. Comparaison des résultats des modèles testés


| Modèles | Précision | Rappel | F1-Score | 
| --- | --- | --- | --- |
| Arbre de Décision | 0.94 | 0.93 | 0.94 |
| Forêt Aléatoire | 0.94 | 0.91 | 0.92 |
| K Plus Proche Voisins | 0.58 | 0.58 | 0.58 |
| Regression Logistique | 0.82 | 0.83 | 0.82 |
| SVM | 0.61 | 0.63 | 0.62 |
| XGBoost | 0.96 | 0.96 | 0.96 |
| CatBoost | 0.95 | 0.95 | 0.95 |

### 2. Meilleur modèle
Après évalutaion de nos différents modèles, nous avons constaté que le modèle XGboost est le modèle le plus performant ayant un meilleur taux de prédiction.

---

## 🛠 **Technologies utilisées**

**Langue principale**
- **Python :** Pour le traitement des données, la modélisation et le développement de l'application.

**Bibliothèques et frameworks**
- **Streamlit :** Création de l'interface interactive.
- **Pandas :** Manipulation et analyse des données.
- **NumPy :** Calcul numérique.
- **Matplotlib & Seaborn :** Visualisation des données.
- **Scikit-learn :** Modélisation et évaluation des modèles.
- **Joblib :** Sauvegarde et chargement des modèles pré-entraînés.

## 🚀 **Améliorations futures**
Les améliorations envisagées pour la suite du projet :

1. Ajout de modèles avancés :
Intégration d'algorithmes des réseaux de neurones (Deep Learning).
2. Optimisation de la visualisation :
Ajout de graphiques interactifs avancés.
3. Exportation des prédictions au format CSV.
4. API REST :
Création d'une API REST pour permettre une intégration facile avec d'autres systèmes.

## 📬 **Contact**
Créé avec ❤️ par [David Lutala](https://github.com/DavidLUTALA)

📧 Email : [David Lutala](davidlutala0@gmail.com)
🌐 Portfolio : votre -portfolio .com
N'hésitez pas à me contacter pour toute question ou collaboration future ! 🙌

## 📱 Photos du système


