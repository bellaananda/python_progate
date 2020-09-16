import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("\n Masukkan pin anda: "))
    trial = 0

    while (id != int(atm.cekPin()) and trial < 3):
        id = int(input("Pin salah. Silakan masukkan lagi : "))
        trial += 1

        if trial == 3:
            print("Error. Silakan ambil kartu dan coba lagi.")
            exit()

    while True:
        a = 1
        print("\n\t ------------------------------ \n")
        print("\t SELAMAT DATANG DI APLIKASI ATM")
        print("\t\t 1 - Cek Saldo \n\t\t 2- Debet \n\t\t 3 - Simpan \n\t\t 4 - Ganti Pin \n\t\t 5 - Keluar")
        # a -= 1
        # if a != 1:
        #     break

        pilihmenu = int(input("\t Silakan pilih menu : "))

        if pilihmenu == 1:
            print("\t Selamat Datang di Menu Cek Saldo")
            print("\t Saldo anda sekarang : Rp. " + str(atm.cekBalance()))

        elif pilihmenu == 2:
            print("\t Selamat Datang di Menu Debet")
            nominal = float(input("\t Silakan masukkan nominal saldo : "))
            verifikasi_debet = input("\t Konfirmasi : Anda akan melakukan debet dengan nominal Rp. " + str(nominal) + " ? y/t" + " ")

            if verifikasi_debet == "y":
                print("\t Saldo awal anda adalah : Rp. " + str(atm.cekBalance()))
            else:
                break
            
            if nominal < atm.cekBalance():
                atm.debetBalance(nominal)
                print("\t Transaksi debet berhasil!")
                print("\t Saldo anda sekarang adalah : Rp. " + str(atm.cekBalance()))
            else:
                print("\t Maaf. Saldo anda tidak cukup untuk melakukan debet.")
                print("\t Silakan lakukan penambahan nominal saldo.")

        elif pilihmenu == 3:
            print("\t Selamat Datang di Menu Simpan")
            nominal = float(input("\t Silakan masukkan nominal saldo : "))
            verifikasi_simpan = input("\t Konfirmasi : Anda akan melakukan penyimpanan dengan nominal Rp. " + str(nominal) + " ? y/t" + " ")

            if verifikasi_simpan == "y":
                atm.simpanBalance(nominal)
                print("\t Saldo anda sekarang adalah : Rp. " + str(atm.cekBalance()))
            else:
                break

        elif pilihmenu == 4:
            print("\t Selamat Datang di Menu Ganti Pin")
            verifikasi_pin = int(input("\t Silakan masukkan pin anda : "))
            
            if verifikasi_pin != int(atm.cekPin()):
                print("\t Pin anda salah. Silakan masukkan pin : ")

            pin_baru = int(input("\t Silakan masukkan pin baru : "))
            print("\t Pin anda berhasil diganti!")

            verifikasi_pinbaru = int(input("\t Coba masukkan pin baru anda : "))
            
            if verifikasi_pinbaru == pin_baru:
                print("\t Selamat, pin baru anda berhasil!")
            else:
                print("\t Maaf, pin baru anda salah!")

        elif pilihmenu == 5:
            print("\t Selamat Datang di Menu Keluar")
            print("\t Resi tercetak otomatis saat anda keluar. \n\t Harap simpan sebagai bukti transaksi.")
            print("\t No. Record: ", random.randint(100000, 1000000))
            print("\t Tanggal: ", datetime.datetime.now())
            print("\t Saldo akhir: ", atm.cekBalance())
            print("\t Terima kasih dan sampai jumpa!")
            exit()