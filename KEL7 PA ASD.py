# Library
import os
from data_staff import collection
from prettytable import PrettyTable
import time
from pwinput import pwinput
from prettytable import PrettyTable
import math
os.system('cls')


# Akses ke pretttable untuk merapikan data
tabel_mahasiswa = PrettyTable()
tabel_menu  = PrettyTable()
tabel_staff = PrettyTable()
tabel_mahasiswa=field_names = ["Nama","NIM","Alamat","Jenis kelamin","Jurusan"]


# ===== Kelas Node =====
class Node:
    def __init__(self, nama, nim, alamat, jenis_kelamin, jurusan):
        self.nama =nama
        self.nim = nim
        self.alamat = alamat
        self.jenis_kelamin= jenis_kelamin
        self.jurusan= jurusan
        self.next = None
        
    def __str__(self):
        return f"Nama{self.nama}, NIM{self.nim}, Alamat{self.alamat}, Jenis_Kelamin {self.jenis_kelamin}, Jurusan {self.jurusan}"


# ===== Kelas Mahasiswa =====
class mahasiswa:
    def __init__(self):
        self.head = None
        self.mahasiswa=[]

    # Tambah Data Mahasiswa
    def tambah_data(self, nama, nim, alamat, jenis_kelamin, jurusan):
        data_baru = Node(nama, nim, alamat, jenis_kelamin, jurusan)
        current = self.head

        if self.head is None:
            self.head = data_baru
            self.mahasiswa.append(data_baru.nim)
        else:
            while current.next is not None:
                current = current.next
            current.next = data_baru
            self.mahasiswa.append(data_baru.nim)
        
    # Hapus Data Mahasiswa
    def hapus_data(self, nim):
        current = self.head
        previous = None

        while current:
            if current.nim == nim:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        
    # Lihat Data Mahasiswa
    def lihat_data(self):
        if self.head is None:
            print("\n")
            print("!!!!! Data Mahasiswa Kosong !!!!!")
            print("\n")
        else:
            current = self.head
            data_list = []
            while current is not None:
                os.system("cls")
                data_list.append([current.nama, current.nim, current.alamat, current.jenis_kelamin, current.jurusan])
                current = current.next
                table = PrettyTable()
                table.field_names= field_names
                table.add_rows(data_list)
                print(table)
    
    # Urut Data Mahasiswa (Quick Sort)
    def quicksort(self, data:list[Node], ascending=True):
        if len(data) <= 1:
            return data
        else:
            pivot = data[0].nim
            if ascending:
                kiri = [x for x in data[1:] if x.nim <= pivot]
                kanan = [x for x in data[1:] if x.nim > pivot]
            else:
                kiri = [x for x in data[1:] if x.nim >= pivot]
                kanan = [x for x in data[1:] if x.nim < pivot]
            return self.quicksort(kiri, ascending) + [data[0]] + self.quicksort(kanan, ascending)
        # kiri adalah sub-daftar yang berisi semua elemen yang lebih kecil atau sama dengan elemen pivot,
        # kanan adalah sub-daftar yang berisi semua elemen yang lebih besar dari elemen pivot.
        
    # Menampilkan Data Mahasiswa yang Terurut
    def lihat_data_urut(self, ascending=True):
        if self.head is None:
            print("\n")
            print("!!!!! Data Mahasiswa Tidak Tersedia !!!!!")
            print("\n")
        else:
            current = self.head
            data_list = []
            while current is not None:
                data_list.append(current)
                current = current.next
            sorted_data = self.quicksort(data_list, ascending)
            table = PrettyTable()
            table.field_names = field_names
            for data in sorted_data:
                table.add_row([data.nama, data.nim, data.alamat, data.jenis_kelamin, data.jurusan])
            print(table)
            
    # Cari Data Mahasiswa (Jump Search)
    def panjang(self):
        panjang = 0
        current = self.head
        while current is not None:
            panjang += 1
            current = current.next
        return panjang

    def cari_data(self, nim):
        cari = False
        a = None
        b = nim
        x = self.panjang()
        langkah = str(math.sqrt(x))
        d = None
        data = data_mahasiswa.head 

        if cari == False :
                while data:
                    if nim in data.nim:
                        if not cari:
                            x = PrettyTable()
                            x.field_names = ["Nama", "NIM", "Alamat", "Jenis Kelamin", "Jurusan"]

                        cari = True
                        x.add_row([data.nama, data.nim, data.alamat, data.jenis_kelamin, data.jurusan])

                    data = data.next

                if x:
                    return x
                else:
                    return None

        while data and data.nim() < nim():
            y = data
            z = 0

            while z < min(langkah, x) and data:
                data = data.next
                z += 1

            if not data:
                return None

        while data and data.nim() > x():
            y = data.prev
            z = 0

            while z < min(langkah, x) and data:
                data = data.prev
                z += 1

            if not data:
                return None

        if data.nim() == x():
            return data

    # Menampilkan Data Mahasiswa yang Dicari
    def lihat_data_cari(self):
        print("Silakan masukkan data yang ingin dicari")
        nim = str(input("Masukkan NIM: "))
        mencari = data_mahasiswa.cari_data(nim)

        if mencari == None:
            print("=" * 10, "PENCARIAN DATA MAHASISWA UNMUL", "=" * 10)

            print("\n")
            print(f"!!!!! Data Mahasiswa NIM {nim} Tidak Ditemukan !!!!!")
            print("\n")

        else:
            print("\n")
            print("=" * 8, "PENCARIAN DATA MAHASISWA UNMUL", "=" * 8)

            print("\n")
            print(f"Data Mahasiswa NIM {nim} Ditemukan")
            print(mencari)   

    # Login Mahasiswa
    def cek_login(self, nama, nim):
        current = self.head
        while current is not None:
            if current.nama == nama and current.nim == nim:
                return True
            current = current.next
        return False
   
