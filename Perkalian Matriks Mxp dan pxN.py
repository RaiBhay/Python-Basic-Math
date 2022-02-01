#Biodata
print("Nama", "\t\t", ": Bhayu Phermana Sachty Muktar")
print("Prodi", "\t\t", ": Matematika 2020")
print("NIM", "\t\t", ": 1305620001")
print("\033[95m","---------------------------------------------------------------------------------", "\033[00m")
print(" Membuat Perkalian 2 Matriks dengan ordo Mxp dan pxN sehingga hasilnya berordo MxN")
print("\033[95m","---------------------------------------------------------------------------------", "\033[00m")

#Input Matriks Pertama
print("\033[92m", "#############################", "\033[00m")
print("\033[92m", "### INPUT MATRIKS PERTAMA ###", "\033[00m")
print("\033[92m", "#############################", "\033[00m")

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

print()
print()

#Input Matriks Kedua
print("\033[92m", "###########################", "\033[00m")
print("\033[92m", "### INPUT MATRIKS KEDUA ###", "\033[00m")
print("\033[92m", "###########################", "\033[00m")

c=b
print("Jumlah Baris Matriks Kedua haruslah = Jumlah Kolom Matriks pertama yaitu ", c)     #Input Baris
d= int(input("Masukkan Jumlah Kolom: "))     #Input Kolom
print()

B=[]
for i in range (0, c):                       #Input List ke dalam List B
    B.append([])

for i in range (0,c):                        #Input Elemen Matriks
    for j in range (0,d):
        print("Baris", i+1, "Kolom", j+1)
        B[i].append(int(input("Elemen: ")))
print()
print("Matriks B : ", c," x ",d,"\n")
for i in range (0, c):                       #Print Matriks
    for j in range (0, d):
        print(B[i][j], end="  ")
    print()
print()
print(f'list B = {B}')                       #Print List Matriks

print()

#Perkalian Matriks A dan Matriks B
print("\033[92m", "#########################################", "\033[00m")
print("\033[92m", "### PERKALIAN MATRIKS A DAN MATRIKS B ###", "\033[00m")
print("\033[92m", "#########################################", "\033[00m")
C = []
for i in range(0,a):
    C.append([])
    for j in range(0, d):
        C[i].append(int(0))

for i in range(0,a):
    for j in range(0,d):
        s=0
        for k in range(0,c):
            s = s + A[i][k]*B[k][j]
            C[i][j]=s

#Print Matriks C
print("Matriks Perkalian C = A x B berordo ", a, " X ", d, "adalah", "\n")
for i in range (a):                       
    for j in range (d):
        print(C[i][j], end="  ")
    print()
print()
print(f'list C = {C}')                       

print()
print("\033[93m","\U0001F600", "TERIMA KASIH SUDAH MENGHITUNG PERKALIAN MATRIKS", "\U0001F600", "\033[00m")
print()