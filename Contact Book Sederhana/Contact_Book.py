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

def hapus_kontak(nama):
    if nama in kontak:
        del kontak[nama]
        print(f"Kontak {nama} berhasil dihapus.")
    else:
        print(f"Kontak {nama} tidak ditemukan.")


nama = input("Masukkan nama kontak: ")
nomor = input("Masukkan nomor kontak: ")
tambah_kontak(nama, nomor)

lihat_kontak = input("Masukkan nama kontak: ")
lihat_kontak(lihat_kontak)

update_kontak = input("Masukkan nama kontak: ")
nomor_baru = input("Masukkan nomor kontak baru: ")
update_kontak(update_kontak, nomor_baru)

hapus_kontak = input("Masukkan nama kontak: ")
hapus_kontak(hapus_kontak)
