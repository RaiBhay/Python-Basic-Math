print("-----------------------------------------------------")
print("------------ MENENTUKAN NILAI RATA-RATA -------------")
print("--- DAN BANYAKNYA DATA LEBIH DARI NILAI RATA-RATA ---")
print("-----------------------------------------------------")

data=[8, 8, 4, 6, 8, 9, 6, 5, 4, 7]
data_diatas_mean=[]
print("Data yang akan diidentifikasi")
print(data)
print("")

n = len(data)
jumlah = 0
for i in range(10):
    jumlah = jumlah + data[i]
rata_rata= jumlah/n
print("Rata-ratanya adalah ",rata_rata)
print("")

print("Data di atas Rata-rata")
for i in range(10):
    if data[i] > rata_rata:
        data_diatas_mean.append(data[i])
a= len(data_diatas_mean)
print(data_diatas_mean, " dengan banyaknya data yaitu", a)

print("")
print("Thank you")
print("")    
