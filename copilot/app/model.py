import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model():
    df = pd.read_csv('data/patient_data.csv')
    df['Diabetes'] = df['Diabetes'].map({'Yes': 1, 'No': 0})
    df['Gender'] = df['Gender'].map({'M': 0, 'F': 1})
    X = df[['Age', 'Gender', 'HeartRate', 'Diabetes']]
    y = df['Diagnosis'].map({'Normal': 0, 'Pre-Diabetes': 1, 'Hypertension': 2})
    model = RandomForestClassifier()
    model.fit(X, y)
    return model