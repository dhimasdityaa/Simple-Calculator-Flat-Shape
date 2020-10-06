def menu():
    print("Pilih Perhitungan")
    print("1. Luas Persegi")
    print("2. Luas Segitiga")


def persegi():
    p = int(input('Masukan Panjang Persegi : '))
    l = int(input('Masukan Luas Persegi : '))

    L = p * l
    print('Luas Persegi adalah ', L)


def segitiga():
    t = int(input('Masukan Tinggi Segitiga : '))
    a = int(input('Masukan Alas Segitiga : '))

    L = a * t * 1/2
    print('Luas Segitiga Adalah', L)


print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+Selamat Datang Pada Program Penghitung Bangun Ruang+")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")

menu()

pilih = int(input('Masukan Pilihan : '))

if pilih == 1:
    persegi()
else:
    segitiga()
