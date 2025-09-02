kontak = {}

def tambah_kontak(nama, nomor):
    kontak[nama] = nomor
    print(f"Kontak {nama} berhasil ditambahkan.")

def lihat_kontak(nama, nomor_baru):
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