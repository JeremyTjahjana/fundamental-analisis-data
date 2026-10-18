# Analisis Penjualan Produk

Notebook `Proyek_Analisis_Data.ipynb` menganalisis nilai penjualan produk dari pesanan berstatus `delivered` selama Januari 2017–Januari 2018. Nilai penjualan dihitung dari kolom `price` pada item pesanan, tanpa ongkos kirim.

Untuk menjalankan dashboard dari folder `Submission`:

```bash
python -m pip install -r requirements.txt
streamlit run dashboard.py
```

Dashboard membaca empat CSV di folder `data` dan menyediakan filter tanggal pembelian, tren bulanan, serta kategori produk dengan nilai penjualan terbesar.
