import pickle
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('penyakit_jantung.sav', 'rb'))

# judul web
st.title('Prediksi Penyakit Jantung')

col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input('Usia')
with col2:
    sex = st.number_input('Jenis Kelamin (1 = Laki-laki, 0 = Perempuan)')
with col3:
    cp = st.number_input('Jenis Nyeri Dada (0-3)')
with col1:
    trestbps = st.number_input('Tekanan Darah Saat Istirahat')
with col2:
    chol = st.number_input('Kolesterol Serum (mg/dl)')
with col3:
    fbs = st.number_input('Gula Darah > 120 mg/dl (1 = Ya, 0 = Tidak)')
with col1:
    restecg = st.number_input('Hasil Elektrokardiografi Istirahat (0-2)')
with col2:
    thalach = st.number_input('Detak Jantung Maksimum')
with col3:
    exang = st.number_input('Angina yang Direspon oleh Olahraga (1 = Ya, 0 = Tidak)')
with col1:
    oldpeak = st.number_input('Depresi ST Dihasilkan oleh Olahraga Relatif terhadap Istirahat')
with col2:
    slope = st.number_input('Kemiringan Segmen ST (0-2)')
with col3:
    ca = st.number_input('Jumlah Pembuluh Darah Utama (0-4)')
with col1:
    thal = st.number_input('Thal (1 = Normal, 2 = Cacat Tetap, 3 = Cacat Reversibel)')

# Predict button
if st.button('Hasil Prediksi Penyakit Jantung'):
    try:
        # Convert inputs to numeric values
        features = np.array([
            float(age), float(sex), float(cp), float(trestbps),
            float(chol), float(fbs), float(restecg), float(thalach),
            float(exang), float(oldpeak), float(slope), float(ca), float(thal)
        ]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)

        # Display result
        if prediction[0] == 0:
            heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'
        else:
            heart_diagnosis = 'Pasien Terkena Penyakit Jantung'

        st.success(heart_diagnosis)
    except ValueError:
        st.error('Pastikan semua input diisi dengan nilai numerik yang valid.')