import os 
import sys
import time


# pewarna makanan
m = "\033[1;31m" # warna merah pekat
x = "\033[1;37m" # warna putih
df = "\033[0m" # default trerminal


# looping sederhana
list = [
    f"{x}1. Penjumlahan{df}",
    f"{x}2. Pengurangan{df}",
    f"{x}3.Perkalian{df}",
    f"{x}4. Pembagian{df}",
    f"{x}5.Modulus{df}",
    f"{x}00. out{df}"
]
monolog = f"{x}Silahkan Masukan angka yang ingin anda hitung"
kosong = ""
style = f"{m}====================> Welcome TO calcu <===================="
style_end = f"{m}============================================================{df}"

def main():
    # pewarna makanan
    m = "\003[31m" # warna merah
    x = "\003[37m" # warna putih
    df = "\003[0m" # default trerminal


    user = ""
    while user != "00":
        print("Welcome to system calcu")
        print(style)
        print(monolog)

        # menampilkan list 
        for i in list:
            print(i)

        print(style_end)

        iyus = input("Masukan Pilihan Anda \n : ")

        if iyus == "00":
            yakin = ["y", "n"]
            print("Apakah anda yakin ingin out?")

            warning = input("(y / n ) Tekan y untuk out dan tekan n untuk batal \n :")

            if warning.lower() == "y":
                print("Terimakasih Telah Menggunakan Calculator adi!")
                time.sleep(15)
                os.system("clear")
                break
            else:
                print("Permintaan akan segera di proses! silahkan tunggu sebentar")
                time.sleep(10)
                os.system("clear")
                print("layer akan siap dalam waktu 3 detik")
                time.sleep(4)
                os.system("clear")
        else:
            print(f"Anda Telah Memilih {user}")
            if user == '1':
                print("Welcome to penjumlahan")
                print(kosong)

                xx1 = input("Masukan angaka pertama : ")
                print(kosong)
                yy1 = input("Masukan angka kedua : ")

                hasil_penjumlahan = xx1 + yy1

                print("hasil perhitungna ada adalah \n" + {hasil_penjumlahan})

if __name__ == "__main__":
    main()



        