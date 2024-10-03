# Bike Sharing Data Analysis Dashboard 🚴‍♂️
## Yermia Turangan / ML-07
## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda dari sistem *Capital Bikeshare* di Washington D.C. Menggunakan dataset yang mencakup data dari tahun 2011 hingga 2012, proyek ini berfokus pada pemahaman perilaku pengguna sepeda berdasarkan kondisi cuaca, musim, dan waktu.

## Dataset
Dataset yang digunakan terdiri dari dua file:
- `day.csv`: Data penyewaan sepeda yang diaggregasi berdasarkan har.
- `hour.csv`: Data penyewaan sepeda yang diaggregasi berdasarkan jam.

## Tujuan Proyek
1. Menganalisis pengaruh kondisi cuaca dan musim terhadap jumlah penyewaan sepeda.
2. Mengidentifikasi perbedaan perilaku antara pengguna terdaftar dan kasual.
3. Membuat visualisasi yang menggambarkan pola penyewaan sepeda.
4. Mengembangkan dashboard interaktif menggunakan Streamlit untuk menampilkan hasil analisis.

## Fitur
- Filter interaktif untuk memilih bulan dan kondisi cuaca.
- Visualisasi penyewaan berdasarkan cuaca dan musim.
- Analisis perilaku pengguna terdaftar dan kasual.

## Setup Environment - Anaconda
```bash
conda create --name bike-sharing-env python=3.9
conda activate bike-sharing-env
jupyter-notebook .
pip install -r requirements.txt

## Setup Environment - Shell/Terminal
```
mkdir bike_sharing_analysis
cd bike_sharing_analysis
pipenv install
pipenv shell
jupyter-notebook .
pip install -r requirements.txt


## Deploy
```
streamlit run [file].py
