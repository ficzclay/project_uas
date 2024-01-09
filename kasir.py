menu = {
    1: {'item': 'Nasi Goreng', 'price': 15000},
    2: {'item': 'Mie Goreng','price': 12000},
    3: {'item': 'Ayam Goreng', 'price': 18000},
    4: {'item': 'Es Teh Manis', 'price': 5000},
    5: {'item': 'Es Jeruk', 'price': 6000},
    6: {'item': 'Bakso', 'price': 12000},
    7: {'item': 'Soto Ayam', 'price': 15000}
}

# Inisialisasi variabel total harga
total_harga = 0

# List untuk menyimpan menu yang dibeli
purchased_items = []

# Menampilkan Menu
print("Menu Kantin".center(30))
print("==============================")
print("No | Item           | Harga")
print("==============================")
for key, value in menu.items():
    print(f"{key}  | {value['item']:<15} | {value['price']}")
print("==============================")

# Meminta input pilihan makanan dari pengguna
while True:
    try:
        pilihan = int(input("Pilih nomor makanan/minuman (0 untuk selesai): "))
        if pilihan == 0:
            break
        elif pilihan in menu:
            total_harga += menu[pilihan]['price']
            purchased_items.append(menu[pilihan])
        else:
            print("Pilihan tidak valid, coba lagi.")
    except ValueError:
        print("Masukkan nomor yang valid")

# Menampilkan struk pembelian yang dibeli pelanggan
print("\n")
print("Struk Pembelian".center(30))
print("==============================")
print("Item             | Harga")
print("==============================")
for item in purchased_items:
    print(f"{item['item']:<15} | {item['price']}")
print("==============================")
print(f"Total Harga: {total_harga}")
print("==============================")

