print("=== APLIKASI BELANJA SEDERHANA ===")
print("1. Tambah barang")
print("2. Lihat daftar barang")
print("3. Total belanja")
print("4. Hapus barang")
print("5. Keluar")
print("=================================")

barang_yang_dibeli = []
total_belanja = 0

while True:
    pilihan = int(input("\nPilih menu: "))
    if pilihan == 1:
        nama_barang = input("Nama barang: ")
        harga_barang = float(input("Harga: "))
        jumlah_barang = int(input("Jumlah barang: "))
        barang_yang_dibeli.append((nama_barang, harga_barang, jumlah_barang))
    elif pilihan == 2:
        print(barang_yang_dibeli)
    elif pilihan == 3:
        total_belanja = sum(barang[1] * barang[2] for barang in barang_yang_dibeli)
        print("Total belanja: ", total_belanja)
    elif pilihan == 4:
        print(barang_yang_dibeli)
        remove = input("Masukkan nama barang yang akan dihapus: ")
        barang_yang_dibeli = [barang for barang in barang_yang_dibeli if barang[0] != remove]
        print("Barang berhasil dihapus!")
    elif pilihan == 5:
        print("Terima kasih telah menggunakan aplikasi ini!")
        print("=================================")
        break