# Project UAS

link Youtube:
https://youtu.be/qSMfEsiJyFk?si=HHySqIDWj4oPtMWU

- Buatlah program kasir di sebuah kantin, dengan kondisi berikut:
- List opsi pilihan makanan/minuman dan aksi, bisa menggunakan
format dictionary
- Program harus meminta input pilihan makanan dari pengguna.
- Program harus menghitung total harga makanan yang dipesan.
- Program harus menampilkan struk pembelian.

### Penjelasan:
Program ini adalah sebuah program kasir sederhana. Program ini digunakan untuk mencatat dan menghitung total harga pembelian makanan dan minuman di sebuah kantin. Berikut adalah ringkasan singkatnya:


**1. Menu Kantin**: Program ini memiliki menu makanan dan minuman dengan nomor, nama item, dan harga terkait.

**2. Input Pengguna**: Pengguna diminta untuk memilih nomor makanan atau minuman yang ingin dibeli. Jika memilih 0, proses pembelian selesai.

**3. Pencatatan Pembelian**: Program mencatat item yang dibeli beserta harganya ke dalam list purchased_items dan mengakumulasi total harga.

**4. Struk Pembelian**: Setelah pengguna selesai memilih, program menampilkan struk pembelian yang berisi item-item yang dibeli beserta harganya, serta total harga keseluruhan.


Berikut Hasilnya:
![alt text](https://github.com/ficzclay/project_uas/blob/main/img/1.png?raw=true)


## Langkah-langkah pengerjaan latihan

1. Konfigurasi terlebih dahulu username dan email pada global repository-nya

```
git config --global user.name “nama_user”
```

```
git config --global user.email “email_user”
```

2. Buat repository local

```
mkdir bahasa_pemrograman
```

```
cd bahasa_pemrograman
```

```
mkdir praktikum8
```

3. Jika sudah, jalankan command (command git init digunakan untuk menginisialisasi repositori git baru)

```
git init
```

## Menambahkan File Baru Pada Repository Lokal

1. Untuk membuat file baru bisa juga dengan text editor

disini akan menggunakan terminal

```
echo “# praktikum8 >> README.md
```

2. Untuk menambahkan file yang baru saja dibuat, gunakan command

```
git add .
```

3. Untuk menyimpan perubahan yang ada pada database repositori
   lokal, gunakan command

```
git commit -m "first commit"
```

## Membuat Repository Server

1. Server repository yang digunakan adalah github
2. Buat akun github terlebih dahulu
3. Klik tombol + new repository
4. Isi nama repository-nya,

```
contoh: praktikum8
```

5. lalu klik tombol Create repository

## Menambahkan Remote Repository

- Remote Repository merupakan server repositori yang akan digunakan untuk menyimpan segala perubahan yang dilakukan pada repositori lokal, dan bisa diakses oleh banyak pengguna
- Untuk menambahkan remote repository server, gunakan command

```
git remote add origin [url]
```

## Mengirim perubahan ke server (Push)

- Untuk mengirim perubahan pada repositori lokal ke server, gunakan command

```
git push -u origin master
```

## Clone Repository

- git clone digunakan untuk mengambil salinan dari repositori Git dari server ke repositori lokal
- gunakan command ini untuk melakukan kloning ke repositori lokal

```
git clone [url]
```
