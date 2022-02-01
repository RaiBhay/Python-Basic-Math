#Biodata
print("Nama", "\t\t", ": Bhayu Phermana Sachty Muktar")
print("Prodi", "\t\t", ": Matematika 2020")
print("NIM", "\t\t", ": 1305620001")
print("\033[95m","---------------------------------------------------------------------------------", "\033[00m")
print("\t","\t","Mencari Determinan Matriks A dengan ordo N x N")
print("\033[95m","---------------------------------------------------------------------------------", "\033[00m")
print()

#INPUT MATRIKS
print("\033[92m", "###########################################", "\033[00m")
print("\033[92m", "### INPUT MATRIKS PERSEGI BERORDO N X N ###", "\033[00m")
print("\033[92m", "###########################################", "\033[00m")
print()

a = int(input("Masukkan Jumlah Kolom Baris dan Kolom : "))        #Input Kolom & Baris Matriks N x N
A=[]
for i in range (0, a):                       #Input List ke dalam List A
    A.append([])

for i in range (0,a):                        #Input Elemen Matriks
    for j in range (0,a):
        print("Baris", i+1, "Kolom", j+1)
        A[i].append(int(input("Elemen: ")))
print()
print("\033[95m","Matriks A : ", a," x ",a,"\n","\033[00m")
for i in range (0, a):                       #Print Matriks
    for j in range (0, a):
        print(A[i][j], end="  ")
    print()
print()
print(f'list A = {A}')                       #Print List Matriks
print()

#MEMBUAT MATRIKS A N X N MENJADI MATRIKS SEGITIGA ATAS
for l in range (0, a-1):
    for i in range (l+1, a):
        k = A[i][l]/A[l][l]
        for j in range (l, a):
            A[i][j]= A[i][j]-(A[l][j]*k)

#PRINT MATRIKS SEGITIGA ATAS
print("\033[95m","Matriks Segitiga Atas A : ", a," x ",a,"\n","\033[00m")
for i in range (0, a):                       #Print Matriks
    for j in range (0, a):
        print(A[i][j], end="  ")
    print()
print()
print(f'list A = {A}')                       #Print List Matriks
print()

#Mencari Determinan Matriks A dengan ordo N x N
det = 1
for m in range (0, a):
    det = det*A[m][m]
print("\033[95m", "Determinan Matriks A dengan ordo ", a, " X ", a, " adalah : ", det,"\033[00m")

print()
print("\033[93m","\U0001F600", "TERIMA KASIH SUDAH MENGHITUNG DETERMINAN MATRIKS PERSEGI ORDO N X N", "\U0001F600", "\033[00m")
print()