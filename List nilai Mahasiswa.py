print("-----------------------------------------------------------------------------")
print("MENAMBAH DATA DI LIST NAMA MAHASISWA, NILAI MAHASISWA, PREDIKAT DAN KELULUSAN")
print("-----------------------------------------------------------------------------")
n = int(input("Banyak data: "))
print()
nilaimhs = []
namamhs = []
predikatlist = []
kelulusan = []
for i in range (n):
    namamhs.append(str(input("Nama mhs: ")))
    nilaimhs.append(int(input("Masukkan nilai: ")))
    print("---")

for i in range(n):
    if nilaimhs[i]>85:
        predikat = "A"
    elif nilaimhs[i]>80 :
        predikat = "A-"
    elif nilaimhs[i]>74 :
        predikat = "B+"
    elif nilaimhs[i]>70 :
        predikat = "B"
    elif nilaimhs[i]>65 :
        predikat = "B-"
    elif nilaimhs[i]>60 :
        predikat = "C+"
    elif nilaimhs[i]>55 :
        predikat = "C"
    elif nilaimhs[i]>50 :
        predikat = "C-"
    elif nilaimhs[i]>45 :
        predikat = "D"
    else:
        predikat = "E"
    predikatlist.append(str(predikat))

jumlah = 0
for i in range (0,n):
    jumlah = jumlah + nilaimhs[i]
rata_rata= float(jumlah/n)
print("Nilai Rata-rata kelas adalah ", rata_rata)

for i in range(n):
    for i in range(n):
        if nilaimhs[i]>60 :
            kelulusan.append("Lulus")
        else:
            kelulusan.append("Tidak Lulus")

print()
print("----------------------------------------------------------------")
print("Nama mhs", "\t", "Nilai", "\t\t", "Predikat", "\t", "Kelulusan")
print("----------------------------------------------------------------")
for i in range (n) :
    print(namamhs[i], "\t\t",nilaimhs[i], "\t\t", predikatlist[i], "\t\t", kelulusan[i])

print("")
print("---------------------")
print("Menentukan Modus Data")
print("---------------------")
print("")

