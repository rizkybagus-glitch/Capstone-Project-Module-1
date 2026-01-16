produk = [
    {"nama": "Oil Based Pomade", "stok": 30, "harga": 120000},
    {"nama": "Water Based Pomade", "stok": 25, "harga": 120000},
    {"nama": "Clay Pomade", "stok": 20, "harga": 100000},
    {"nama": "Hair Tonic", "stok": 40, "harga": 50000},
    {"nama": "Hair Powder", "stok": 35, "harga": 70000},
    {"nama": "Beard Oil", "stok": 15, "harga": 60000}
]

def tampilkan_produk():
    print("\nDaftar Produk de Cartel")
    print("No | Nama Produk           | Stock | Harga")
    for i, p in enumerate(produk, start=1):
        print(f"{i:<2} | {p['nama']:<22} | {p['stok']:<5} | {p['harga']}")

def tambah_produk():
    nama = input("Masukkan nama produk  : ")
    stok = int(input("Masukkan stok produk  : "))
    harga = int(input("Masukkan harga produk : "))
    produk.append({"nama": nama, "stok": stok, "harga": harga})
    print("Produk berhasil ditambahkan!")

def hapus_produk():
    tampilkan_produk()
    nomor = int(input("Masukkan nomor produk yang ingin dihapus: "))
    index = nomor - 1  # konversi ke index list
    if 0 <= index < len(produk):
        produk.pop(index)
        print("Produk berhasil dihapus!")
    else:
        print("Nomor tidak valid!")

while True:
    print("\nSelamat Datang di Toko Pomade de Cartel")
    print("List Menu:")
    print("1. Menampilkan Daftar Produk")
    print("2. Menambah Produk")
    print("3. Menghapus Produk")
    print("4. Exit Program")

    pilihan = input("Masukkan angka Menu yang ingin dijalankan: ")

    if pilihan == "1":
        tampilkan_produk()
    elif pilihan == "2":
        tambah_produk()
    elif pilihan == "3":
        hapus_produk()
    elif pilihan == "4":
        print("Terima kasih telah menggunakan berkunjung di de Cartel!")
        break
    else:
        print("Menu tidak tersedia!")