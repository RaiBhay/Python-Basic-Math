def faktorial(angka):
    fak=1
    for i in range (1, angka+1):
        fak= fak*i
    return fak

angka = int(input("Masukkan Nilai yang akan difaktorialkan: "))
hasil = faktorial(angka)
print("Nilainya adalah ", hasil)