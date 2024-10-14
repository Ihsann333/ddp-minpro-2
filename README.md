# ddp-minpro-2
# Nama: Nur Ihsan
# NIM: 2409116051
# Sistem Informasi B
![image](http![flowchart minpro 2](https://github.com/user-attachments/assets/28879d34-f7ba-4244-9f19-9d3072ed3aa9)
![image](https://github.com/user-attachments/assets/af26b6ed-e8e6-43e6-bd18-b02cc30c8374)
# Untuk menampilkan tabel dari library
![image](https://github.com/user-attachments/assets/bf167892-6023-45ca-bd46-dce7ba08d758)
# Mendefinisikan daftar data_mobil yang berisi informasi tentang beberapa mobil, setiap mobil diwakili sebuah dictionary yang mencakup merek, model, tipe, dan tahun 
![image](https://github.com/user-attachments/assets/ac0ce3c1-c99d-409e-ad3d-e6fe4e039932)
# Fungsi tambah_mobil() ini digunakan untuk menambahkan informasi mobil baru ke dalam daftar data_mobil. Pengguna diminta memasukkan merek, model, tipe, dan tahun mobil, kemudian data tersebut disimpan dalam bentuk dictionary dan ditambahkan ke daftar. Setelah berhasil, fungsi juga memanggil lihat_mobil() untuk menampilkan daftar mobil yang sudah ada.
![image](https://github.com/user-attachments/assets/f0229fe9-23e7-4071-a012-b29fe7be9f0a)
# Fungsi hapus_mobil() ini menghapus mobil dari daftar data_mobil. Setelah menampilkan daftar mobil, pengguna diminta memasukkan model yang ingin dihapus. Fungsi kemudian mencari model tersebut, menghapusnya dan memberi tahu pengguna. Jika mobil tidak ditemukan, fungsi akan memberi pesan bahwa mobil tidak ditemukan.
![image](https://github.com/user-attachments/assets/19b7e6cf-f9d2-4905-b7f3-f9d35d652470)
# Menampilkan pesan bahwa logout berhasil
![image](https://github.com/user-attachments/assets/67a0fca5-102b-43ab-8757-a6bb722bccc7)
# Fungsi ikut_lelang() memungkinkan pengguna untuk mengikuti lelang mobil. Pengguna memilih model mobil dari daftar yang ditampilkan, kemudian memasukkan tawaran harga. Setelah itu, pengguna diminta untuk mengkonfirmasi apakah ingin melanjutkan pembelian. Jika ya, sistem mengonfirmasi pembelian jika tidak, pembelian dibatalkan.
![image](https://github.com/user-attachments/assets/8efee641-3df1-47e8-bfdb-07d44b37d3d7)
# Meminta pengguna untuk memasukkan username dan password. Input tersebut akan disimpan dalam variabel username dan password.
![image](https://github.com/user-attachments/assets/736a4779-5d9d-4808-83c9-9924f0edb934)
# Memeriksa apakah username dan password yang dimasukkan adalah "admin" dan "password". Jika benar, pengguna disambut sebagai admin dan ditampilkan menu pilihan yang berisi opsi untuk menambah, melihat, menghapus mobil, atau logout. Menu ditampilkan dalam format tabel yang rapi menggunakan PrettyTable.
![image](https://github.com/user-attachments/assets/28435557-f0d5-4bc6-883b-60672c74107c)
# Bagian kode ini meminta pengguna untuk memilih opsi dari menu (1-4). Jika pengguna memilih:
# 1: Memanggil fungsi tambah_mobil()
# 2: Memanggil fungsi lihat_mobil()
# 3: Memanggil fungsi hapus_mobil()
# 4: Memanggil fungsi logout() dan keluar dari menu
# Jika pilihan tidak valid, akan ditampilkan pesan kesalahan.
![image](https://github.com/user-attachments/assets/af6f1aef-cf25-4c26-8f14-c1b240fc6fc8)
# Memeriksa apakah username dan password adalah "user biasa" dan "password". Jika benar, pengguna disambut sebagai "user biasa" dan ditampilkan menu dengan opsi untuk melihat mobil, ikut lelang, atau logout.
![image](https://github.com/user-attachments/assets/b13da5e3-fae9-4ee0-87d4-8e9946ac4915)
# Meminta pengguna untuk memilih opsi dari menu (1-3). Jika memilih 1, pengguna akan melihat mobil, lalu ditanya apakah ingin ikut lelang. Jika jawab "ya", fungsi ikut_lelang() dipanggil; jika "tidak", ditampilkan pesan bahwa mereka memilih untuk tidak ikut lelang. Jika pilihan tidak valid, akan muncul pesan kesalahan.
![image](https://github.com/user-attachments/assets/c9316142-a9cf-4d6e-a257-35648b51ed7c)
# Jika pengguna memilih 2, fungsi ikut_lelang() dipanggil. Jika memilih 3, fungsi logout() dipanggil dan keluar dari menu. Jika pilihan tidak valid, ditampilkan pesan kesalahan. Jika username atau password salah, muncul pesan "Tidak valid".
