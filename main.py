"""Aplikasi daftar tugas sederhana tanpa library tambahan."""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tugas.json")


def main():
    try:
        tugas = json.loads(DATA_FILE.read_text()) if DATA_FILE.exists() else []
    except (OSError, json.JSONDecodeError):
        print("File tugas.json tidak dapat dibaca. Periksa file sebelum mencoba lagi.")
        return

    if not isinstance(tugas, list) or not all(isinstance(item, str) for item in tugas):
        print("Format tugas.json tidak valid. Isinya harus berupa daftar teks.")
        return

    while True:
        print("\nDAFTAR TUGAS\n1. Lihat tugas\n2. Tambah tugas\n3. Selesaikan tugas\n4. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            if not tugas:
                print("Belum ada tugas.")
            for nomor, item in enumerate(tugas, 1):
                print(f"{nomor}. {item}")
        elif pilihan == "2":
            item = input("Tugas baru: ").strip()
            if item:
                tugas.append(item)
                DATA_FILE.write_text(json.dumps(tugas, ensure_ascii=False, indent=2))
                print("Tugas tersimpan.")
            else:
                print("Tugas tidak boleh kosong. Silakan masukkan nama tugas.")
        elif pilihan == "3":
            try:
                nomor = int(input("Nomor tugas yang selesai: "))
                if not 1 <= nomor <= len(tugas):
                    raise ValueError
                tugas.pop(nomor - 1)
                DATA_FILE.write_text(json.dumps(tugas, ensure_ascii=False, indent=2))
                print("Tugas selesai!")
            except ValueError:
                print("Masukkan nomor tugas yang tersedia.")
        elif pilihan == "4":
            print("Sampai jumpa!")
            break
        else:
            print("Pilih angka 1 sampai 4.")


if __name__ == "__main__":
    main()
