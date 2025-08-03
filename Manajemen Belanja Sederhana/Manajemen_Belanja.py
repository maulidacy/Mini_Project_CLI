barang_yang_dibeli = []

def tampilkan_menu():
    print("\n=== APLIKASI BELANJA SEDERHANA ===")
    print("1. Tambah barang")
    print("2. Lihat daftar barang")
    print("3. Total belanja")
    print("4. Hapus barang")
    print("5. Keluar")
    print("=================================")

while True:
    tampilkan_menu()
    try:
        pilihan = int(input("Pilih menu: "))
    except ValueError:
        print("Masukkan angka antara 1 sampai 5!")
        continue

    if pilihan == 1:
        nama_barang = input("Nama barang: ")
        try:
            harga_barang = float(input("Harga: "))
            jumlah_barang = int(input("Jumlah: "))
        except ValueError:
            print("Harga dan jumlah harus berupa angka!")
            continue
        barang_yang_dibeli.append((nama_barang, harga_barang, jumlah_barang))
        print(f"{nama_barang} berhasil ditambahkan!")

    elif pilihan == 2:
        if not barang_yang_dibeli:
            print("Belum ada barang yang ditambahkan.")
        else:
            print("\nDaftar Barang:")
            print("-" * 40)
            print("{:<20} {:<10} {:<10}".format("Nama", "Harga", "Jumlah"))
            print("-" * 40)
            for b in barang_yang_dibeli:
                print("{:<20} Rp{:<10,.0f} {:<10}".format(b[0], b[1], b[2]))
            print("-" * 40)

    elif pilihan == 3:
        total = sum(b[1] * b[2] for b in barang_yang_dibeli)
        print(f"Total belanja: Rp{total:,.0f}")

    elif pilihan == 4:
        nama_hapus = input("Masukkan nama barang yang ingin dihapus: ")
        awal = len(barang_yang_dibeli)
        barang_yang_dibeli = [b for b in barang_yang_dibeli if b[0].lower() != nama_hapus.lower()]
        if len(barang_yang_dibeli) < awal:
            print(f"{nama_hapus} berhasil dihapus.")
        else:
            print(f"{nama_hapus} tidak ditemukan.")

    elif pilihan == 5:
        print("Terima kasih telah menggunakan aplikasi ini!")
        break
    else:
        print("Pilihan tidak valid. Masukkan angka 1-5.")
