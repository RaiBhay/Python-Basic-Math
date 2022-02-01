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
print("\033[92m", "####### INPUT MATRIKS BERORDO N X N #######", "\033[00m")
print("\033[92m", "###########################################", "\033[00m")
print()

a = int(input("Masukkan Jumlah Baris dan Kolom Matriks: "))

print()
matriks = []
for i in range (a):
    matriks.append([])

#FUNGSI INPUT DATA
def input_data(n):
    for i in range (0, a):
        print("Baris", n+1, "Kolom", i+1, ":")
        baris_satu = int(input("Elemen : "))
        matriks[n].append(baris_satu)

#FUNGSI DETERMINAN
def determinan(P):
    for l in range (0, a-1):
        for i in range (l+1, a):
            k = P[i][l]/P[l][l]
            for j in range (l, a):
                P[i][j]= P[i][j]-(P[l][j]*k)
    det = 1
    for p in range (0, a):
        det = det*P[p][p]
    return det

#FUNGSI HASIL KALI MATRIKS
def hasil_kali(Q, R):
    S = []
    for i in range(0,a):
        S.append([])
        for j in range(0, a):
            S[i].append(int(0))

    for i in range(0,a):
        for j in range(0,a):
            s=0
            for k in range(0,a):
                s = s + Q[i][k]*R[k][j]
                S[i][j]= s
    return S

#INPUT MATRIKS A
print("Matriks A")
matriks = []
for i in range (a):
    matriks.append([])
for i in range (0, a):
    input_data(i)
A = matriks

print()

#PRINT MATRIKS 
print("Matriks A")
for i in range (0, a):
    print (A[i])
print()

#INPUT MATRIKS B
print("Matriks B")
matriks = []
for i in range (a):
    matriks.append([])
for i in range (0, a):
    input_data(i)
B = matriks

print()

#PRINT MATRIKS
print("Matriks B")
for i in range (0, a):
    print (B[i])
print()

#HASIL PERKALIAN MATRIKS
AB = hasil_kali(A, B)
print("Matriks Perkalian A x B adalah", "\n")
for i in range (a):                       #Print Matriks
    for j in range (a):
        print(AB[i][j], end="  ")
    print()
print()
print("Listnya : ", hasil_kali(A, B))

#MENCARI DETERMINAN MATRIKS
print()
print("Determinan A : ")
print("\033[95m", "Determinan Matriksnya adalah : ", determinan(A),"\033[00m")

print()
print("Determinan B : ")
print("\033[95m", "Determinan Matriksnya adalah : ", determinan(B),"\033[00m")

print()
print("Determinan AB : ")
print("\033[95m", "Determinan Matriksnya adalah : ", determinan(AB),"\033[00m")

#KESIMPULAN
print()
print("\033[93m","\U0001F600", "\t","\t","\t","TERIMA KASIH SUDAH MEMBUKTIKAN BAHWA","\t","\t","\t", "\U0001F600", "\033[00m")
print("\033[93m","\U0001F600","\t", "DETERMINAN MATRIKS A X DETERMINAN MATRIKS B = DETERMINAN MATRIKS AB","\t", "\U0001F600", "\033[00m")
print("\033[93m","\U0001F600","\t","\t","\t", "PADA MATRIKS PERSEGI ORDO N X N","\t","\t","\t", "\U0001F600", "\033[00m")
print()