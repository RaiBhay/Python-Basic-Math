#Biodata
print("Nama", "\t\t", ": Bhayu Phermana Sachty Muktar")
print("Prodi", "\t\t", ": Matematika 2020")
print("NIM", "\t\t", ": 1305620001")
print("---------------------")
print("Program Input Matriks")
print("---------------------")

#Input Matriks
a= int(input("Masukkan Jumlah Baris: "))     #Input Baris
b= int(input("Masukkan Jumlah Kolom: "))     #Input Kolom
print()

A=[]
for i in range (0, a):                       #Input List ke dalam List A
    A.append([])

for i in range (0,a):                        #Input Elemen Matriks
    for j in range (0,b):
        print("Baris", i+1, "Kolom", j+1)
        A[i].append(int(input("Elemen: ")))
print()
print("Matriks A : ", a," x ",b,"\n")
for i in range (0, a):                       #Print Matriks
    for j in range (0, b):
        print(A[i][j], end="  ")
    print()
print()
print(f'list A = {A}')                       #Print List Matriks