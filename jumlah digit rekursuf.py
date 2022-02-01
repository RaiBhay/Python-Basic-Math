#Biodata
print("Nama", "\t\t", ": Bhayu Phermana Sachty Muktar")
print("Prodi", "\t\t", ": Matematika 2020")
print("NIM", "\t\t", ": 1305620001")
print("\033[95m","---------------------------------------------------------------------------------------", "\033[00m")
print("\t","Mencari Hasil Jumlah Dari Seluruh Digit Suatu Bilangan (Fungsi Rekursif)")
print("\033[95m","---------------------------------------------------------------------------------------", "\033[00m")
print()

def jumlah_digit(a):
    b = len(str(abs(a)))
    c = 10**(b-1)
    if b == 1 :
        A.append(a)
        print("List digitnya adalah ", A)
        e = 0
        for i in range (0, len(A)):
           e = e + A[i] 
        return e
    else:
        d = int(a/c)
        A.append(d)
        return jumlah_digit(a%c)

A=[]
f = int(input("Masukkan nilai yang ingin dicari jumlah digitnya: "))
print("Hasil Jumlah dari digitnya adalah ", jumlah_digit(f))
print()
print("\033[93m","\U0001F600","TERIMA KASIH SUDAH MENCARI JUMLAH DIGIT SUATU BILANGAN", "\U0001F600", "\033[00m")