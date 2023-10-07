import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

st.header('Bike Sharing Dashboard')



day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

season_counts = hour_df.groupby('season')['cnt'].mean()

# Convert the dteday column to datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

day_df['day_of_week'] = day_df['dteday'].dt.day_name()
rentals_by_day = day_df.groupby('day_of_week')['cnt'].mean()

# Plot grafik 1
st.subheader("Rental Bike Performance by Season")

fig, ax = plt.subplots()
season_counts.plot(kind='bar', ax=ax)
ax.set_ylabel('Jumlah Rental Bikes')
ax.set_title('Rata - rata Rental Bikes per Season')
ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
st.pyplot(fig)

# Grafik 2
st.subheader("Rental Bike Performance by Day")

fig, ax = plt.subplots()
rentals_by_day.plot(kind='bar', ax=ax)
ax.set_ylabel('Total Rental')
ax.set_title('Rata-rata Total Rental per Hari')
ax.set_xticklabels(['Friday','Monday','Saturday','Sunday','Thursday','Tuesday','Wednesday'])
st.pyplot(fig)
