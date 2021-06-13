import pandas as pd
from pathlib import Path
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from imblearn.combine import SMOTEENN
from collections import Counter
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier


def import_data(s3_url):
    raw_data = pd.read_csv(s3_url)
    return raw_data


def preprocess_raw_data(raw_df):

    numerical_cols = raw_df.dtypes[raw_df.dtypes != 'object'].index.tolist()

    numerical_df = raw_df[numerical_cols]
    numerical_df.index = raw_df['#']

    selected_features = ['ppg', 'mpg', 'rpg', 'apg', 'spg', 'gp', 'tov', 'pk']
    data_df = numerical_df[selected_features]

    X = data_df.drop(columns=['pk'])
    y = data_df['pk'].apply(lambda x: 1 if x <= 60 else 2)

    smoteenn = SMOTEENN(random_state=1)
    X_resampled, y_resampled = smoteenn.fit_resample(X, y)

    X_train, X_test, y_train, y_test = train_test_split(
        X_resampled, y_resampled, random_state=1)

    scaler = StandardScaler()
    X_scaler = scaler.fit(X_resampled)

    X_scaled = X_scaler.transform(X_resampled)

    training_data = [X_scaled, y_resampled]

    return training_data


def random_forest_model(X_train, y_train):

    rf = RandomForestClassifier(n_estimators=120, random_state=1)
    rf.fit(X_train, y_train)

    return rf


def predict_player(dict_of_stats, trained_model):
    player_df = pd.DataFrame([dict_of_stats])
    player_pred = trained_model.predict(player_df)

    return player_pred
