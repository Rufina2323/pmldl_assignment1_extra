import pickle
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV


def apply_scaler(X_train, X_test):
    scaler = StandardScaler()
    x_train = scaler.fit_transform(X_train)
    x_test = scaler.transform(X_test)
    return scaler, x_train, x_test


def train_model(x_train, y_train):
    # Define the hyperparameter grid
    param_grid = {'n_neighbors': np.arange(1, 10),
                'weights': ['uniform', 'distance'],
                'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
                }

    knn = KNeighborsClassifier()

    grid = GridSearchCV(knn, param_grid, scoring='accuracy')
    grid.fit(x_train, y_train)

    # Create best model
    best_model = KNeighborsClassifier(n_neighbors=grid.best_params_['n_neighbors'],
                                    weights=grid.best_params_['weights'],
                                    algorithm=grid.best_params_['algorithm']
                                    )
    best_model.fit(x_train, y_train)
    return best_model


def evaluate_model(model, x_test, y_test):
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    print(classification_report(y_test, y_pred))


def save_file(model, path: str):
    with open(path, 'wb') as file:
        pickle.dump(model, file)


def model_engineering():
    scaler, x_train, x_test = apply_scaler(pd.read_csv("/opt/airflow/data/processed/X_train.csv"), pd.read_csv("/opt/airflow/data/processed/X_test.csv"))
    y_train = pd.read_csv("/opt/airflow/data/processed/y_train.csv")
    y_test = pd.read_csv("/opt/airflow/data/processed/y_test.csv")
    model = train_model(x_train, y_train)
    evaluate_model(model, x_test, y_test)
    save_file(model, '/opt/airflow/code/deployment/api/models/model.pkl')
    save_file(scaler, '/opt/airflow/code/deployment/api/models/scaler.pkl')
