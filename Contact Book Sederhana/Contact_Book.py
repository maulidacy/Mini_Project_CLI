kontak = {}

def tampilkan_menu():
    print("\n=== APLIKASI DAFTAR KONTAK SEDERHANA ===")
    print("1. Tambah kontak")
    print("2. Lihat semua kontak")
    print("3. Update kontak")
    print("4. Hapus kontak")
    print("5. Keluar")
    print("========================================")

def tambah_kontak(nama, nomor):
    kontak[nama] = nomor
    print(f"Kontak {nama} berhasil ditambahkan.")

def lihat_kontak(nama):
    if not kontak:
        print("Daftar kontak kosong.")
    else:
        for nama, nomor in kontak.items():
            print(f"Nama: {nama}, Nomor: {nomor}")

def update_kontak(nama, nomor_baru):
    if nama in kontak:
        kontak[nama] = nomor_baru
        print(f"Kontak {nama} berhasil diperbarui.")
    else:
        print(f"Kontak {nama} tidak ditemukan.")

def hapus_kontak(nama):
    if nama in kontak:
        del kontak[nama]
        print(f"Kontak {nama} berhasil dihapus.")
    else:
        print(f"Kontak {nama} tidak ditemukan.")

while True:
    tampilkan_menu()
    try:
        pilihan = int(input("Pilih menu: "))
    except ValueError:

nama = input("Masukkan nama kontak: ")
nomor = input("Masukkan nomor kontak: ")
tambah_kontak(nama, nomor)

nama = input("Masukkan nama kontak: ")
lihat_kontak(nama)

update_kontak = input("Masukkan nama kontak: ")
nomor_baru = input("Masukkan nomor kontak baru: ")
update_kontak(update_kontak, nomor_baru)

hapus_kontak = input("Masukkan nama kontak: ")
hapus_kontak(hapus_kontak)



