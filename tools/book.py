from services import db
from datetime import datetime as dt
import random
import string
import os
import main

def start():
    while True:
        os.system('cls')
        print("========== READING LIST MENU ==========")
        opsi = int(input(f"Pilih opsi berikut:\n1. Read data/List\n2. Add data\n3. Update data\n4. Remove data\n5. Kembali ke menu utama\nPilih opsi: "))
        if opsi == 1:
            read_data()
        elif opsi == 2:
            add_data()
        elif opsi == 3:
            pass
        elif opsi == 4:
            pass
        elif opsi == 5:
            break


def add_data():
    print("Tolong masukan data yang diminta: ")
    kode_buku = ''.join(random.choice(string.ascii_letters.upper()) for i in range(6))
    judul_buku = str(input("Masukan Judul Buku: "))
    penulis_buku = str(input("Masukan Nama Penulis Buku: "))
    tahun_terbit_buku = str(input("Masukan Tahun Terbit Buku: "))
    sinopsis_buku = str(input("Masukan Sinopsis Buku: "))
    tgl_update = dt.now()

    db.insert_item(kode_buku, judul_buku, penulis_buku, tahun_terbit_buku, sinopsis_buku, tgl_update)
    print("Data has been added")

def read_data():
    books = db.fetch_item()
    for book in books:
        id_buku = book[0]
        kode_buku = book[1]
        judul_buku = book[2]
        penulis_buku = book[3]
        tahun_terbit_buku = book[4]
        sinopsis_buku = book[5]
        tgl_update = book[6]

        print(f'''
ID: {id_buku}
KODE: {kode_buku}
JUDUL: {judul_buku}
PENULIS: {penulis_buku}
TAHUN TERBIT: {tahun_terbit_buku}
SINOPSIS: {sinopsis_buku}
DATA DI UPDATE PADA:{tgl_update}
''')
    str(input("\nBack to menu: (press enter)"))