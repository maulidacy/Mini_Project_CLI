# Analisis Penjualan Toko
# Deskripsi:

# Kamu memiliki data penjualan barang dalam bentuk list tuple:

penjualan = [
    ("Buku", 15000, 3),
    ("Pensil", 2000, 10),
    ("Penghapus", 1000, 5),
    ("Bolpoin", 2500, 7),
    ("Penggaris", 3000, 2)
]

# Tiap tuple berisi:
# - Nama Barang
# - Harga Satuan
# - Jumlah Terjual

# Tugas:
# 1. Hitung Total per Barang
#    - Buat list baru berisi total harga tiap barang menggunakan list comprehension.
#      Contoh output:
#      ```python[45000, 20000, 5000, 17500, 6000]

# 2. Buat Laporan Format String
#    - Buat list baru berisi string laporan seperti:
#      ```"Buku: 3 pcs, Total Rp 45000"`
#   (gunakan list comprehension + f-string)

# 3. Filter Barang Laris
#    - Buat list berisi **nama barang** yang jumlah terjualnya lebih dari 5.
#    Contoh:
#   ```python ["Pensil", "Bolpoin"] ```

# 4. Total Semua Penjualan
#    - Gunakan list comprehension **di dalam fungsi** untuk menghitung total semua penjualan toko.