# membuat variabel penghubung class mahasiswa biar simpel -bayu
data_mahasiswa = mahasiswa()

# Variabel untuk Memanggil collection di Mongodb 
collection = collection

# ============ 1. AKSES ADMIN =============
# ===== DATABASE HOSTING/ONLINE ADMIN =====
data_admin ={"userdataadmin":["KEL7"],
    "password":["777"]}

# Fungsi Login Admin
def login_atas_admin():
    while True:
        os.system('cls')
        print("======= LOGIN SEBAGAI ADMIN =======")
        user_admin = input("Silakan Masukkan Username Anda: ")
        pass_admin = pwinput("Silakan Masukkan Password Anda: ")
        try:
            masuk_admin = data_admin.get("userdataadmin").index(user_admin)
            if user_admin == data_admin.get("userdataadmin")[masuk_admin] and pass_admin == data_admin.get("password")[masuk_admin]:
                print("===== LOGIN BERHASIL =====")
                menu_atas_staff()
            else:
                    print('\n')
                    print(" xxxxx MAAF LOGIN GAGAL ! xxxxx")
                    back= input("TEKAN 0 UNTUK KELUAR : ")
                    if back == '0':
                        alur_program()
                    else:
                        pass

        except ValueError:
                print('\n')
                print(" xxxxx MAAF LOGIN GAGAL ! xxxxx")
                back= input("TEKAN 0 UNTUK KELUAR : ")
                if back == '0':
                    alur_program()
                else:
                    pass


# Menu 1 Pilihan Admin (Menampilkan Data Admin)
def tampil_data_admin():  
    print("=== DATA STAFF ===")
    t = collection.find({})
    tabel = PrettyTable()
    tabel.field_names = ['nip', 'pass']
    for i in t:
        tabel.add_row([i['nip'], i['pass']])
    print(tabel)

# Menu 2 Pilihan Admin (Menambahkan Staff Baru)
def tambah_staff_baru():
     while True:
            try:
                print("\n === Silakan Masukkan Data Staff Baru Berikut ===")
                nipbaru = int(input("NIP baru: "))
                passbaru = int(pwinput("Masukkan Pass baru: "))
                collection.insert_one({'nip': nipbaru, 'pass': passbaru})
                print("\n === Data Staff Berhasil Ditambahkan ===")
                time.sleep(1)
                os.system('cls')
                break
            except:
                print("xxx Gunakan Angka Saat Menginput NIP & password! xxx")
                time.sleep(2)
                os.system('cls')
                continue
    
