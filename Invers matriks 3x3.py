#Biodata
print("Nama", "\t\t", ": Bhayu Phermana Sachty Muktar")
print("Prodi", "\t\t", ": Matematika 2020")
print("NIM", "\t\t", ": 1305620001")
print("\033[95m","---------------------------------------------------------------------------------", "\033[00m")
print("\t","\t","Mencari Invers Matriks persegi berordo 3 x 3")
print("\033[95m","---------------------------------------------------------------------------------", "\033[00m")
print()

#INPUT MATRIKS
print("\033[92m", "###########################################", "\033[00m")
print("\033[92m", "### INPUT MATRIKS PERSEGI BERORDO 3 X 3 ###", "\033[00m")
print("\033[92m", "###########################################", "\033[00m")
print()

a = 3                                        #Input Kolom & Baris Matriks 3 x 3
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

#MENENTUKAN DETERMINAN MATRIKS A : 3 X 3 (MENGGUNAKAN ATURAN SARRUS)
plus = (A[0][0]*A[1][1]*A[2][2])+(A[0][1]*A[1][2]*A[2][0])+(A[0][2]*A[1][0]*A[2][1]) 
minus = (A[2][0]*A[1][1]*A[0][2])+(A[2][1]*A[1][2]*A[0][0])+(A[2][2]*A[1][0]*A[0][1])

det = plus - minus
print("\033[92m","Determinan Matriks A adalah ", det, "\033[00m")
print()

#MENENTUKAN MINOR DAN KOFAKTOR MATRIKS A : 3 X 3
if det == 0 :
    print("Invers Tidak Dapat dicari karena determinan sama dengan 0")
    print("\033[93m","Maaf ya", "\U0001F600", " Anda Kurang Beruntung", "\033[00m")
    print()
else :
    #MENENTUKAN MINOR ACUAN KOLOM 
    M = []
    for i in range (0, a):                       #Input List ke dalam List M
        M.append([0,0,0])

    #KOLOM PERTAMA
    M[0][0]= ((A[1][1]*A[2][2])-(A[2][1]*A[1][2]))
    M[1][0]= -1*((A[0][1]*A[2][2])-(A[2][1]*A[0][2]))
    M[2][0]= ((A[0][1]*A[1][2])-(A[1][1]*A[0][2]))
    #KOLOM KEDUA
    M[0][1]= -1*((A[1][0]*A[2][2])-(A[2][0]*A[1][2]))
    M[1][1]= ((A[0][0]*A[2][2])-(A[2][0]*A[0][2]))
    M[2][1]= -1*((A[0][0]*A[1][2])-(A[1][0]*A[0][2]))
    #KOLOM KETIGA
    M[0][2]= ((A[1][0]*A[2][1])-(A[2][0]*A[1][1]))
    M[1][2]= -1*((A[0][0]*A[2][1])-(A[2][0]*A[0][1]))
    M[2][2]= ((A[0][0]*A[1][1])-(A[1][0]*A[0][1]))

    print("\033[95m","Matriks KOFAKTOR A : ", a," x ",a,"\n", "\033[00m")
    for i in range (0, a):                       
        for j in range (0, a):
            print(M[i][j], end="  ")
        print()
    print()
    print(f'list A = {M}')                       
    print()

    #MENENTUKAN ADJOIN MATRIKS A : 3 X 3
    J = []
    for i in range (3):
        J.append([0,0,0])

    for i in range (3):
        for j in range (3):
            J[i][j]= M[j][i]

    print("\033[95m","Matriks Adjoin A : ", a," x ",a,"\n", "\033[00m")
    for i in range (0, a):                  
        for j in range (0, a):
            print(J[i][j], end="  ")
        print()
    print()
    print(f'list A = {J}')                        
    print()
    
    #INVERS MATRIKS A : 3 X 3 ((1/det)*Adjoin A)
    I = []
    for k in range (3):
        I.append([])

    o = 1/det
    for i in range (0,a):
        for j in range (0,a):
            u = o*J[i][j]
            I[i].append(u)

    #PRINT INVERS MATRIKS A : 3 X 3
    print("\033[95m","Matriks Invers A : ", a," x ",a,"\n", "\033[00m")
    for i in range (0, a):                       
        for j in range (0, a):
            print(I[i][j], end="  ")
        print()
    print()
    print(f'list A = {I}')                       
    print()

print()
print("\033[93m","\U0001F600", "TERIMA KASIH SUDAH MENGHITUNG INVERS MATRIKS PERSEGI ORDO 3 X 3", "\U0001F600", "\033[00m")
print()