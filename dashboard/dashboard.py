# Memanggil semua library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Membuka file all_data.csv
all_data = pd.read_csv("all_data.csv")

# Membuat judul pada Streamlit
st.header("Bike-Sharing Dashboard")

# Menampilkan logo di sidebar
with st.sidebar:
    st.image("https://github.com/forkfrog-rtn/submission/raw/main/dashboard/logo%20(3).png")


# Menampilkan data berdasarkan musim
st.subheader("Banyaknya Penyewaan Berdasarkan Musim") # Membuat sub-header
merge_casual = all_data.groupby('season_x').agg({'casual_x': 'sum'})
fig = plt.figure(figsize=(10, 5))

colors_1 = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]
sns.barplot(
    x='season_x',
    y='casual_x',
    data=merge_casual,
    palette=colors_1
)

plt.title('Pada Pelanggan Biasa/Casual', loc='center', fontsize=15)
plt.ylabel(None)
plt.xlabel('Musim')

st.pyplot(fig)


merge_registered = all_data.groupby('season_x').agg({'registered_x': 'sum'})
fig = plt.figure(figsize=(10, 5))

colors_1 = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]
sns.barplot(
    x='season_x',
    y='registered_x',
    data=merge_registered,
    palette=colors_1
)

plt.title('Pada Pelanggan yang Berlangganan/Registered', loc='center', fontsize=15)
plt.ylabel(None)
plt.xlabel('Musim')

st.pyplot(fig)


# Menampilkan data berdasarkan bulan
st.subheader("Banyaknya Penyewaan Berdasarkan Bulan")

merge_casual_month = all_data.groupby('mnth_x').agg({'casual_x': 'sum'})
fig = plt.figure(figsize=(10, 5))

colors_1 = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3"]
sns.barplot(
    x='mnth_x',
    y='casual_x',
    data=merge_casual_month,
    palette=colors_1
)

plt.title('Pada Pelanggan Biasa/Casual', loc='center', fontsize=15)
plt.ylabel(None)
plt.xlabel('Bulan')

st.pyplot(fig)


merge_registered_month = all_data.groupby('mnth_x').agg({'registered_x': 'sum'})
fig = plt.figure(figsize=(10, 5))

colors_1 = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3"]
sns.barplot(
    x='mnth_x',
    y='registered_x',
    data=merge_registered_month,
    palette=colors_1
)

plt.title('Pada Pelanggan yang Berlangganan/Registered', loc='center', fontsize=15)
plt.ylabel(None)
plt.xlabel('Bulan')

st.pyplot(fig)


# Menampilkan data berdasarkan jam
st.subheader("Banyaknya Penyewaan Per Jam")
merge_hr_casual = all_data.groupby('hr').agg({'casual_y': 'sum',})
fig = plt.figure(figsize=(10, 5))

colors_1 = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x='hr',
    y='casual_y',
    data=merge_hr_casual,
    palette=colors_1
)

plt.title('Berdasarkan Pelanggan Biasa/Casual', loc='center', fontsize=15)
plt.ylabel(None)
plt.xlabel('Jam')

st.pyplot(fig)


merge_hr_registered = all_data.groupby('hr').agg({'registered_y': 'sum',})
fig = plt.figure(figsize=(10, 5))

colors_1 = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3","#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x='hr',
    y='registered_y',
    data=merge_hr_registered,
    palette=colors_1
)

plt.title('Berdasarkan Pelanggan yang Berlangganan/Registered', loc='center', fontsize=15)
plt.ylabel(None)
plt.xlabel('Jam')

st.pyplot(fig)