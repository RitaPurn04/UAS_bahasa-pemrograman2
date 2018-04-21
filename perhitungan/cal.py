def tambah ():
    print('\t1.penjumlahan x')
    a = int(input('\t Masukan Nilai x='))
    b = int(input('\t Masukan Nilai y='))
    c = a + b
    print('\tx+y=',c)
    tanya()
def kurang():
    print('\t2.pengurangan x')
    a = int(input('\t Masukan Nilai x='))
    b = int(input('\t Masukan Nilai y='))
    c = a - b
    print('\tx-y=',c)
    tanya()
def bagi():
    print('\t3.pembagian x')
    a = int(input('\t Masukan Nilai x='))
    b = int(input('\t Masukan Nilai y='))
    c = a/b
    print('\tx/y=',c)
    tanya()
def kali():
    print('\t4.perkalian x')
    a = int(input('\t Masukan Nkilai x='))
    b = int(input('\t Masukan nilai y='))
    c = a * b
    print('\tx*y=',c)
    tanya()

def tanya():
    tanya = input('\n\tKembali ke menu kalkulator (y/t)?')
    if tanya == 'y':
        menu2()
    elif tanya == 't':
        exit
    else:
        print('\n\tsalah input.........!!!')
def menu2():
    print('\n\t=============================')
    print('\tProgram Kalkulator Sederhana')
    print('\t===============================')
    print('\t1. Penjumlahan')
    print('\t2. Pengurangan')
    print('\t3. Pembagian')
    print('\t4. Perkalian')
    print('\t===============================')
    print('\tSilahkan pilih 1-4')
    print('')
    pil = input('\tMasukan Pilihan :')
    if pil == '1':
        tambah()
    elif pil == '2':
        kurang()
    elif pil == '3':
        bagi()
    elif pil == '4':
        kali()
    else:
        print('\t Maaf, input yang anda masukan salah')
        print('\tCoba Ulangi Kembali')
        tanya()
        
