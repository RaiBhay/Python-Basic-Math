modus = max(set(predikatlist), key= predikatlist.count)   #key buat apaan?
a = predikatlist.count(modus)
b = []
for i in predikatlist :
    if a-1 < predikatlist.count(i):
        b.append(i)
c = b[::a]                      #gak tau tanda apaan
modus1 = "Modus data adalah "
modus2 = []
if len(c)==1 :
    modus1 += str(c[0])
else:
    for i in c:
        modus2.append(str(i))
    modus1 += "&".join(modus2)   #join buat apa?

print("Modusnya adalah nilai predikat ", modus)