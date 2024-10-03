import pandas as pd

from sklearn.model_selection import train_test_split

def load_data(path):
    return pd.read_csv(path)

def clean_data():
    return

def split_data(df):
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def data_engineering():
    df = load_data("/opt/airflow/data/raw/heart-disease.csv")
    X_train, X_test, y_train, y_test = split_data(df)
    X_train.to_csv('/opt/airflow/data/processed/X_train.csv', index=False)
    X_test.to_csv('/opt/airflow/data/processed/X_test.csv', index=False)
    y_train.to_csv('/opt/airflow/data/processed/y_train.csv', index=False)
    y_test.to_csv('/opt/airflow/data/processed/y_test.csv', index=False)
