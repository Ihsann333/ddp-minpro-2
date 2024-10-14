from prettytable import PrettyTable

data_mobil = [
    {"Merek": "Honda", "Model": "W-RV", "Tipe": "Prestige CVT", "Tahun": 2023}, 
    {"Merek": "Honda", "Model": "H-RV", "Tipe": "E-CVT", "Tahun": 2020},
    {"Merek": "Honda", "Model": "B-RV", "Tipe": "N7X Prestige CVT", "Tahun": 2021}
]

def lihat_mobil():
    tabel = PrettyTable()
    tabel.field_names = ["Merek", "Model", "Tipe", "Tahun"]
    for mobil in data_mobil:
        tabel.add_row([mobil["Merek"], mobil["Model"], mobil["Tipe"], mobil["Tahun"]])
    print(tabel)

def tambah_mobil():
    global data_mobil
    print("Tambahkan mobil...")
    Merek = input("Masukkan merek: ")
    Model = input("Masukkan model: ")
    Tipe = input("Masukkan tipe: ")
    Tahun = input("Masukkan tahun: ")
    data_mobil.append({"Merek": Merek, "Model": Model, "Tipe": Tipe, "Tahun": Tahun})
    print("Berhasil menambahkan")
    lihat_mobil()

def hapus_mobil():
     global data_mobil
     print("Hapus mobil...")
     lihat_mobil() 
     model_mobil = input("Masukkan model mobil yang ingin dihapus: ")

     for mobil in data_mobil:
        if mobil["Model"].lower() == model_mobil.lower():
            data_mobil.remove(mobil)
            print(f"Mobil {model_mobil} berhasil dihapus.")
            return 
        print(f"Mobil {model_mobil} tidak ditemukan.")

def logout():
    print("Logout berhasil...")

def ikut_lelang():
    print("Memilih Mobil...")
    lihat_mobil()
    model_mobil = input("Masukkan model mobil yang ingin Anda lelang: ")
    print(f"Anda memilih untuk ikut lelang pada model: {model_mobil}")
    tawaran = input("Masukkan tawaran Anda: ")
    print(f"Tawaran anda sebesar {tawaran} untuk model {model_mobil} telah diajukan.")
    konfirmasi = input("Apakah Anda ingin melanjutkan ke pembelian? (ya/tidak): ").lower()
    if konfirmasi == 'ya':
        print(f"Anda telah membeli mobil {model_mobil} dengan tawaran {tawaran}.")
    else:
        print("User membatalkan pembelian.")

# Proses login dan menu...
username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == 'admin' and password == 'password':
    print("Selamat datang admin!")
    while True:
        menu_pilihan = [
            {"Nomor": "1", "Pilihan": "Tambah mobil"}, 
            {"Nomor": "2", "Pilihan": "Lihat mobil"},  
            {"Nomor": "3", "Pilihan": "Hapus mobil"}, 
            {"Nomor": "4", "Pilihan": "Logout"},
        ]
        tabel = PrettyTable()
        tabel.field_names = ["Nomor", "Pilihan"]
        for menu in menu_pilihan:
            tabel.add_row([menu["Nomor"], menu["Pilihan"]])
        print(tabel)

        pilihan = input("Pilih opsi (1-4):")

        if pilihan == '1':
            tambah_mobil()
        elif pilihan == '2':
            lihat_mobil()
        elif pilihan == '3':
            hapus_mobil()
        elif pilihan == '4':
            logout()
            break 
        else:
            print("Opsi tidak valid! Silahkan pilih antara 1-4.")

elif username == 'user biasa' and password == 'password':
    print("Selamat datang user biasa!")
    while True:
        print("Menu:")
        print("1. Lihat mobil:")
        print("2. Ikut lelang:")
        print("3. Logout")
        
        pilihan = input("Pilih opsi (1-3):")

        if pilihan == '1':
            lihat_mobil()
            ikut_lelang_option = input("Apakah Anda ingin ikut lelang? (ya/tidak): ").lower()
            if ikut_lelang_option == 'ya':
                ikut_lelang()
            elif ikut_lelang_option == 'tidak':
                print("Anda memilih untuk tidak ikut lelang.")
            else:
                print("Pilihan tidak valid!")

        elif pilihan == '2':
            ikut_lelang()
        elif pilihan == '3':
            logout()
            break 
        else:
            print("Opsi tidak valid! Silahkan pilih antara 1-3.")
else:
    print("Tidak valid")