import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Memuat dataset
data_hari = pd.read_csv('day.csv')

# Mengubah tipe data dteday menjadi datetime
data_hari['dteday'] = pd.to_datetime(data_hari['dteday'])

# Sidebar untuk filter
st.sidebar.header("Filter Data")
selected_month = st.sidebar.selectbox('Pilih Bulan', data_hari['mnth'].unique())
selected_weather = st.sidebar.selectbox('Pilih Kondisi Cuaca', data_hari['weathersit'].unique())

# Filter data berdasarkan pilihan user
filtered_data = data_hari[(data_hari['mnth'] == selected_month) & (data_hari['weathersit'] == selected_weather)]

# Menampilkan ringkasan data
st.header("Ringkasan Data Penyewaan")
st.write(filtered_data.describe())

# Menampilkan Total Penyewaan
total_cnt = filtered_data['cnt'].sum()
total_registered = filtered_data['registered'].sum()
total_casual = filtered_data['casual'].sum()

st.subheader("Total Penyewaan")
st.write(f"Total Penyewaan: {total_cnt}")
st.write(f"Pengguna Terdaftar: {total_registered}")
st.write(f"Pengguna Kasual: {total_casual}")





# Visualisasi distribusi penyewaan sepeda
st.subheader("Distribusi Penyewaan Sepeda")

plt.figure(figsize=(10, 6))
sns.histplot(filtered_data['cnt'], kde=True, bins=30)
plt.title('Distribusi Penyewaan Sepeda')
st.pyplot(plt)


# Visualisasi pengaruh cuaca terhadap penyewaan sepeda
st.subheader("Pengaruh Kondisi Cuaca Terhadap Penyewaan Sepeda")

plt.figure(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=filtered_data)
plt.title('Pengaruh Kondisi Cuaca Terhadap Penyewaan Sepeda')
st.pyplot(plt)



# Visualisasi tren penyewaan per bulan
st.subheader("Tren Penyewaan Sepeda Berdasarkan Bulan")

monthly_trend = filtered_data.groupby('mnth')['cnt'].sum()
plt.figure(figsize=(10, 6))
monthly_trend.plot(kind='bar', color='skyblue')
plt.title('Tren Penyewaan Sepeda Berdasarkan Bulan')
st.pyplot(plt)


st.subheader("Statistik Dasar Pengguna Terdaftar dan Kasual")

total_registered = filtered_data['registered'].sum()
total_casual = filtered_data['casual'].sum()

avg_registered = filtered_data['registered'].mean()
avg_casual = filtered_data['casual'].mean()

var_registered = filtered_data['registered'].var()
var_casual = filtered_data['casual'].var()

st.write(f"Total Penyewaan Pengguna Terdaftar: {total_registered}")
st.write(f"Total Penyewaan Pengguna Kasual: {total_casual}")
st.write(f"Rata-rata Penyewaan Pengguna Terdaftar: {avg_registered:.2f}")
st.write(f"Rata-rata Penyewaan Pengguna Kasual: {avg_casual:.2f}")
st.write(f"Variansi Penyewaan Pengguna Terdaftar: {var_registered:.2f}")
st.write(f"Variansi Penyewaan Pengguna Kasual: {var_casual:.2f}")


# Sidebar tambahan untuk memilih hari kerja dan rentang bulan
selected_workingday = st.sidebar.radio('Hari Kerja atau Akhir Pekan?', ('Hari Kerja', 'Akhir Pekan'))
selected_months = st.sidebar.multiselect('Pilih Beberapa Bulan', data_hari['mnth'].unique(), default=data_hari['mnth'].unique())
selected_weather = st.sidebar.multiselect('Pilih Kondisi Cuaca', data_hari['weathersit'].unique(), default=data_hari['weathersit'].unique())

# Filter berdasarkan pilihan user
if selected_workingday == 'Hari Kerja':
    filtered_data = data_hari[(data_hari['workingday'] == 1) & (data_hari['mnth'].isin(selected_months)) & (data_hari['weathersit'].isin(selected_weather))]
else:
    filtered_data = data_hari[(data_hari['workingday'] == 0) & (data_hari['mnth'].isin(selected_months)) & (data_hari['weathersit'].isin(selected_weather))]

# Menampilkan ringkasan data setelah filter
st.header("Ringkasan Data Setelah Filter")
st.write(filtered_data.describe())


# Scatter plot interaktif untuk suhu vs penyewaan
st.subheader("Hubungan Suhu dengan Penyewaan Sepeda")

plt.figure(figsize=(10, 6))
sns.scatterplot(x='atemp', y='cnt', data=filtered_data, hue='season', palette='coolwarm')
plt.title('Penyewaan Sepeda Berdasarkan Suhu yang Dirasakan')
plt.xlabel('Suhu (dalam skala normal)')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(plt)

# Tabel ringkasan data
st.subheader("Tabel Ringkasan Data Penyewaan")
st.write(filtered_data[['dteday', 'season', 'weathersit', 'cnt', 'registered', 'casual']].head(10))
