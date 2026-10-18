# Analisis Penjualan Produk

Notebook `Proyek_Analisis_Data.ipynb` menganalisis nilai penjualan produk dari pesanan berstatus `delivered` selama Januari 2017–Januari 2018. Nilai penjualan dihitung dari kolom `price` pada item pesanan, tanpa ongkos kirim.

## Menjalankan dashboard

Dari folder `Submission`:

```bash
python -m pip install -r requirements.txt
streamlit run dashboard/dashboard.py
```

`dashboard/main_data.csv` berisi data yang sudah disiapkan untuk dashboard. Seluruh CSV asli tetap tersedia di folder `data` untuk menjalankan notebook. File `dashboard.py` di akar folder mempertahankan entrypoint deployment lama.

Dashboard: https://jlv2u6zxo7ifh8g6uhvhyv.streamlit.app/
