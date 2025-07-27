# Kasir Sederhana CLI
# Program ini memungkinkan pengguna untuk menambahkan barang ke total belanja dan menghitung total belanja setelah diskon
print("Selamat datang di Kasir Sederhana CLI!")

barang_yang_dibeli = []
total_belanja = 0
diskon = 0
total_setelah_diskon = 0

while True:
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = float(input("Masukkan harga barang: "))
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    tambah_barang = input("Tambahkan barang lagi? (Y/N): ")
    
    def diskon():
         if total_belanja > 100000:
            diskon = total_belanja * 0.20
            print("Selamat anda mendapatkan diskon 20%")
            total_setelah_diskon = total_belanja - diskon
            print("Total Belanja: ", total_setelah_diskon)
            exit()
         else: 
            print("Total Belanja: ", total_belanja)
            exit()

    if tambah_barang == 'N':
        total_belanja += harga_barang * jumlah_barang
        diskon()  # Panggil fungsi diskon
    elif tambah_barang == 'Y':
        total_belanja += harga_barang * jumlah_barang
        diskon()  # Panggil fungsi diskon
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
        