 #salah satu contoh package
from texttable import Texttable
import getpass
from perhitungan.penilaian_mahasiswa import nilai_mahasiswa
from perhitungan.pembayaran_mahasiswa import pembayaran
from perhitungan.cal import menu2



def menu():
    print("=+=+=+=+=+=+ APLIKASI KAMPUS PELITA BANGSA =+=+=+=+=+=")
    print("======================================================")
    print("\n\t----Pilihan-----")
    print("\t1. Penilaian Mahasiswa")
    print("\t2. Pembayaran Mahasiswa")
    print("\t3. Kalkulator")
    print("\n\t;/Sudah selesai dari tanggal 08 april 2018")

    pilih = input("\n\tSilahkan pilih : ")
    if pilih == "1" :
        nilai_mahasiswa()
    elif pilih == "2" :
        pembayaran()
    elif pilih == "3" :
        menu2()
    else:
        exit
    tanya()

def tanya():
    tanya = input("\nKembali ke menu (y/n) ?")
    if tanya == "y":
        menu()
    elif tanya == "n":
        exit
    else:
        print("\n\tSalah Input !!")
        
username = input("\nUsername : ")
password = getpass.getpass()
print("======================================================")

if username == "RITAHANS" and password == "12345" :
    menu()

else :
    print("Maaf username atau password kamu salah")



