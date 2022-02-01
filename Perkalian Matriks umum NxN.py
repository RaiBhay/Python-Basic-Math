#Biodata
print("Nama", "\t\t", ": Bhayu Phermana Sachty Muktar")
print("Prodi", "\t\t", ": Matematika 2020")
print("NIM", "\t\t", ": 1305620001")
print("-------------------------------------------")
print("Membuat Perkalian 2 Matriks dengan ordo NxN")
print("-------------------------------------------")

#Input Matriks Pertama
print("Input Matriks Pertama")
a= int(input("Masukkan Jumlah Baris dan Kolom: "))     #Input Baris & Kolom
print()

A=[]
for i in range (0, a):                       #Input List ke dalam List A
    A.append([])

for i in range (0,a):                        #Input Elemen Matriks
    for j in range (0,a):
        print("Baris", i+1, "Kolom", j+1)
        A[i].append(int(input("Elemen: ")))
print()
print("Matriks A : ", a," x ",a,"\n")
for i in range (0, a):                       #Print Matriks
    for j in range (0, a):
        print(A[i][j], end="  ")
    print()
print()
print(f'list A = {A}')                       #Print List Matriks

print()
print()

#Input Matriks Kedua
print("Input Matriks Kedua")
print()

B=[]
for i in range (0, a):                       #Input List ke dalam List B
    B.append([])

for i in range (0,a):                        #Input Elemen Matriks
    for j in range (0,a):
        print("Baris", i+1, "Kolom", j+1)
        B[i].append(int(input("Elemen: ")))
print()
print("Matriks B : ", a," x ",a,"\n")
for i in range (0, a):                       #Print Matriks
    for j in range (0, a):
        print(B[i][j], end="  ")
    print()
print()
print(f'list B = {B}')                       #Print List Matriks

print()
print()

#Perkalian Matriks A dan Matriks B
print("Perkalian Matriks A dan Matriks B")
print()

C = []
for i in range(0,a):
    C.append([])
    for j in range(0, a):
        C[i].append(int(0))

for i in range(0,a):
    for j in range(0,a):
        s=0
        for k in range(0,a):
            s = s + A[i][k]*B[k][j]
            C[i][j]= s
print(C)
#Print Matriks C
print("Matriks Perkalian C = A x B adalah", "\n")
for i in range (a):                       #Print Matriks
    for j in range (a):
        print(C[i][j], end="  ")
    print()
print()
print(f'list C = {C}')                       #Print List Matriks