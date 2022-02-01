C=[[1,4,7],[4,6,8],[4,6,2],[2,0,4]]
for i in range (0,4):
    for j in range (0,3):
        print(C[i][j], end=' ')
    print()

print()

D=[[4,3,2],[5,4,5],[9,3,6],[2,9,3]]
for k in range (0,4):
    for l in range (0,3):
        print(D[k][l], end=' ')
    print()

print()

for m in range (0,4):
    for n in range (0,3):
        print(C[m][n]+D[m][n], end=' ')
    print()
