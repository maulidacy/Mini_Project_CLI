# Kasir Sederhana CLI
# Program ini memungkinkan pengguna untuk menambahkan barang ke total belanja dan menghitung total belanja setelah diskon
print("Selamat datang di Kasir Sederhana CLI!")

barang_yang_dibeli = []
total_belanja = 0

# Input data barang
while True:
    nama = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga barang: "))
    jumlah = int(input("Masukkan jumlah barang: "))

    barang_yang_dibeli.append((nama, harga, jumlah))
    total_belanja += harga * jumlah

    lanjut = input("Tambahkan barang lagi? (Y/N): ")
    if lanjut.upper() == 'N':
        break

# Fungsi menghitung diskon
def hitung_diskon(total):
    if total > 100000 and total <= 250000:
        return total * 0.1
    elif total > 250000 and total <= 500000:
        return total * 0.15
    elif total > 500000:
        return total * 0.2
    else:
        return 0

# Menampilkan struk
def tampilkan_struk(barang_yang_dibeli, total_belanja):
    diskon = hitung_diskon(total_belanja)
    total_setelah_diskon = total_belanja - diskon

    print("\n================ Struk Pembelian ================")
    print("Total Belanja: ", total_belanja)
    print("Diskon: ", diskon)
    print("Total Setelah Diskon: ", total_setelah_diskon)
    print("Barang yang dibeli:")
    for barang in barang_yang_dibeli:
        print(f"- {barang[0]} x {barang[2]} = {barang[1] * barang[2]}")
    print("Terima kasih telah berbelanja di Kasir Sederhana CLI!")
    print("===================================================")

# Tampilkan struk belanja
tampilkan_struk(barang_yang_dibeli, total_belanja)