# Menu 3 Pilihan Admin (Hapus Data Staff)
def hapus_staff():
    tampil_data_admin()
    cari_hapus = collection.find({})
    aa = int(input("Silakan Masukkan NIP yang ingin dihapus: "))
    collection.delete_one({"nip": aa})
    print("\n !!! DATA TELAH TERHAPUS !!!")
    time.sleep(1)
    os.system('cls')

# Menu Admin
def menu_atas_staff():
    os.system('cls')
    ulang = "y" or "Y"
    while(ulang == "y" or "Y" or True):

        print("""
            +====+==========================+
            | NO |      MENU PILIHAN        |
            +====+==========================+
            | 1. |  LIHAT DATA STAFF        |
            | 2. |  TAMBAH STAFF            |
            | 3. |  HAPUS  STAFF            |
            | 4. |  MENU SEBELUMNYA         |
            | 5. |  KELUAR DARI PROGRAM     |
            +====+==========================+
            """)

        tindakan_owner = input("Masukkan Tindakan Anda: ")
        if tindakan_owner == '1':
            # Lihat Data Staff
            os.system('cls')
            print("\n")
            tampil_data_admin()
            time.sleep(5)
            os.system("cls")
            menu_atas_staff()
            
        elif tindakan_owner=='2':
            # Tambah Staff
            os.system('cls')
            time.sleep(3)
            tambah_staff_baru()
            time.sleep(3)

        elif tindakan_owner=='3':
            # Hapus Staff
            os.system('cls')
            time.sleep(3)
            hapus_staff()
            time.sleep(3)

        elif tindakan_owner == '4':
            # Menu Sebelumnya
            os.system('cls')
            alur_program()

        elif tindakan_owner=='5':
            # Keluar Program
            os.system('cls')
            print("TERIMAKASIH!")
            print("\nAnda Telah Keluar dari Program")
            exit()
        

        else :
            print("\n xxxxx Pilihan Tidak Tersedia xxxxx")
            ulang = input("\n Apakah Anda ingin mengulang ? [y/n] \n==>")
            if ulang == "y" or 'Y':
                os.system('cls')
                continue
            else:
                print("TERIMAKASIH!")
                print("\nAnda Telah Keluar dari Program")
                exit()



# ========== 2. AKSES STAFF ==========
akun_staff1 ={"user" :[000, 908],
             "pass" :[123, 111]
             
             }
    # tambahkan akun staff lainnya jika diperlukan

# dibackup dengan data dictionary        

def login_staff():
    os.system('cls')
    while True:
        try:
            print("======= LOGIN SEBAGAI STAFF =======")
            useradmin = int(input("Silakan Masukkan NIP: "))
            passadmin = int(pwinput("Silakan Masukkan Password: "))
            if useradmin in akun_staff1.get("user") and passadmin in akun_staff1.get("pass"):
                os.system('cls')
                print('===== LOGIN BERHASIL =====')
                input("Tekan enter untuk melanjutkan...")
                time.sleep(1)
                menu_staff()
                break

            staff = collection.find_one({"nip": useradmin, "pass": passadmin})

            if staff is not None:
                if passadmin == staff['pass']:
                    os.system('cls')
                    print('===== LOGIN BERHASIL =====')
                    input("Tekan enter untuk melanjutkan...")
                    time.sleep(1)
                    menu_staff()
                    break
                else:
                    print("LOGIN GAGAL, PASSWORD SALAH")

            else:
                keluar= input("LOGIN GAGAL, KETIK 0 UNTUK KEMBALI:")
                if keluar == '0':
                    alur_program()
                    break
                else:
                    continue
        except:
            os.system("cls")
            print("Silakan masukan user dan pass menggunakan interger atau angka")
            time.sleep(4)
            os.system("cls")


