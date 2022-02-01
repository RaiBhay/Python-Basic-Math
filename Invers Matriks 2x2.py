#Biodata
print("Nama", "\t\t", ": Bhayu Phermana Sachty Muktar")
print("Prodi", "\t\t", ": Matematika 2020")
print("NIM", "\t\t", ": 1305620001")
print()
print("MENCARI INVERS MATRIKS")
print()

#Input Matriks A
print("\033[92m", "#######################", "\033[00m")
print("\033[92m", "### INPUT MATRIKS A ###", "\033[00m")
print("\033[92m", "#######################", "\033[00m")

a= int(input("Masukkan Jumlah Baris dan Kolom (Kolom & Baris Matriks Harus sama): "))     #Input Baris & Kolom
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

#Mencari Determinan Matriks A
p = A[0][0]*A[1][1]
q = A[0][1]*A[1][0]

det = p - q
print("Determinan Matriks A adalah ", det)

#Mencari Adjoin Matriks A (2x2)
k = A[0][0]
l = A[1][1]
A[0][0] = l
A[1][1] = k

A[0][1] = A[0][1]*-1
A[1][0] = A[1][0]*-1

print()
print("Matriks Adjoin A : ", a," x ",a,"\n")
for i in range (0, a):                       #Print Matriks
    for j in range (0, a):
        print(A[i][j], end="  ")
    print()
print()
print(f'list A = {A}')                       #Print List Matriks
print()

#Mencari Invers Matriks
B = []
for k in range (0,2):
    B.append([])

o = 1/det
for i in range (0,a):
    for j in range (0,a):
        u = o*A[i][j]
        B[i].append(u)

#Print Invers Matriks
print()
print("Matriks Invers : ", a," x ",a,"\n")
for i in range (0, a):                       #Print Matriks
    for j in range (0, a):
        print(B[i][j], end="  ")
    print()
print()
print(f'list B = {B}')                       #Print List Matriks
print()

#Mencari Harga Sebungkus Mie Goreng dan Permen
print(" X = Harga Mie Goreng ")
print(" Y = Harga Permen ")
print()

D = []
for i in range (0,2):
    D.append([])

for i in range (0,2):                        #Input Elemen Matriks
    for j in range (0,1):
        print("Baris", i+1, "Kolom", j+1)
        D[i].append(int(input("Elemen: ")))

#Perkalian Matriks B dan D
C = []
for i in range(0,2):
    C.append([])
    for j in range(0, 1):
        C[i].append(int(0))

for i in range(0,2):
    for j in range(0,1):
        s=0
        for k in range(0,2):
            s = s + B[i][k]*D[k][j]
            C[i][j]=s

#Print Matriks C
print("Matriks Perkalian C = B x D berordo ", 2, " X ", 1, "adalah", "\n")
for i in range (a):                       
    print(C[i], end="  ")
print()
print(f'list C = {C}')
