nilai=[80, 70, 65, 90, 85]
print(nilai)
for j in range(0, len(nilai)-1):
    for i in range(0, (len(nilai)-1)-j):
        if nilai[i] > nilai[i+1] :
            p = nilai[i+1]
            nilai[i+1] = nilai[i]
            nilai[i] = p
print(nilai)

if len(nilai)%2 == 0 :
    a = int(len(nilai)/2)
    b =(nilai[a-1] + nilai[a])/2
    median = str(b)
else:
    a = int((len(nilai)+1)/2)
    median = str(nilai[a-1])

print("Median data adalah ", median)



        
