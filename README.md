# Daftar Tugas

Contoh project Python untuk latihan Git dan GitHub. Aplikasi berjalan di Terminal dan tidak membutuhkan library tambahan.

## Fitur

- Melihat daftar tugas.
- Menambahkan tugas.
- Menghapus tugas yang sudah selesai.
- Menyimpan tugas secara otomatis ke `tugas.json`.

## Menjalankan

Pastikan Python 3 sudah terpasang. Buka Terminal di folder project, lalu jalankan:

```bash
python3 main.py
```

Pilih menu dengan angka 1–4, lalu tekan Enter. Data pribadi dalam `tugas.json` dikecualikan dari Git melalui `.gitignore`.

## Upload pertama ke GitHub

Buat repository kosong bernama `contoh-project-github` di GitHub. Jangan tambahkan README, .gitignore, atau license saat membuat repository karena file project sudah tersedia di sini.

Jalankan perintah berikut dari folder project:

```bash
git init
git branch -M main
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:hanafiafan/contoh-project-github.git
git push -u origin main
```

## Latihan perubahan berikutnya

Ubah judul aplikasi di `main.py`, simpan, lalu jalankan:

```bash
git add .
git commit -m "Ubah judul aplikasi"
git push
```
