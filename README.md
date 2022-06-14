# Payport

## Application Description
This application has 2 external parties, namely the owner and staff. This application has 2 types of views that are distinguished based on the user login process, namely the display for the owner and the display for employees. Views on the owner include viewing daily sales reports and monthly sales reports, while the display on the employee includes entering the amount of stock, inputting orders, and making transactions.

At the beginning the Owner can enter a number of initial data such as balances, accounts used, prices, products, and promotional programs into the database. Then the staff will use it to enter orders, and the amount of stock per day into the system and the system can inform staff about the remaining stock, total price, and the amount of change that needs to be paid to the customer. At the end of the day the system can provide the calculation results of every transaction made by the system in the form of a sales report to the Owner.

## How to run the Application

### A.
1. Download [XAMPP](https://www.apachefriends.org/download.html)
2. Run Apache and MySql on XAMPP
3. Open phpMyAdmin
4. Import the payport database
5. Download Artifacts MSDeploy (On Payport Repository)
6. Open the src/dist folder
7. Run main.exe

### B.
1. Follow steps 1-4 in method A
2. Download the PayPort Zip Repository
3. Open the payport folder
4. Run terminal, start virtual environment
5. Install requirements.txt
```bash
pip install -r requirement.txt
```
6. Run main
``` python
python main.py
```

## Implemented Modul
The following is a list of the modules that we have implemented along with the screen display of the module with *screen capture* of the module screen

### Login
![Login](./doc/Login.png)

### Laporan Harian
![Laporan Harian](./doc/Laporan-Harian.png)

### Laporan Bulanan
![Laporan Bulanan](./doc/Laporan-Bulanan.png)

### Edit Anggota
![Edit Anggota](./doc/Edit-Anggota.png)

### Edit Produk
![Edit Produk](./doc/Edit-Produk.png)

### Edit Promosi
![Edit Promosi](./doc/Edit-Promosi.png)

### Cek Stok
![Cek Stok](./doc/Cek-Stok.png)

### Input Pesanan
![Input Pesanan](./doc/Input-Pesanan.png)

### Transaksi
![Transaksi](./doc/Transaksi.png)

## List of Table from the database
The following is a list of database tables that are implemented and equipped with table names along with their attributes and descriptions

### Tabel Anggota

|   Id Field  	| Deskripsi                   	| Tipe & length 	|
|:-----------:	|-----------------------------	|:-------------:	|
| IDAnggota   	| Primary Key                 	| Integer(11)   	|
| NamaAnggota 	| Nama dari Anggota           	| Varchar(50)   	|
| TipeAnggota 	| Tipe berupa Owner dan Staff 	| Varchar(10)   	|
| Username    	| Nama untuk Login            	| Varchar(10)   	|
| Password    	| Password untuk Login        	| Varchar(8)    	|

### Tabel Transaksi

|   Id Field  	| Deskripsi                   	| Tipe & length 	|
|:-----------:	|-----------------------------	|:-------------:	|
| IDTransaksi 	| Primary Key                 	| Integer(11)   	|
| IDAnggota   	| ID dari tabel Anggota       	| Integer(11)   	|
| IDPromosi   	| ID dari tabel Promosi       	| Integer(11)   	|
| Tanggal     	| Tanggal transaksi           	| date          	|
| TotalHarga  	| Total harga yang dibayarkan 	| Integer(11)   	|

### Tabel Pesanan

|   Id Field   	| Deskripsi             	| Tipe & length 	|
|:------------:	|-----------------------	|:-------------:	|
| IDTransaksi  	| Primary Key           	| Integer(11)   	|
| NomorPesanan 	| Primary Key           	| Integer(11)   	|
| IDProduk     	| ID dari tabel Promosi 	| Integer(11)   	|
| Kuantitas    	| Kuantitas Produk      	| Integer(11)   	|
| TotalHarga   	| Total harga Pesanan   	| Integer(11)   	|

### Tabel Produk

|   Id Field  	| Deskripsi           	| Tipe & length 	|
|:-----------:	|---------------------	|:-------------:	|
| IDProduk    	| Primary Key         	| Integer(11)   	|
| NamaProduk  	| Nama produk         	| Varchar(50)   	|
| Deskripsi   	| Deskripsi produk    	| Varchar(100)  	|
| HargaProduk 	| Harga satuan produk 	| Integer(11)   	|
| Stok        	| Total stok          	| Integer(11)   	|

### Tabel Promosi

|    Id Field   	| Deskripsi                      	| Tipe & length 	|
|:-------------:	|--------------------------------	|:-------------:	|
| IDPromosi     	| Primary Key                    	| Integer(11)   	|
| NamaPromosi   	| Nama promosi                   	| Varchar(20)   	|
| JumlahPromosi 	| Jumlah Promosi yang ditentukan 	| Float         	|
