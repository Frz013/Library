# Library

Library adalah aplikasi command line (CLI) berbasis Python untuk mengelola daftar bacaan (Reading List). Datanya disimpan di database MySQL lokal. Menu daftar tontonan (Watch List) sudah disiapkan, tetapi fiturnya belum dibuat.

## Fitur utama

### Reading List (sudah jalan)

- `Read data/List`: menampilkan semua buku di database. Dari daftar itu kamu bisa membuka detail satu buku lewat `id`-nya, yang berisi kode, judul, penulis, tahun terbit, sinopsis, dan waktu update terakhir.
- `Add data`: menambah buku baru. Aplikasi membuat `kode_buku` sendiri berupa 6 huruf kapital acak yang unik, lalu mencatat waktu simpan di `tgl_update`.
- `Update data`: mengubah judul, penulis, tahun terbit, atau sinopsis buku berdasarkan `kode_buku`.
- `Remove data`: menghapus buku berdasarkan `kode_buku`.

### Watch List (belum diimplementasikan)

## Tech stack

- Bahasa: Python 3
- Database: MySQL lokal, misalnya lewat XAMPP, Laragon, atau MySQL Server
- Library Python: `mysql-connector-python==9.5.0` (terdaftar di [requirements.txt](https://github.com/Frz013/Library/blob/main/requirements.txt))
- Standard library: `os`, `random`, `string`, `datetime`

## Struktur project

Repository [Frz013/Library](https://github.com/Frz013/Library) berisi file-file berikut:

| File / Folder | Fungsi |
| :--- | :--- |
| [main.py](https://github.com/Frz013/Library/blob/main/main.py) | Entry point aplikasi. Menjalankan loop menu utama CLI (`Reading List`, `Watch List`, dan `Close Program`). |
| [tools/book.py](https://github.com/Frz013/Library/blob/main/tools/book.py) | Mengatur tampilan sub-menu CLI dan alur CRUD untuk Reading List (`read_data`, `add_data`, `update_data`, `delete_data`). |
| [services/db.py](https://github.com/Frz013/Library/blob/main/services/db.py) | Koneksi dan query MySQL (`library` / `tbl_book`), termasuk generator `kode_buku` acak 6 huruf kapital yang unik. |
| [requirements.txt](https://github.com/Frz013/Library/blob/main/requirements.txt) | Daftar dependensi Python yang dibutuhkan project. |
| [test.py](https://www.google.com/search?q=https://github.com/Frz013/Library/blob/main/test.py) | Skrip percobaan singkat untuk menguji generator kode buku acak 6 huruf. |

## Persiapan database MySQL

Jalankan service MySQL lokal sebelum memakai aplikasi. Koneksi di [services/db.py](https://github.com/Frz013/Library/blob/main/services/db.py) memakai pengaturan default berikut:

- Host: `localhost`
- User: `root`
- Password: kosong (`""`)
- Database: `library`
- Tabel: `tbl_book`

Kalau MySQL di perangkatmu memakai user atau password lain, ubah dulu parameter koneksi di [services/db.py](https://github.com/Frz013/Library/blob/main/services/db.py).

Repository ini belum menyertakan file `.sql`, jadi database dan tabelnya perlu dibuat manual. Query berikut sudah disesuaikan dengan kolom di `services/db.py`:

```sql
CREATE DATABASE IF NOT EXISTS library;
USE library;

CREATE TABLE tbl_book (
    id INT AUTO_INCREMENT PRIMARY KEY,
    kode_buku VARCHAR(6) NOT NULL UNIQUE,
    judul_buku VARCHAR(255) NOT NULL,
    penulis_buku VARCHAR(255) NOT NULL,
    tahun_terbit_buku VARCHAR(10),
    sinopsis_buku TEXT,
    tgl_update DATETIME
);
```

## Cara instalasi dan menjalankan

1. Clone repository:
   ```bash
   git clone https://github.com/Frz013/Library.git
   cd Library
   ```

2. Buat dan aktifkan virtual environment (opsional, disarankan):
   ```bash
   python -m venv .venv
   # Windows (Command Prompt / PowerShell)
   .venv\Scripts\activate
   ```

3. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan aplikasi:
   ```bash
   python main.py
   ```

## Alur penggunaan

Saat dijalankan, aplikasi langsung membuka menu utama:

1. `Reading List`: masuk ke sub-menu pengelolaan buku.
   - `1. Read data/List`: melihat daftar semua buku. Pilih `1. Detail buku`, lalu masukkan `ID` buku untuk membuka detailnya.
   - `2. Add data`: isi judul, penulis, tahun terbit, dan sinopsis buku baru.
   - `3. Update data`: masukkan `kode_buku`, lalu pilih kolom yang mau diubah (`1` judul, `2` penulis, `3` tahun terbit, `4` sinopsis).
   - `4. Remove data`: masukkan `kode_buku` buku yang mau dihapus.
   - `5. Kembali ke menu utama`: kembali ke menu awal.
2. `Watch List`: belum aktif, masih dalam pengembangan.
3. `Close Program`: menutup aplikasi.
