def jumlah_pecahan(n):
    if n == 0 :
        print("Tidak Dapat dicari karena membagi 0")
    elif n == 1 :
        return 1
    else:
        return (n/n + jumlah_pecahan(n-1))

a = int(input("Masukkan berapa n yang ingin dihitung : "))
print(jumlah_pecahan(a))


