print("-----------------------------------------------------")
print("------------ MENENTUKAN NILAI RATA-RATA -------------")
print("--- DAN BANYAKNYA DATA LEBIH DARI NILAI RATA-RATA ---")
print("-----------------------------------------------------")

data=[7, 6, 5, 5, 7, 8, 7, 8, 7, 9, 5, 7, 6, 5, 9, 8, 5, 6, 7, 8, 9, 6, 5, 7, 4]
data_diatas_mean=[]
print("Data yang akan diidentifikasi")
print(data)
print("")

n = len(data)
jumlah = 0
for i in range(n):
    jumlah = jumlah + data[i]
print("Jumlahnya adalah ", jumlah)
rata_rata= jumlah/n
print("Rata-ratanya adalah ",rata_rata)
print("")

print("Data di atas Rata-rata")
for i in range(n):
    if data[i] > rata_rata:
        data_diatas_mean.append(data[i])
a= len(data_diatas_mean)
print(data_diatas_mean, " dengan banyaknya data yaitu", a)
print("")
print("Thank you")
print("")    
