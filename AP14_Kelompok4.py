#Kelompok 4 (Pendidikan Matematika)
#Fadila Audia (1301620033)
#Dolly Fernando (1301620005)
#Muhammad Zaenul Karim (1301620024)
#Indri Rahman (1301620013)
#Neiluvar Muhammad Budiyanto (1301620037)
#Mutiah (1301620015)
#Indy Rizky Zakiya (1301620043)
#Yushak William Siahaan (1301620007)
#Aulia Iftinaf Fayyadh (1301620010)
#Retiana Rizkia (1301620022)
#Tia Wahyuningsih (1301620041)
#Fachrizal Nurrachman (1301620040)

#Kel 4 (Matematika)
#rizky kurnia (1305620026)
#natalie efrata susanti (1305620029) 
#david marcel lomak siahaan (1305620019)
#firdaus luthfi kurniawan (1305620037)
#Tasya'ul Khumairoh (1305620039)
#Bhayu Phermana Sachty Muktar (1305620001)
#Rafli Ahmad Fachrezi(1305620040)
#Febrina Nur Istiqomah(1305620022)

print("Menentukan Banyaknya Pasangan Kelinci Di Bulan Ke n")
print()
m=int(input("Masukkan Bulan Yang Diinginkan: "))
def LoopKelinci(m):
    if m < 0:
        print("Tidak Dapat Diproses Karena Bulan Kurang Dari 0")
        print()
    elif m == 0:
        return 0
    elif m == 1 or m == 2:
        return 1
    else:
        return LoopKelinci(m-1) + LoopKelinci(m-2)
print("Banyaknya Pasangan Kelinci Di Bulan Ke ",m," adalah ", LoopKelinci(int(m)))
