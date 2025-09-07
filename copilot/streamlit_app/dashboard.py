import os
import pandas as pd
import streamlit as st

# Always resolve the path relative to this file (dashboard.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "..", "data", "patient_data.csv")

# Load data
try:
    df = pd.read_csv(file_path)
    st.success("Patient data loaded successfully!")
except FileNotFoundError:
    st.error(f"CSV file not found at: {file_path}")
    st.stop()

# Example dashboard code
st.title("Patient Data Dashboard")
st.write("Showing preview of patient data:")
st.dataframe(df.head())
