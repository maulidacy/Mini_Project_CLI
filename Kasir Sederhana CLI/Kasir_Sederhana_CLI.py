nama_barang = input("Masukkan nama barang: ")
harga_barang = float(input("Masukkan harga barang: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

total_belanja = harga_barang * jumlah_barang
diskon = 0
total_setelah_diskon = 0

if total_belanja > 100.000:
    print("Selamat anda mendapatkan diskon 20%")
    diskon = total_belanja * 0.20
    total_setelah_diskon = total_belanja - diskon
    print("Total Belanja: ", total_setelah_diskon)
else:
    print("Total Belanja: ", total_belanja)