import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

st.title("📊 E-Commerce Public Analysis Dashboard")
st.markdown("by Paul David Djukardi")

@st.cache_data
def load_data():
    dataset_direktori = 'submission/dataset'
    df_customer = pd.read_csv(os.path.join(dataset_direktori, "customers_dataset.csv"))
    df_items = pd.read_csv(os.path.join(dataset_direktori, "order_items_dataset.csv"))
    df_payments = pd.read_csv(os.path.join(dataset_direktori, "order_payments_dataset.csv"))
    df_orders = pd.read_csv(os.path.join(dataset_direktori, "orders_dataset.csv"))
    df_orders_customer = pd.merge(df_orders, df_customer, on='customer_id')
    data_gabungan = pd.merge(df_orders_customer, df_items, on='order_id')
    data_gabungan['order_purchase_timestamp'] = pd.to_datetime(data_gabungan['order_purchase_timestamp'])
    data_gabungan['order_date'] = data_gabungan['order_purchase_timestamp'].dt.date
    return data_gabungan, df_payments

try:
    data_gabungan, df_payments = load_data()
except FileNotFoundError as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

st.sidebar.header("🔍 Filter Data")

min_date = data_gabungan['order_date'].min()
max_date = data_gabungan['order_date'].max()
date_range = st.sidebar.date_input(
    "Rentang Tanggal Transaksi",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

unique_states = sorted(data_gabungan['customer_state'].unique())
selected_states = st.sidebar.multiselect(
    "Pilih Negara Bagian",
    options=unique_states,
    default=unique_states
)

unique_payments = sorted(df_payments['payment_type'].unique())
selected_payments = st.sidebar.multiselect(
    "Pilih Metode Pembayaran",
    options=unique_payments,
    default=unique_payments
)

if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date

filtered_data = data_gabungan[
    (data_gabungan['order_date'] >= start_date) &
    (data_gabungan['order_date'] <= end_date) &
    (data_gabungan['customer_state'].isin(selected_states))
]

df_payments_filtered = df_payments[
    df_payments['payment_type'].isin(selected_payments)
].merge(filtered_data[['order_id']], on='order_id', how='inner')

st.header("🏙️ Tren Pembelian per Kota")

num_cities = st.slider("Jumlah Kota yang Ditampilkan", 5, 20, 10)
view_choice = st.radio("Tampilkan:", ["Top", "Bottom"], horizontal=True)

total_transaksi = filtered_data.groupby('customer_city', as_index=False)['price'].sum()

if view_choice == "Top":
    kota_visual = total_transaksi.nlargest(num_cities, 'price')
else:
    kota_visual = total_transaksi.nsmallest(num_cities, 'price')

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x='price', y='customer_city', data=kota_visual, palette='viridis', ax=ax1)
ax1.set_title(f"{view_choice} {num_cities} Kota (Periode: {start_date} hingga {end_date})")
ax1.set_xlabel("Total Nilai Pembelian (R$)")
ax1.set_ylabel("Kota")
st.pyplot(fig1)

st.header("💳 Analisis Metode Pembayaran")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribusi Metode Pembayaran")
    frekuensi = df_payments_filtered['payment_type'].value_counts()
    fig2, ax2 = plt.subplots()
    ax2.pie(frekuensi, labels=frekuensi.index, autopct='%1.1f%%', startangle=140)
    st.pyplot(fig2)

with col2:
    st.subheader("Rata-Rata Nilai Transaksi")
    mean_values = df_payments_filtered.groupby('payment_type')['payment_value'].mean()
    fig3, ax3 = plt.subplots()
    sns.barplot(x=mean_values.index, y=mean_values.values, palette='viridis')
    plt.xticks(rotation=45)
    ax3.set_ylabel("Rata-Rata (R$)")
    st.pyplot(fig3)

st.markdown("---")
st.info(f"""
**Filter Aktif:**
- Periode: {start_date} hingga {end_date}
- Negara Bagian: {', '.join(selected_states)}
- Metode Pembayaran: {', '.join(selected_payments)}
""")

st.markdown("---")
st.caption("""
**Catatan:**
- Gunakan filter di sidebar untuk menyesuaikan tampilan data
- Data akan otomatis update sesuai dengan filter yang dipilih
""")
