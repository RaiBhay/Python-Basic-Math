def ulangi():
    print("Masukkan Bilangan yang ingin diperiksa..")
    faktor = 1
    bilangan = int(input())
    if bilangan > 1:
        while True:    #This simulates a Do Loop
            faktor = faktor + 1
            if not(bilangan % faktor != 0): break   #Exit loop
        if faktor == bilangan:
            print(str(bilangan) + " Merupakan Bilangan Prima")
        else:
            print(str(bilangan) + " Bukan Bilangan Prima karena habis dibagi oleh " + str(faktor))
    else:
        print("Bukan Bilangan Prima karena <1")
    print("Apakah ingin mencoba lagi? (Y/T)")
    coba = input()
    if coba == "Y":
        pass
    else:
        while coba != "T":
            print("Silahkan Masukkan Huruf Y/T")
            coba = input()
            while coba == "Y":
                ulangi()
        print("Terima Kasih sudah memakai jasa ini")
        quit()
    return coba    

# Main
print("Memeriksa apakah suatu bilangan merupakan prima atau bukan")
print("Masukkan Bilangan yang ingin diperiksa..")
faktor = 1
bilangan = int(input())
if bilangan > 1:
    while True:    #This simulates a Do Loop
        faktor = faktor + 1
        if not(bilangan % faktor != 0): break   #Exit loop
    if faktor == bilangan:
        print(str(bilangan) + " Merupakan Bilangan Prima")
    else:
        print(str(bilangan) + " Bukan Bilangan Prima karena habis dibagi oleh " + str(faktor))
else:
    print("Bukan Bilangan Prima karena <1")
print("Apakah ingin mencoba lagi? (Y/T)")
coba = input()
while coba == "Y":
    ulangi()
while coba != "T":
    print("Silahkan Masukkan Huruf Y/T")
    coba = input()
    while coba == "Y":
        ulangi()
print("Terima Kasih sudah memakai jasa ini")
