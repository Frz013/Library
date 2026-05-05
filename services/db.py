
import mysql.connector
import random
import string

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'library'
)
def create_kode_buku():
    cur = db.cursor()
    
    while True:
        kode_buku = ''.join(random.choice(string.ascii_letters.upper()) for i in range(6))

        is_kode_buku_exists ="SELECT EXISTS(SELECT 1 FROM tbl_book WHERE kode_buku = %s)"
        cur.execute(is_kode_buku_exists, (kode_buku,))

        result = cur.fetchone()
        
        if result[0] == 0:
            
            return kode_buku

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
            what_update = ["Judul Buku", "judul_buku"]
        elif opsi_update == 2:
            what_update = ["Penulis Buku", "penulis_buku"]
        elif opsi_update == 3:
            what_update = ["Tahun Terbit Buku", "tahun_terbit_buku"]
        elif opsi_update == 4:
            what_update = ["Sinopsis Buku", "sinopsis_buku"]
        
    print(f"Update Data {what_update[0]}")
    data_baru = str(input(f"Masukan {what_update[0]} yang baru: "))
    update_data = f"UPDATE tbl_book SET {what_update[1]} =%s WHERE kode_buku =%s"
    input_data_baru = (data_baru, kode_buku)
    cur.execute(update_data, input_data_baru)
    db.commit()
    print(f"{what_update[0]} berhasil di update")

def delete_data(kode_buku):
    cur = db.cursor()
    is_kode_buku_exists ="SELECT EXISTS(SELECT 1 FROM tbl_book WHERE kode_buku = %s)"
    cur.execute(is_kode_buku_exists, (kode_buku,))

    result = cur.fetchone()
    if result[0] == 0:
        print("kode buku tidak ditemukan")
    elif result[0] == 1:
        delete_data_buku = "DELETE FROM tbl_book WHERE kode_buku = %s"
        cur.execute(delete_data_buku,(kode_buku,))
        db.commit()
        print("Data Buku Berhasil Dihapus")
