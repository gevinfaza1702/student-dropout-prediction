import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model dan feature columns
model = joblib.load('model.pkl')
feature_columns = joblib.load('feature_columns.pkl')

st.set_page_config(page_title="Prediksi Dropout Siswa", page_icon="🎓", layout="centered")

# -----------------------------
# Header
# -----------------------------
st.title("🎓 Prediksi Siswa Berisiko Dropout")
st.markdown(
    "Masukkan informasi siswa untuk memprediksi apakah siswa berpotensi **dropout** atau tidak."
)

st.markdown("---")

# -----------------------------
# Form Input
# -----------------------------
with st.form("dropout_form"):
    input_data = {}
    st.subheader("📋 Informasi Siswa")

    for col in feature_columns:
        # Untuk data kategorikal (hasil dari one-hot encoding), kita inputkan angka
        input_data[col] = st.number_input(f"{col}", value=0.0)

    submitted = st.form_submit_button("Prediksi Dropout")

# -----------------------------
# Prediction
# -----------------------------
if submitted:
    X_input = pd.DataFrame([input_data])[feature_columns]
    prediction = model.predict(X_input)[0]
    probas = model.predict_proba(X_input)[0]

    st.markdown("---")
    st.subheader("🧠 Hasil Prediksi")

    if prediction == 1:
        st.error(f"⚠️ Siswa **berisiko dropout** dengan probabilitas {probas[1]*100:.2f}%")
    else:
        st.success(f"✅ Siswa **tidak berisiko dropout** dengan probabilitas {probas[0]*100:.2f}%")

    st.markdown("---")
    st.caption("📊 Model: RandomForestClassifier · Akurasi ±88%")