# Menu Staff
def menu_staff():
    os.system('cls')
    ulang = "y" or "Y"
    while(ulang == "y" or "Y" or True):

        print("""
    +====+==========================+
    | NO |      MENU PILIHAN        |
    +====+==========================+
    | 1. |  TAMBAH DATA MAHASISWA   |
    | 2. |  HAPUS DATA MAHASISWA    |
    | 3. |  LIHAT DATA MAHASISWA    |
    | 4. |  URUTKAN DATA MAHASISWA  |
    | 5. |  CARI DATA MAHASISWA     |
    | 6. |  MENU SEBELUMNYA         |
    | 7. |  KELUAR DARI PROGRAM     |
    +====+==========================+
    """)
        
        tindakan_staff = input("Silakan Masukkan No. Pilihan Anda : ")
        if tindakan_staff == '1':
            # Tambah Data Mahasiswa
            os.system("cls")
            print("\n")
            print("=== Silahkan Lengkapi Data Mahasiswa Baru ===")
            while True:
                namaa = input("Nama : ")
                if namaa.isalpha():
                    break
                else:
                    os.system("cls")
                    print("Nama tidak valid, hanya boleh terdiri dari huruf")
                    time.sleep(2)
                    os.system("cls")
                    
            nama_kecill = namaa.lower()
            while True:
                nim = input ("NIM : ")
                if nim.isdigit():
                    break
                else:
                    os.system("cls")
                    print("NIM tidak valid, hanya boleh terdiri dari angka/digit")
                    time.sleep(2)
                    os.system("cls")
                    
            alamat =input("Alamat : ")
            
            # Masukkan Jenis Kelamin
            ulang = "y" or "Y"
            while(ulang == "y" or "Y" or True):
                print ("\nPilih Jenis Kelamin: \n[1] Laki - laki\n[2] Perempuan")
                jenis_kelamin = input("Masukkan No. Pilihan Anda: ")
                if jenis_kelamin == '1':
                    jenis_kelamin = "Laki - laki" 
                elif jenis_kelamin  == '2':
                    jenis_kelamin = "Perempuan"
                else:
                    print("\n xxxxx Pilihan Tidak Tersedia xxxxx")
                    ulang = input("\n Apakah Anda ingin mengulang ? [y/n] \n==>")
                    if ulang == "y" or 'Y':
                        os.system('cls')
                        continue
                    else:
                        print("TERIMAKASIH!")
                        print("\nAnda Telah Keluar dari Program")
                        exit()
                break
            
            # Masukkan Program Studi
            ulang = "y" or "Y"
            while(ulang == "y" or "Y" or True):
                print("\nPilih Jurusan: \n[1] Sistem Informasi\n[2] Informatika\n[3] Teknik Kimia\n[4] Teknik Industri\n[5] Teknik Elektro")
                jurusan = input("Masukkan No. Pilihan Anda: ")
                if jurusan == '1':
                    jurusan = "Sistem Informasi"
                elif jurusan == '2':
                    jurusan = "Informatika"
                elif jurusan == '3':
                    jurusan = "Teknik Kimia"
                elif jurusan == '4':
                    jurusan = "Teknik Industri"
                elif jurusan == '5':
                    jurusan = "Teknik Elektro"
                else:
                    print("\n xxxxx Pilihan Tidak Tersedia xxxxx")
                    ulang = input("\n Apakah Anda ingin mengulang ? [y/n] \n==>")
                    if ulang == "y" or 'Y':
                        os.system('cls')
                        continue
                    else:
                        print("TERIMAKASIH!")
                        print("\nAnda Telah Keluar dari Program")
                        exit()
                break

            data_mahasiswa.tambah_data(nama_kecill, nim, alamat, jenis_kelamin, jurusan)
            os.system("cls")
            data_mahasiswa.lihat_data()
            print("===== Data Mahasiswa Berhasil Ditambahkan =====")
            time.sleep(3)
            os.system("cls")
                

        elif tindakan_staff == '2':
            # Hapus Data Mahasiswa
            os.system("cls")
            data_mahasiswa.lihat_data()
            hapus = input("Masukkan NIM dari Mahasiswa yang ingin dihapus : ")
            if data_mahasiswa.hapus_data(hapus):
                os.system("cls")
                print("===== Data Mahasiswa Berhasil Dihapus =====")
                time.sleep(3)
                data_mahasiswa.lihat_data()
                time.sleep(3)
                os.system("cls")
            else:
                print("DATA MAHASISWA TIDAK TERDAFTAR!")

        elif tindakan_staff == '3' :
            # Lihat Data Mahasiswa
            os.system("cls")
            print("\n")
            print("=" * 10, "DATA MAHASISWA", "=" * 10)
            data_mahasiswa.lihat_data()
            time.sleep(3)
            os.system('cls')
            
        elif tindakan_staff == '4':
            # Urutkan Data Mahasiswa
            os.system("cls")
            print("\n")
            print("=" * 10, "DATA MAHASISWA TERURUT BERDASARKAN NIM", "=" * 10)
            data_mahasiswa.lihat_data_urut()
            time.sleep(3)
            os.system('cls')

        elif tindakan_staff == '5':
            # Cari Data Mahasiswa
            os.system("cls")
            data_mahasiswa.lihat_data()
            data_mahasiswa.lihat_data_cari()
            time.sleep(3)
            os.system('cls')
        
        elif tindakan_staff == '6':
            # Menu Sebelumnya
            os.system('cls')
            alur_program()

        elif tindakan_staff == '7':
            # Keluar Program
            os.system('cls')
            print("\nAnda Telah Keluar dari Program")
            quit()

        else:
            print("\n xxxxx Pilihan Tidak Tersedia xxxxx")
            ulang = input("\n Apakah Anda ingin mengulang ? [y/n] \n==>")
            if ulang == "y" or 'Y':
                os.system('cls')
                continue
            else:
                print("TERIMAKASIH!")
                print("\nAnda Telah Keluar dari Program")
                exit()


