import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load model dan nama kolom fitur
model = joblib.load('model.pkl')
feature_columns = joblib.load('feature_columns.pkl')

st.set_page_config(page_title="Prediksi Dropout", layout="centered")
st.title("🎓 Prediksi Siswa Berisiko Dropout")

st.markdown("""
Masukkan informasi siswa untuk memprediksi apakah siswa berpotensi **dropout** atau tidak.
""")

# Buat form input untuk semua fitur
input_data = {}

for col in feature_columns:
    input_data[col] = st.text_input(f"{col}", value="0")

# Konversi input jadi dataframe
input_df = pd.DataFrame([input_data])

# Ubah semua input ke float
try:
    input_df = input_df.astype(float)
except:
    st.error("❌ Input harus berupa angka. Periksa kembali nilai yang dimasukkan.")

# Prediksi
if st.button("Prediksi Dropout"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Siswa ini diperkirakan akan **dropout** (Probabilitas: {probability:.2f})")
    else:
        st.success(f"✅ Siswa ini diperkirakan **tidak dropout** (Probabilitas: {probability:.2f})")
