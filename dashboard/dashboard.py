from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import streamlit as st


DATA_FILE = Path(__file__).resolve().parent / "main_data.csv"
FIRST_DATE = date(2017, 1, 1)
LAST_DATE = date(2018, 1, 31)


@st.cache_data
def load_sales():
    return pd.read_csv(DATA_FILE, parse_dates=["order_purchase_timestamp"])


st.set_page_config(page_title="Analisis Penjualan Produk", layout="wide")
st.title("Analisis Penjualan Produk")
st.caption("Pesanan delivered, Januari 2017–Januari 2018. Nilai penjualan = jumlah price, tanpa ongkos kirim.")

with st.sidebar:
    selected_dates = st.date_input(
        "Tanggal pembelian",
        value=(FIRST_DATE, LAST_DATE),
        min_value=FIRST_DATE,
        max_value=LAST_DATE,
    )

if len(selected_dates) != 2:
    st.info("Pilih tanggal awal dan akhir.")
    st.stop()

start_date, end_date = selected_dates
sales = load_sales()
sales = sales.loc[
    sales["order_purchase_timestamp"].ge(pd.Timestamp(start_date))
    & sales["order_purchase_timestamp"].lt(pd.Timestamp(end_date + timedelta(days=1)))
]

if sales.empty:
    st.info("Tidak ada pesanan delivered pada rentang tanggal ini.")
    st.stop()

total_sales = sales["price"].sum()
order_count = sales["order_id"].nunique()
category_sales = sales.groupby("category_name")["price"].sum().sort_values(ascending=False)

col1, col2, col3 = st.columns(3)
col1.metric("Nilai penjualan produk", f"{total_sales:,.2f}")
col2.metric("Jumlah pesanan", f"{order_count:,}")
col3.metric("Kategori teratas", category_sales.index[0])

st.subheader("Tren nilai penjualan bulanan")
monthly_sales = sales.groupby(sales["order_purchase_timestamp"].dt.to_period("M"))["price"].sum()
monthly_sales.index = monthly_sales.index.astype(str)
st.line_chart(monthly_sales.rename("Nilai penjualan"))

st.subheader("10 kategori dengan nilai penjualan terbesar")
st.bar_chart(category_sales.head(10).rename("Nilai penjualan"), horizontal=True)
