print("-----MENENTUKAN NILAI KELULUSAN MAHASISWA UNJ 2021-----")
print("-------------------------------------------------------")
a = int(input("Banyaknya Data : "))

nama_mahasiswa=[]
nilai_mahasiswa=[]

for i in range(a):
    nama_mahasiswa.append(input("Masukkan Nama Mahasiswa :"))
    nilai_mahasiswa.append(float(input("Masukkan Nilai Mahasiswa :")))
    print("-----")

print("---------------------------------------")
print("-----DAFTAR MAHASISWA DAN NILAINYA-----")
print("---------------------------------------")
for i in range(a):
    print(nama_mahasiswa[i]," dengan nilai ", nilai_mahasiswa[i])    
print("-----")

n  = len(nilai_mahasiswa)
jumlah = 0
for i in range (0,n):
    jumlah = jumlah + nilai_mahasiswa[i]
rata_rata= float(jumlah/n)
print("Nilai Rata-ratanya adalah ", rata_rata)
print("")
print("----------------------------------------------")
print("-----PENGUMUMAN KELULUSAN NILAI MAHASISWA-----")
print("----------------------------------------------")

for i in range(a):
    if nilai_mahasiswa[i] > rata_rata:
        print(nama_mahasiswa[i], " dengan nilai ", nilai_mahasiswa[i], " dinyatakan lulus")
    else:
        print(nama_mahasiswa[i], " dengan nilai ", nilai_mahasiswa[i], " dinyatakan tidak lulus")



