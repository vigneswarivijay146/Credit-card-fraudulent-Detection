
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

model = load_model('fraud_detection_model.h5')

def preprocess_input(df):
    df = df.copy()
    df['Amount'] = (df['Amount'] - df['Amount'].mean()) / df['Amount'].std()
    return np.reshape(df.values, (df.shape[0], df.shape[1], 1))

def predict_transactions(df):
    X = preprocess_input(df)
    preds = model.predict(X)
    return (preds > 0.5).astype(int).flatten()
