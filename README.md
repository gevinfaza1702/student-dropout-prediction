# Proyek Akhir: Menyelesaikan Permasalahan Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang mengalami tantangan serius terkait angka dropout atau putus kuliah mahasiswa. Permasalahan ini berdampak pada reputasi institusi, perencanaan akademik, serta efisiensi anggaran pendidikan. Untuk itu, dibutuhkan solusi berbasis data untuk mendeteksi siswa yang berpotensi dropout secara dini, sehingga dapat dilakukan intervensi yang tepat.

## Permasalahan Bisnis

- Bagaimana memprediksi siswa yang berisiko tinggi mengalami dropout?
- Faktor apa saja yang paling berpengaruh terhadap keputusan siswa untuk dropout?
- Bagaimana menyajikan informasi dropout dalam bentuk dashboard interaktif agar mudah dimonitor oleh pihak manajemen?

## Cakupan Proyek

- Menerapkan algoritma machine learning untuk memprediksi siswa yang berisiko dropout.
- Melakukan eksplorasi dan visualisasi data (EDA) untuk memahami karakteristik siswa.
- Membuat prototype aplikasi prediksi berbasis Streamlit.
- Membuat dashboard interaktif menggunakan Looker Studio untuk memonitor performa siswa.

## Persiapan

**Sumber data**:  
[students_performance.csv (Dicoding)](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv)

**Setup environment**:

- Python 3.x
- Jupyter Notebook / Google Colab
- Streamlit
- Looker Studio
- scikit-learn, pandas, matplotlib, seaborn, joblib

---

## Business Dashboard

Dashboard ini dibuat menggunakan **Looker Studio** dan menampilkan berbagai visualisasi untuk memahami faktor-faktor dropout.  
Terdapat berbagai diagram seperti:

- Donut chart distribusi dropout berdasarkan gender
- Bar chart status pembayaran dan dropout
- Bar chart dropout berdasarkan beasiswa
- Bar chart distribusi jumlah siswa dropout
- Line chart rata-rata nilai masuk siswa berdasarkan umur

📊 Link Looker Studio:  
🔗 _(https://lookerstudio.google.com/reporting/7460b9b0-b7b6-4ba2-b5df-3917ec8b460a)_

---

## Menjalankan Sistem Machine Learning

Prototype sistem prediksi dropout dibuat menggunakan **Streamlit**.  
Pengguna dapat memasukkan data siswa seperti nilai, status keuangan, jurusan, dan sistem akan memprediksi apakah siswa berisiko dropout atau tidak.

🌐 Link Streamlit App:  
🔗 [https://student-dropout-prediction-kksxeauicgzexxcaxrzh4g.streamlit.app/](https://student-dropout-prediction-kksxeauicgzexxcaxrzh4g.streamlit.app/)

Untuk menjalankan secara lokal:

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Conclusion

Proyek ini berhasil membangun sistem prediksi dropout dengan akurasi model sebesar **88%**, menggunakan algoritma **RandomForestClassifier**.  
Beberapa fitur yang sangat berpengaruh dalam prediksi antara lain:

- Status pembayaran
- Status penerima beasiswa
- Umur saat pendaftaran

---

## Rekomendasi Action Items

- 🎯 Lakukan intervensi awal kepada siswa dengan skor akademik rendah dan belum membayar biaya pendidikan.
- 📈 Monitor siswa secara berkala melalui dashboard Looker Studio untuk mempermudah pengambilan keputusan manajemen.
- 🤝 Pertimbangkan pemberian bantuan keuangan atau bimbingan tambahan bagi siswa yang memiliki risiko tinggi dropout.
