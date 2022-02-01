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

print("Matriks A")
matriks = []
for i in range (a):
    matriks.append([])
for i in range (0, a):
    input_data(i)
A = matriks

print()

print("Matriks B")
matriks = []
for i in range (a):
    matriks.append([])
for i in range (0, a):
    input_data(i)
B = matriks

