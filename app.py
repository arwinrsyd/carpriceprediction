import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model yang telah dilatih dan disimpan
model = joblib.load("carprice_model.pkl")

st.title("Prediksi Harga Mobil")
st.write("Masukkan detail mobil untuk memprediksi harga jualnya:")

# Form input pengguna
with st.form("form_mobil"):
    carwidth = st.number_input("Lebar Mobil (carwidth)", min_value=50.0, max_value=80.0, step=0.1)
    carheight = st.number_input("Tinggi Mobil (carheight)", min_value=40.0, max_value=80.0, step=0.1)
    curbweight = st.number_input("Berat Mobil (curbweight)", min_value=1000, max_value=5000, step=1)
    enginesize = st.number_input("Ukuran Mesin (enginesize)", min_value=50, max_value=500, step=1)
    horsepower = st.number_input("Tenaga Kuda (horsepower)", min_value=40, max_value=400, step=1)
    highwaympg = st.number_input("Highway MPG", min_value=10, max_value=70, step=1)

    # Tambahan jika model butuh fitur kategorikal, misalnya:
    fueltype = st.selectbox("Tipe Bahan Bakar (fueltype)", ['gas', 'diesel'])
    aspiration = st.selectbox("Aspiration", ['std', 'turbo'])
    drivewheel = st.selectbox("Tipe Penggerak (drivewheel)", ['fwd', 'rwd', '4wd'])

    submit = st.form_submit_button("Prediksi")

if submit:
    # Data dimasukkan ke dalam dataframe (pastikan kolom sesuai model)
    input_data = pd.DataFrame({
        'carwidth': [carwidth],
        'carheight': [carheight],
        'curbweight': [curbweight],
        'enginesize': [enginesize],
        'horsepower': [horsepower],
        'highwaympg': [highwaympg],
        'fueltype': [fueltype],
        'aspiration': [aspiration],
        'drivewheel': [drivewheel]
    })

    # Prediksi harga
    prediksi_harga = model.predict(input_data)[0]
    st.success(f"Perkiraan Harga Mobil: ${prediksi_harga:,.2f}")