# ========== 3. AKSES MAHASISWA ==========
# ===== DATABASE MAHASISWA =====
Login_Mahasiswa ={"Nama":["bayu","kayla", "ani"],
       "password":["222","222", "222"]}    

# Menu Mahasiswa
def menu_mahasiswa():
    os.system('cls')
    global nama_mahasiswa
   
    print("======= LOGIN SEBAGAI MAHASISWA =======")
    nama_mahasiswa = input("Masukkan Nama Anda: ")
    nim_mahasiswa = pwinput("Masukkan NIM Anda: ")
    nama_kecil = nama_mahasiswa.lower()
    login = None
    try:
        login = Login_Mahasiswa.get("Nama").index(nama_kecil)
    except ValueError:
        pass
    
    if login is not None and nim_mahasiswa == Login_Mahasiswa.get("password")[login]:
        os.system('cls')
        print(" ===== Login Telah Berhasil =====")
        time.sleep(2)
        os.system("cls")
        lanjutan_mahasiswa()
        
    elif data_mahasiswa.cek_login(nama_kecil, nim_mahasiswa):
        os.system("cls")
        print(" ===== Login Telah Berhasil =====")
        time.sleep(2)
        os.system("cls")
        lanjutan_mahasiswa()
    else:
        os.system("cls")
        print(" !!! Nama dan password tidak terdaftar !!! ")
        back= input("TEKAN 0 UNTUK KELUAR : ")
        if back == '0':
            alur_program()
        else:
                pass
        os.system("cls")
        menu_mahasiswa()
         
        
def lanjutan_mahasiswa():
    ulang = "y" or "Y"
    while(ulang == "y" or "Y" or True):
        print(f"""
                
    +====+==========================+
    |        SELAMAT DATANG         |
    +====+==========================+
    |Nama Pengguna :{nama_mahasiswa} 
    +====+==========================+

    +====+==========================+
    | NO |      MENU PILIHAN        |
    +====+==========================+
    | 1. |  LIHAT MATA KULIAH       |
    | 2. |  LIHAT DATA MAHASISWA    |
    | 3. |  MENU SEBELUMNYA         |
    | 4. |  KELUAR DARI PROGRAM     |
    +====+==========================+
    """)
        
        tindakan_mahasiswa = input("Silakan Masukkan No. Pilihan Anda : ")
        if tindakan_mahasiswa == '1':
            os.system("cls")
            print("\n")
            print("""
            +====+==============================================+
            | NO |         DAFTAR MATA KULIAH SEMESTER 2        |   
            +====+==============================================+   
            | 1. |  Algoritma dan Struktur Data                 |   
            | 2. |  Database Management System                  |
            | 3. |  Pengantar Bisnis                            |
            | 4. |  Statistika                                  |
            | 5. |  Arsitektur SI/TI                            |
            | 6. |  Sistem Operasi                              |
            | 7. |  Bahasa Indonesia                            |
            | 8. |  Kepemimpinan dan Kecakapan Interpersonal    |
            +====+==============================================+
            """)
            time.sleep(4)
            os.system("cls")

        
        elif tindakan_mahasiswa == '2':
            # Lihat Data Mahasiswa
            os.system("cls")
            data_mahasiswa.lihat_data()
            time.sleep(3)
            os.system("cls")

        elif tindakan_mahasiswa == '3':
            alur_program()

        elif tindakan_mahasiswa == '4':
            print("TERIMAKASIH!")
            print("\nAnda Telah Keluar dari Program")
            exit()       

        else:
            print("\n xxxxx Pilihan Tidak Tersedia xxxxx")
            ulang = input("\n Apakah Anda ingin mengulang ? [y/n] \n==>")
            if ulang == "y" or 'Y':
                os.system('cls')
                continue
            else:
                print("TERIMAKASIH!")
                print("\nAnda Telah Keluar dari Program")
                exit()


