
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'library'
)

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