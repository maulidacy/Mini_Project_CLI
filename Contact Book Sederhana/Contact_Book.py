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