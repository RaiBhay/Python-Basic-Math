def jumlah_kelinci(n):
    a = 0
    A = []
    for i in range (0, n):
        a = a + A[i]
        A.append(a)
    return A

b = int(input("Masukkan jumlah bulan : "))
print(jumlah_kelinci(b))
