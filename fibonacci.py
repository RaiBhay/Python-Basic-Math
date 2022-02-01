def fibonacci(a,b, m):
    if m == 1:
        return a
    elif m == 2:
        return b
    else:
        return fibonacci(a, b, m-1) + fibonacci(a,b, m-2) 

a = int(input("Masukkan suku pertama a : "))
b = int(input("Masukkan suku kedua b: "))
m = int(input("Masukkan jumlah suku yang di mau: "))
print(fibonacci(a,b, m))

