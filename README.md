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

---

## 💻 **Installation**

### Prérequis
- **Python** : Version 3.8 ou supérieure.
- **pip** : Pour la gestion des dépendances Python.

### Étapes d'installation
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/DavidLUTALA/Systeme-d-analyse-et-de-prediction-des-donnees-sur-la maladie-d-Alzheimers
```

2. Installer les dépendances :
   ```bash
   pip install pandas numpy streamlit matplotlib sklearn xgboost catboost seaborn numpy pillow
   ```

3. Lancer l'application :
   ```bash
   streamlit run app.py
   ```
