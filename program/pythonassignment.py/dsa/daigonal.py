a = [[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]

mul = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[i])):
        sum=0
        for k in range(len(b[i])):
            mul[i][j] += a[i][k]*b[k][j]
        #print(sum,end=" ")
print(mul)
