print("\n")
print("MENAMBAH DATA DI LIST")
print()
n = int(input("Banyak data: "))
print()
nilaimhs = [0]
namamhs = ["0"]
predikat = []
for i in range (n):
    namamhs.append(str(input("Nama mhs: ")))
    nilaimhs.append(int(input("Masukkan nilai: ")))

for i in range(1, n+1):
    if nilaimhs[i]>85:
        predikat = "A"
    elif 80< nilaimhs[i]< 86 :
        predikat = "A-"
    elif 75 <= nilaimhs[i]<=80 :
        predikat = "B+"
    elif 70< nilaimhs[i]<75 :
        predikat = "B"
    elif 65< nilaimhs[i]<=70 :
        predikat = "B-"
    elif 60< nilaimhs[i]<=65 :
        predikat = "C+"
    elif 55< nilaimhs[i]<=60 :
        predikat = "C"
    elif 50< nilaimhs[i]<=55 :
        predikat = "C-"
    elif 45< nilaimhs[i]<=50 :
        predikat = "D"
    else:
        predikat = "E"
        
print()
print("------------------------------------")
print("Nama mhs", "\t", "Nilai", "\t", "Predikat")
print("------------------------------------")
for i in range (1,n+1) :
    print(namamhs[i], "\t\t",nilaimhs[i], "\t\t", predikat[i])
