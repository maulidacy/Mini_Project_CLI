#--------------------------------- Kasir Sederhana ------------------------------------
# Program kasir sederhana untuk warung makan dengan fungsi-fungsi yang terpisah.
# Fungsi ini menyapa pembeli, menampilkan menu, menerima pesanan, menghitung total belanja, dan memberikan diskon jika memenuhi syarat.

def sapa_pembeli(nama="Pembeli"):
    """Menyapa pembeli dengan nama tertentu atau default."""
    print(f"Halo {nama}, selamat datang di Warung Python!")

def tampilkan_menu():
    """Menampilkan daftar menu makanan dan harga."""
    print("\n====== Daftar Menu =======")
    print("1. Nasi Goreng \t - Rp. 15000")
    print("2. Mie Ayam \t - Rp. 12000")
    print("3. Sambalado \t - Rp. 4000")
    print("4. Telor Ceplok\t - Rp. 3000")
    print("5. Teh Pait \t - Rp. 3000")
    print("==========================")

# --- Menggunakan kamus (dictionary) untuk menyimpan menu agar lebih rapi ---
daftar_menu = {
    1: {"nama": "Nasi Goreng", "harga": 15000},
    2: {"nama": "Mie Ayam", "harga": 12000},
    3: {"nama": "Sambalado", "harga": 4000},
    4: {"nama": "Telor Ceplok", "harga": 3000},
    5: {"nama": "Teh Pait", "harga": 3000}
}

def hitung_total(daftar_harga):
    """Menerima list harga dan menghitung totalnya."""
    total = sum(daftar_harga)
    return total

def beri_diskon(total, diskon=0.1):
    """Menghitung harga setelah diskon (default diskon = 10%)."""
    if total > 50000: # Contoh: diskon hanya berlaku jika total belanja > 50000
        diskon_amount = total * diskon
        total_setelah_diskon = total - diskon_amount
        return total_setelah_diskon
    else:
        return total

# --- PROGRAM UTAMA ---
if __name__ == "__main__": # Memastikan kode utama berjalan hanya saat file ini dieksekusi langsung.
    # Sapa pembeli
    nama_pembeli = input("Halo, siapa nama Anda? ")
    sapa_pembeli(nama_pembeli)

    pesanan_harga = []
    
    while True:
        tampilkan_menu()
        
        try:
            pilihan = int(input("Pilih menu (tekan 0 untuk selesai): "))
        except ValueError:
            print("Pilihan tidak valid, masukkan angka antara 0-5.")
            continue
            
        if pilihan == 0:
            break
        elif pilihan in daftar_menu:
            menu_terpilih = daftar_menu[pilihan]
            nama_menu = menu_terpilih["nama"]
            harga_menu = menu_terpilih["harga"]
            
            try:
                jumlah_dibeli = int(input(f"Berapa jumlah {nama_menu} yang ingin dibeli? "))
                if jumlah_dibeli <= 0:
                    print("Jumlah tidak valid. Masukkan angka positif.")
                    continue
                
                total_harga_item = harga_menu * jumlah_dibeli
                pesanan_harga.append(total_harga_item)
                print(f"{nama_menu} sejumlah {jumlah_dibeli} ditambahkan ke keranjang!")
                
            except ValueError:
                print("Jumlah tidak valid, masukkan angka.")
                continue
        else:
            print("Pilihan tidak ada di menu. Silakan pilih lagi.")
            
    # --- PROSES PEMBAYARAN ---
    if not pesanan_harga:
        print("\nAnda tidak memesan apa pun. Sampai jumpa!")
    else:
        total_belanja = hitung_total(pesanan_harga)
        total_setelah_diskon = beri_diskon(total_belanja)
        
        print("\n========== Struk Belanja ===========")
        print(f"Total belanja sebelum diskon: Rp. {total_belanja:,}")
        
        if total_belanja > 50000:
            print(f"Selamat! Anda mendapatkan diskon 10%.")
            print(f"Total yang harus dibayar: Rp. {total_setelah_diskon:,}")
        else:
            print(f"Total yang harus dibayar: Rp. {total_belanja:,}")
        print("====================================")
            
        print("Terima kasih sudah berbelanja!")