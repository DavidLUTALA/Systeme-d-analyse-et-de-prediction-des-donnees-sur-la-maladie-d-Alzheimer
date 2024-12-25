import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler

# Configuration Streamlit
st.set_page_config(
    page_title="Alzheimer Disease Prediction",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Ajouter du CSS pour le style
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            padding: 0;
        }
        .btn {
            width: 100%;
            padding: 15px;
            font-size: 16px;
            text-align: center;
            color: white;
            background-color: #4CAF50;
            border: none;
            margin-bottom: 10px;
            cursor: pointer;
        }
        .btn:hover {
            background-color: #45a049;
        }
        .block-container {
            padding: 0 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Charger le dataset automatiquement
try:
    df = pd.read_csv("alzheimers_disease_data3.csv")
except FileNotFoundError:
    st.error("Le fichier 'alzheimers_disease_data3.csv' est introuvable dans le dossier actuel. Veuillez vérifier.")

# Gestion des pages avec st.session_state
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Introduction"

# Gestion des pages avec des boutons
if st.sidebar.button("🔍 Introduction", key="btn_intro"):
    st.session_state["current_page"] = "Introduction"
if st.sidebar.button("📂 Aperçu des Données", key="btn_data"):
    st.session_state["current_page"] = "Aperçu des Données"
if st.sidebar.button("🔧 Prétraitement", key="btn_preprocess"):
    st.session_state["current_page"] = "Prétraitement"
if st.sidebar.button("🤖 Modélisation", key="btn_model"):
    st.session_state["current_page"] = "Modélisation"
if st.sidebar.button("📊 Visualisations", key="btn_visualize"):
    st.session_state["current_page"] = "Visualisations"

# Utiliser st.session_state pour afficher la bonne page
current_page = st.session_state["current_page"]

# Section : Introduction
if current_page == "Introduction":
    st.title("🔍 Alzheimer Disease Prediction")
    st.markdown(
        """
        🧠Bienvenue dans cette application de prédiction pour la maladie d'Alzheimer. 
        Vous pourrez : 
        
        Un système interactif de visualisation et de prédiction des données lié à la maladie d'Alzheimer.
        - Charger un dataset (pré-chargé automatiquement)
        - Prétraiter les données
        - Entraîner différents modèles de machine learning
        - Visualiser les résultats.
        """
    )
# Section : Aperçu des Données
elif current_page == "Aperçu des Données":
    st.title("📂 Aperçu des Données")
    if df is not None:
        st.write("Aperçu des données :")
        st.write(df.shape)
        st.dataframe(df)

        st.write("Statistiques descriptives :")
        st.write(df.describe())

        st.write("Nombre des lignes duppliquées :", sum(df.duplicated()))

        categorical_vars = df.select_dtypes(include=['object']).columns
        numeric_vars = df.select_dtypes(include=['number']).columns

        # Afficher la categorie de variables
        st.write("Variables catégorielles :", categorical_vars)
        st.write("Variables numériques :", numeric_vars)
    else:
        st.warning("Le dataset n'est pas chargé.")

# Section : Prétraitement des Données
elif current_page == "Prétraitement":
    st.title("🔧 Prétraitement des Données")
    if df is not None:
        # Suppression des colonnes inutiles
        if "PatientID" in df.columns:
            df = df.drop(columns=["PatientID"])
        if "DoctorInCharge" in df.columns:
            df = df.drop(columns=["DoctorInCharge"])

        # Encodage des variables catégorielles
        categorical_columns = df.select_dtypes(include="object").columns
        label_encoder = LabelEncoder()
        for col in categorical_columns:
            df[col] = label_encoder.fit_transform(df[col])

        # Normalisation des colonnes numériques
        numeric_columns = df.select_dtypes(include=["float64", "int64"]).columns
        scaler = MinMaxScaler()
        df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

        st.write("Données après prétraitement :")
        st.dataframe(df.head())
    else:
        st.warning("Le dataset n'est pas chargé.")

# Section : Modélisation
elif current_page == "Modélisation":
    st.title("🤖 Modélisation")
    if df is not None:

        categorical_vars = df.select_dtypes(include=['object']).columns
        numeric_vars = df.select_dtypes(include=['number']).columns

        labelencoder_X = LabelEncoder()
        for col in categorical_vars:
            df[col] = labelencoder_X.fit_transform(df[col])

        columns = ['Age', 'BMI', 'AlcoholConsumption', 'PhysicalActivity', 'DietQuality', 'SleepQuality', 'SystolicBP', 'DiastolicBP', 'CholesterolTotal', 'CholesterolLDL', 'CholesterolHDL', 'CholesterolTriglycerides', 'MMSE', 'FunctionalAssessment', 'ADL']

        #normalize the columns
        min_max_scaler = MinMaxScaler()
        df[columns] = min_max_scaler.fit_transform(df[columns])

        #standardize the columns
        standard_scaler = StandardScaler()
        df[columns] = standard_scaler.fit_transform(df[columns])


        # Séparation des données
        X = df.drop(columns=["Diagnosis"])
        y = df["Diagnosis"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Paramètres des modèles
        param_grids = {
            'Decision Tree': {'max_depth': [3, 5, 7, 12, None]},
            'Random Forest': {'n_estimators': [50, 100, 200], 'max_depth': [3, 5, 7, 12, None]},
            'K-Nearest Neighbors': {'n_neighbors': [3, 5, 7]},
            'Logistic Regression': {'C': [0.1, 1, 10]},
            'Support Vector Machine': {'C': [0.1, 1, 10], 'gamma': [0.1, 1, 'scale', 'auto']},
            'XGBoost': {'n_estimators': [50, 100, 200], 'learning_rate': [0.01, 0.1, 1], 'max_depth': [3, 5, 7]},
            'CatBoost': {'iterations': [50, 100, 200], 'learning_rate': [0.01, 0.1, 1]}
        }

        # Modèles disponibles
        models = {
            "Decision Tree": DecisionTreeClassifier(),
            "Random Forest": RandomForestClassifier(),
            "K-Nearest Neighbors": KNeighborsClassifier(),
            "Logistic Regression": LogisticRegression(),
            "Support Vector Machine": SVC(),
            "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric="logloss"),
            "CatBoost": CatBoostClassifier(verbose=0),
        }

        selected_model = st.selectbox("Choisissez un modèle", list(models.keys()))

        model = models[selected_model]
        grid_search = GridSearchCV(model, param_grids[selected_model], cv=5, scoring='f1')
        grid_search.fit(X_train, y_train)
        best_model = grid_search.best_estimator_

        # Afficher les résultats de la classification
        y_pred = best_model.predict(X_test)
        st.write(f"Classification Report pour {selected_model}:")
        st.text(classification_report(y_test, y_pred))

        st.write("Meilleurs paramètres trouvés:", grid_search.best_params_)
    else:
        st.warning("Le dataset n'est pas chargé.")

# Section : Visualisations
elif current_page == "Visualisations":
    st.title("📊 Visualisations")
    if df is not None:
        # Distribution de la variable cible
        st.subheader("Distribution de la variable cible")
        fig, ax = plt.subplots()
        df["Diagnosis"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
        st.pyplot(fig)

        # Matrice de corrélation
        numerical_features = df.select_dtypes(include=[np.number]).columns.tolist()
        st.subheader("Matrice de corrélation")
        fig, ax = plt.subplots(figsize=(30, 10))
        sns.heatmap(df[numerical_features].corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Le dataset n'est pas chargé.")
