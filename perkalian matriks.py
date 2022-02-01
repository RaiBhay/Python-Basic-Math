A=[[1,4,7],[4,6,8],[4,6,2]]
for i in range (0,3):
    for j in range (0,3):
        print(A[i][j], end=' ')
    print()

print()

B=[[4,3,2],[5,4,5],[9,3,6]]
for k in range (0,3):
    for l in range (0,3):
        print(B[k][l], end=' ')
    print()

hasil=[[],[],[]]

#Perkalian Baris 1
print()
jumlah=0
jumlah_1=0
jumlah_2=0
for m in range (0,3):
    p = A[0][m]*B[m][0]
    jumlah=jumlah+p
hasil[0].append(int(jumlah))

for m in range (0,3):
    p = A[0][m]*B[m][1]
    jumlah_1=jumlah_1+p
hasil[0].append(int(jumlah_1))

for m in range (0,3):
    p = A[0][m]*B[m][2]
    jumlah_2=jumlah_2+p
hasil[0].append(int(jumlah_2))

#Perkalian Baris 2
print()
jumlah_3=0
jumlah_4=0
jumlah_5=0
for m in range (0,3):
    p = A[1][m]*B[m][0]
    jumlah_3=jumlah_3+p
hasil[1].append(int(jumlah_3))

for m in range (0,3):
    p = A[1][m]*B[m][1]
    jumlah_4=jumlah_4+p
hasil[1].append(int(jumlah_4))

for m in range (0,3):
    p = A[1][m]*B[m][2]
    jumlah_5=jumlah_5+p
hasil[1].append(int(jumlah_5))

#Perkalian Baris 3
print()
jumlah_6=0
jumlah_7=0
jumlah_8=0
for m in range (0,3):
    p = A[2][m]*B[m][0]
    jumlah_6=jumlah_6+p
hasil[2].append(int(jumlah_6))

for m in range (0,3):
    p = A[2][m]*B[m][1]
    jumlah_7=jumlah_7+p
hasil[2].append(int(jumlah_7))

for m in range (0,3):
    p = A[2][m]*B[m][2]
    jumlah_8=jumlah_8+p
hasil[2].append(int(jumlah_8))

print("List hasil kalinya : ",hasil)
print()
print("Matriksnya : ")
for n in range (0,3):
    for o in range (0,3):
        print(hasil[n][o], end=' ')
    print()