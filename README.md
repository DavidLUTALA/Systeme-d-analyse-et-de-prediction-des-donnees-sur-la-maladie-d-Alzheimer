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
   git clone https://github.com/DavidLUTALA/Systeme-d-analyse-et-de-prediction-des-donnees-sur-la    maladie-d-Alzheimers
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

## 📊 **Ensemble de données**

### 1. Les Variables de notre jeu de données

Le projet utilise le jeu de données suivant :

### Informations des patients

- **PatientID :** Un identifiant unique attribué à chaque patient (4751 à 6900).

- **Âge :** L’âge des patients varie de 60 à 90 ans.

- **Gender :** Sexe des patients (Male ou Femelle).

- **Ethnicity :** L'origine ethnique des patients.

- **EducationLevel :** Le niveau d'éducation des patients.

##**Facteurs liés au mode de vie**

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

##**Évaluations cognitives et fonctionnelles**
**MMSE :** score du Mini-Mental State Examination, compris entre 0 et 30. Des scores inférieurs indiquent une déficience cognitive.

- **FunctionalAssessment :** Score d’évaluation fonctionnelle, allant de 0 à 10. Des scores plus faibles indiquent une déficience plus importante.

- **MemoryComplaints :** Présence de plaintes de mémoire (Oui ou Non).

- **BehavioralProblems :** Présence de problèmes de comportement (Oui ou Non).

- **ADL :** Score des activités de la vie quotidienne, allant de 0 à 10. Les scores les plus bas indiquent une plus grande déficience.

## Symptômes

- **Confusion :** Présence de confusion (Oui ou Non).

- **Disorientation :** Présence de désorientation (Oui ou Non).

- **PersonalityChanges :** Présence de changements de personnalité (Oui ou Non).

- **DifficultyCompletingTasks :** Présence de difficulté à terminer les tâches (Oui ou Non).

- **Forgetfulness :** Présence d'oubli (Oui ou Non).

## Informations sur le diagnostic

- **Diagnostic :** Statut du diagnostic de la maladie d'Alzheimer (Oui ou Non).

## Informations confidentielles

- **DoctorInCharge :** Cette colonne contient des informations confidentielles sur le médecin responsable, avec « XXXConfid » comme valeur pour tous les patients.

### 2. La Variable cible de notre jeu de données

Dans notre étude, la variable cible est **Diagnostic**, Cette variable catégorielle nous permet de prédire les individus ayant la maladie d'Alzheimer ou pas.
- **0** est équivalent à **No**
- **1** est équivalent à **Yes**

## 📊 **Methodes et techniques d'étude**

