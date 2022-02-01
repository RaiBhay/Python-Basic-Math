print("Mencari nilai terbesar dan nilai terkecil")
data=[8, 5, 7, 4, 3, 6]
print(data)
print("")
for i in data :
    print (i)
data.sort()
print(data)
print("")
for i in range (6) :
    print (data[i])
print("")

print("Nilai terbesar adalah")
maksimal=data[0]
for a in data :
    if a > maksimal:
        maksimal=a
print(maksimal,"data ke " ,i)

print("Nilai terkecil adalah")
minimal=data[0]
for b in data :
    if b< minimal:
        minimal=b
print (minimal)

print("")
print("Nilai terbesarnya adalah ", max(data))
print("Nilai terkecilnya adalah ", min(data))