# ===== FUNGSI TAMPILAN AWAL PROGRAM =====
def tampilan_awal():
    os.system('cls')
    ulang = "y" or "Y"
    while(ulang == "y" or "Y" or True):

        print("=" * 54)
        print("="*3,"Selamat Datang di Portal Data Mahasiswa UNMUL ".center(40),"="*3)
        print("=" * 54)

        print("""
        +====+=======================+
        | NO |     MENU PILIHAN      |
        |====|=======================|
        | 1. |     LAYANAN PORTAL    |
        | 2. |     EXIT              |
        +====+=======================+
        """)
        
        while True:
            try:
                pilih = int(input("Silahkan Masukkan Pilihan Anda [1/2] : "))
                break
            except:
                print("xxx Gunakan Angka Saat Menginput Pilihan xxx")
                continue
                
        if pilih == 1 :
            os.system("cls")
            alur_program()
        elif pilih == 2 :
            os.system('cls')
            print("TERIMAKASIH!")
            time.sleep(2)
            os.system("cls")
            print("\nAnda Telah Keluar dari Program")
            exit()

        else:
            print("\n xxxxx Pilihan Tidak Tersedia xxxxx")
            ulang = input("\n Apakah Anda ingin mengulang ? [y/n] \n==>")
            if ulang == "y" or 'Y':
                os.system('cls')
                continue
            else:
                print("TERIMAKASIH!")
                print("\nAnda Telah Keluar dari Program")
                exit()


# ===== Fungsi Alur Menu Program =====
def alur_program():
    os.system('cls')
    ulang = "y" or "Y"
    while(ulang == "y" or "Y" or True):

        print("""
    +====+=======================+
    | NO |     MENU PILIHAN      |
    |====|=======================|
    | 1. |     LOGIN ADMIN       |
    | 2. |     LOGIN STAFF       |
    | 3. |     LOGIN MAHASISWA   |
    | 4. |     MENU SEBELUMNYA   |
    | 5. |     KELUAR            |
    +====+=======================+
    """)

        while True:
            try:
                user = int(input("Masukkan No. Pilihan Anda: "))
                break
            except:
                print("\nxxx Silakan masukan pilihan yang tersedia dan gunakan angka xxx")
                continue

        if user == 1:
            # Login Admin
            login_atas_admin()
        elif user == 2 :
            # Login Staff
            login_staff()
        elif user == 3:
            # Login Mahasiswa
            menu_mahasiswa()
        elif user == 4:
            # Kembali ke Menu Sebelumnya
            tampilan_awal()
        elif user == 5:
            # Keluar Program
            print("TERIMAKASIH!")
            print("\nAnda Telah Keluar dari Program")
            exit()
        else:
            print("\n xxxxx Pilihan Tidak Tersedia xxxxx")
            ulang = input("\n Apakah Anda ingin mengulang ? [y/n] \n==>")
            if ulang == "y" or 'Y':
                continue
            else:
                print("TERIMAKASIH!")
                print("\nAnda Telah Keluar dari Program")
                exit()


# ===== PROGRAM BERJALAN =====
tampilan_awal()
alur_program()