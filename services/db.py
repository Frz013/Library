
import mysql.connector
import random
import string

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'library'
)
def create_kode_buku(kode_buku_cek):
    cur = db.cursor()
    is_kode_buku_exists ="SELECT EXISTS(SELECT 1 FROM tbl_book WHERE kode_buku = %s)"
    cur.execute(is_kode_buku_exists, (kode_buku_cek))

    result = cur.fetchone()
    while True:
        if result[0] == 0:
            kode_buku = ''.join(random.choice(string.ascii_letters.upper()) for i in range(6))
            return kode_buku
        elif result[0] == 1:
            continue

def insert_item(kode_buku, judul_buku, penulis_buku, tahun_terbit_buku, sinopsis_buku, tgl_update):
    cur = db.cursor()
    cur.execute('INSERT INTO tbl_book (kode_buku, judul_buku, penulis_buku, tahun_terbit_buku, sinopsis_buku, tgl_update) VALUES (%s, %s, %s, %s, %s, %s)', (kode_buku, judul_buku, penulis_buku, tahun_terbit_buku, sinopsis_buku, tgl_update))
    db.commit()
    if cur.rowcount > 0:
        return print("data berhasil ditambahkan")
    else:
        return print("data gagal ditambahkan")

def fetch_item():
    cur = db.cursor()
    cur.execute("SELECT * FROM tbl_book")
    return cur.fetchall()

def fetch_item_by_id(id):
    cur = db.cursor()
    cur.execute("SELECT * FROM tbl_book WHERE id=%s", (id,))
    return cur.fetchone()

def update_item(opsi_update, kode_buku):
    cur = db.cursor()
    is_kode_buku_exists ="SELECT EXISTS(SELECT 1 FROM tbl_book WHERE kode_buku = %s)"
    cur.execute(is_kode_buku_exists, (kode_buku,))

    result = cur.fetchone()
    if result[0] == 0:
        print("kode buku tidak ditemukan")

    elif result[0] == 1:
        
        if opsi_update == 1:
            print("Update Data Judul")
            data_baru = str(input("Masukan judul yang baru: "))
            update_data = "UPDATE tbl_book SET judul_buku =%s WHERE kode_buku =%s"
            input_data_baru = (data_baru, kode_buku)
            cur.execute(update_data, input_data_baru)
            db.commit()
            print("judul berhasil di update")


        elif opsi_update == 2:
            return
        elif opsi_update == 3:
            return
        elif opsi_update == 4:
            return